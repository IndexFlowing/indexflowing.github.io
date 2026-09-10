#!/usr/bin/env python3
"""Generate a blog illustration with Gemini on Vertex AI."""

from __future__ import annotations

import argparse
import base64
import mimetypes
import os
from io import BytesIO
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PROMPT = (
    "A warm editorial illustration for a blog post about learning Mandarin Chinese "
    "through films and TV shows, with a notebook, headphones, and subtle Chinese "
    "cinema motifs, clean composition, no text, landscape orientation"
)
DEFAULT_OUTPUT = Path("static/images/gemini-test.webp")
DEFAULT_MODEL = "gemini-3.1-flash-image"
DEFAULT_PROXY = "http://127.0.0.1:7897"
DEFAULT_LOCATION = "global"
DEFAULT_ASPECT_RATIO = "16:9"
FINAL_BANNER_RATIO = 5 / 2


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--prompt",
        default=DEFAULT_PROMPT,
        help="Image prompt (default: a Mandarin-learning blog illustration)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output image path (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--model",
        default=DEFAULT_MODEL,
        help=f"Gemini model to use (default: {DEFAULT_MODEL})",
    )
    parser.add_argument(
        "--aspect-ratio",
        default=DEFAULT_ASPECT_RATIO,
        help=f"Requested image aspect ratio (default: {DEFAULT_ASPECT_RATIO})",
    )
    parser.add_argument(
        "--check-config",
        action="store_true",
        help="Validate Vertex AI configuration and ADC without making a network request",
    )
    return parser.parse_args()


def save_image(data: bytes, mime_type: str | None, output: Path) -> Path:
    if not data:
        raise RuntimeError("Vertex AI returned an empty image.")

    output.parent.mkdir(parents=True, exist_ok=True)
    requested_webp = output.suffix.lower() == ".webp"

    if requested_webp:
        try:
            from PIL import Image

            with Image.open(BytesIO(data)) as image:
                if output.stem.endswith("-banner"):
                    width, height = image.size
                    target_width = round(height * FINAL_BANNER_RATIO)
                    if width >= target_width:
                        left = (width - target_width) // 2
                        image = image.crop((left, 0, left + target_width, height))
                    else:
                        image = image.resize((target_width, height))
                image.save(output, format="WEBP")
            return output
        except ImportError:
            print("Pillow is not installed; saving the returned image format instead.")
        except Exception as error:
            print(f"WebP conversion failed ({error}); saving the returned image format instead.")

    extension = mimetypes.guess_extension(mime_type or "") or ".bin"
    actual_output = output.with_suffix(extension) if requested_webp else output
    actual_output.write_bytes(data)
    return actual_output


def configuration() -> tuple[str | None, str, str]:
    project = os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("GCLOUD_PROJECT")
    location = os.environ.get("GOOGLE_CLOUD_LOCATION", DEFAULT_LOCATION)
    proxy = os.environ.get("GEMINI_PROXY", DEFAULT_PROXY)
    return project, location, proxy


def check_config() -> bool:
    project, location, proxy = configuration()
    problems: list[str] = []

    if not project:
        problems.append(
            "GOOGLE_CLOUD_PROJECT is missing; set it to the Google Cloud project ID "
            "that has Vertex AI enabled."
        )

    try:
        import google.auth

        google.auth.default(scopes=["https://www.googleapis.com/auth/cloud-platform"])
    except ImportError:
        problems.append(
            "Google authentication dependencies are missing; install scripts/requirements.txt."
        )
    except Exception:
        problems.append(
            "Application Default Credentials are unavailable; run `gcloud auth application-default login` "
            "and try again."
        )

    if problems:
        print("Vertex AI configuration needs attention:")
        for problem in problems:
            print(f"- {problem}")
        return False

    print("Vertex AI configuration looks ready (no network request was made).")
    print(f"Project: {project}")
    print(f"Location: {location}")
    print(f"Proxy: {proxy}")
    print("If generation fails, confirm that the Vertex AI API is enabled in this project.")
    return True


def generate_image(prompt: str, output: Path, model: str, aspect_ratio: str = DEFAULT_ASPECT_RATIO) -> Path:
    try:
        from google import genai
        from google.genai.types import GenerateContentConfig, ImageConfig, Modality
    except ImportError as error:
        raise RuntimeError(
            "Missing dependencies; install them with: "
            "python -m pip install -r scripts/requirements.txt"
        ) from error

    project, location, proxy = configuration()
    if not project:
        raise RuntimeError(
            "GOOGLE_CLOUD_PROJECT is not set. Set the Google Cloud project ID in .env "
            "and enable the Vertex AI API."
        )

    os.environ["HTTP_PROXY"] = proxy
    os.environ["HTTPS_PROXY"] = proxy
    os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "true"

    try:
        client = genai.Client(vertexai=True, project=project, location=location)
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=GenerateContentConfig(
                response_modalities=[Modality.TEXT, Modality.IMAGE],
                image_config=ImageConfig(aspect_ratio=aspect_ratio, image_size="1K"),
            ),
        )
    except Exception as error:
        message = str(error)
        if "credential" in message.lower() or "authentication" in message.lower():
            raise RuntimeError(
                "Vertex AI authentication failed. Run `gcloud auth application-default login` "
                "and confirm the account can access the project."
            ) from error
        if "permission" in message.lower() or "not found" in message.lower():
            raise RuntimeError(
                "Vertex AI rejected the request. Confirm GOOGLE_CLOUD_PROJECT is correct and "
                "the Vertex AI API is enabled for that project."
            ) from error
        raise RuntimeError(f"Vertex AI image generation failed: {message}") from error

    for candidate in getattr(response, "candidates", None) or []:
        content = getattr(candidate, "content", None)
        for part in getattr(content, "parts", None) or []:
            inline_data = getattr(part, "inline_data", None)
            data = getattr(inline_data, "data", None) if inline_data else None
            if data:
                if isinstance(data, str):
                    data = base64.b64decode(data)
                return save_image(
                    data,
                    getattr(inline_data, "mime_type", None),
                    output,
                )

    raise RuntimeError("Vertex AI returned no image data.")


def main() -> int:
    load_dotenv(PROJECT_ROOT / ".env")
    args = parse_args()
    if args.check_config:
        return 0 if check_config() else 1

    try:
        output = generate_image(args.prompt, args.output, args.model, args.aspect_ratio)
    except Exception as error:
        print(f"Image generation failed: {error}")
        return 1

    print(f"Saved generated image to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
