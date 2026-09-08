#!/usr/bin/env python3
"""Check article translations and manage shared article illustrations incrementally."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONTENT_ROOT = PROJECT_ROOT / "content"
STATE_PATH = PROJECT_ROOT / ".agentbridge" / "article-image-state.json"
VISUAL_PLAN_PATH = PROJECT_ROOT / ".agentbridge" / "article-visual-plan.json"
SHARED_ASSET_ROOT = PROJECT_ROOT / "assets" / "images" / "articles"
SHARED_ASSET_PREFIX = "images/articles/"
STATE_VERSION = 1
LANGUAGES = ("en", "zh")
IMAGE_SUFFIXES = {".avif", ".gif", ".jpeg", ".jpg", ".png", ".webp"}
ASSET_TYPES = {"hero", "concept", "diagram", "workflow", "comparison", "example", "screenshot", "chart", "editorial"}
ASSET_SOURCES = {"generated", "manual", "existing"}
ASSET_PLACEMENTS = {"hero", "after_heading", "before_heading", "after_paragraph", "existing", "manual"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Check bilingual article pairs and manage shared article images."
    )
    target = parser.add_mutually_exclusive_group()
    target.add_argument("article", type=Path, nargs="?", help="Article file or Page Bundle path")
    target.add_argument("--all", action="store_true", help="Process all changed articles")
    parser.add_argument("--check", action="store_true", help="Check pairs and pending work without generating images")
    parser.add_argument("--force", action="store_true", help="Regenerate images even when resources already exist")
    parser.add_argument("--rebuild-state", action="store_true", help="Discard a damaged state file and rebuild it")
    parser.add_argument("--model", default="gemini-3.1-flash-image", help="Vertex AI Gemini image model")
    return parser.parse_args()


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def relative(path: Path) -> str:
    return path.relative_to(PROJECT_ROOT).as_posix()


def load_visual_plan() -> dict[str, list[dict]]:
    if not VISUAL_PLAN_PATH.exists():
        return {}
    try:
        plan = json.loads(VISUAL_PLAN_PATH.read_text(encoding="utf-8"))
        shared = {asset["id"]: asset for asset in plan.get("shared_assets", [])}
        by_article = {}
        for article in plan.get("articles", []):
            assets = []
            for planned in article.get("visual_assets", []):
                asset = dict(planned)
                shared_asset = shared.get(asset.get("id"), {})
                asset["path"] = shared_asset.get("path", asset.get("path", ""))
                assets.append(asset)
            by_article[article["path"]] = assets
        return by_article
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        raise RuntimeError(f"Visual plan is invalid at {VISUAL_PLAN_PATH}: {error}") from error


def shared_asset_path(path: str) -> Path:
    normalized = Path(path.replace("\\", "/"))
    if normalized.is_absolute() or normalized.as_posix() != path or not path.startswith(SHARED_ASSET_PREFIX):
        raise ValueError(f"Shared asset path must be relative to {SHARED_ASSET_PREFIX}: {path}")
    output = PROJECT_ROOT / "assets" / normalized
    if output.parent != SHARED_ASSET_ROOT and SHARED_ASSET_ROOT not in output.parents:
        raise ValueError(f"Shared asset path escapes {SHARED_ASSET_ROOT}: {path}")
    return output


def load_front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        match = re.match(r"^([A-Za-z][\w-]*)\s*:\s*(.+?)\s*$", line)
        if not match:
            continue
        key, value = match.groups()
        values[key.lower()] = value.strip().strip('"\'')
    return values


def content_fingerprint(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def image_resources(bundle: Path) -> list[str]:
    return sorted(relative(path) for path in bundle.iterdir() if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES)


def asset_from_path(path: str, source: str = "existing", placement: str = "existing") -> dict:
    name = Path(path).stem
    return {
        "id": name,
        "type": "screenshot" if source in {"manual", "existing"} else "editorial",
        "source": source,
        "placement": placement,
        "required": False,
        "path": path,
    }


def normalize_asset(asset: dict, fallback_path: str = "") -> dict:
    path = str(asset.get("path") or fallback_path)
    source = str(asset.get("source") or "generated").lower()
    placement = str(asset.get("placement") or "hero").lower()
    asset_type = str(asset.get("type") or "editorial").lower()
    if source not in ASSET_SOURCES:
        raise ValueError(f"Unsupported visual asset source: {source}")
    if placement not in ASSET_PLACEMENTS:
        raise ValueError(f"Unsupported visual asset placement: {placement}")
    if asset_type not in ASSET_TYPES:
        raise ValueError(f"Unsupported visual asset type: {asset_type}")
    return {
        "id": str(asset.get("id") or Path(path).stem or "asset"),
        "type": asset_type,
        "source": source,
        "placement": placement,
        "required": bool(asset.get("required", False)),
        "path": path,
        **({"purpose": str(asset["purpose"])} if asset.get("purpose") else {}),
    }


def visual_assets(article: dict, previous: dict | None = None, visual_plan: dict[str, list[dict]] | None = None) -> list[dict]:
    planned_from_file = (visual_plan or {}).get(article["path"])
    if planned_from_file:
        return [normalize_asset(asset) for asset in planned_from_file]
    planned = (previous or {}).get("visual_assets", [])
    if planned:
        return [normalize_asset(asset) for asset in planned]
    # Existing bundle files are inventory, not generation requests.
    return [asset_from_path(path) for path in article["resources"]]


def article_from_file(path: Path) -> dict:
    path = path.resolve()
    bundle = path.parent
    rel = path.relative_to(CONTENT_ROOT).parts
    if len(rel) < 3 or rel[0] not in LANGUAGES or path.name != "index.md":
        raise ValueError("Expected a Page Bundle index.md under content/en or content/zh.")
    front_matter = load_front_matter(path)
    language, section = rel[0], rel[1]
    slug = bundle.name
    translation_key = front_matter.get("translationkey") or front_matter.get("translation_key")
    return {
        "path": relative(path),
        "language": language,
        "section": section,
        "slug": slug,
        "translation_key": translation_key or "",
        "title": front_matter.get("title", ""),
        "date": front_matter.get("date", ""),
        "fingerprint": content_fingerprint(path),
        "mtime_ns": path.stat().st_mtime_ns,
        "resources": image_resources(bundle),
    }


def discover_articles() -> list[dict]:
    articles = []
    for language in LANGUAGES:
        for path in sorted((CONTENT_ROOT / language).glob("**/index.md")):
            articles.append(article_from_file(path))
    return articles


def load_state(rebuild: bool) -> dict:
    if not STATE_PATH.exists():
        return {"version": STATE_VERSION, "updated_at": now(), "articles": {}}
    try:
        state = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        if state.get("version") != STATE_VERSION or not isinstance(state.get("articles"), dict):
            raise ValueError("unsupported state format")
        return state
    except (OSError, json.JSONDecodeError, ValueError) as error:
        if not rebuild:
            raise RuntimeError(
                f"State index is invalid at {STATE_PATH}: {error}. Re-run with --rebuild-state."
            ) from error
        print(f"Warning: rebuilding invalid state index ({error}).")
        return {"version": STATE_VERSION, "updated_at": now(), "articles": {}}


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    temporary = STATE_PATH.with_suffix(".tmp")
    temporary.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(STATE_PATH)


def pair_articles(articles: list[dict]) -> tuple[dict[str, dict], list[tuple[dict, dict]]]:
    by_path = {article["path"]: article for article in articles}
    by_key: dict[tuple[str, str], list[dict]] = {}
    for article in articles:
        key = article["translation_key"] or article["slug"]
        by_key.setdefault((article["section"], key), []).append(article)
    pairs: dict[str, dict] = {}
    suspicious: list[tuple[dict, dict]] = []
    for group in by_key.values():
        languages = {item["language"] for item in group}
        if languages == set(LANGUAGES) and len(group) == 2:
            first, second = group
            pairs[first["path"]] = second
            pairs[second["path"]] = first
    # A shared date and a similar Latin title is useful as a warning, never as an automatic pair.
    for article in articles:
        if article["path"] in pairs:
            continue
        candidates = [item for item in articles if item["language"] != article["language"] and item["section"] == article["section"]]
        for candidate in candidates:
            left = set(re.findall(r"[a-z0-9]+", article["title"].lower()))
            right = set(re.findall(r"[a-z0-9]+", candidate["title"].lower()))
            if article["date"] and article["date"] == candidate["date"] and left and len(left & right) >= 2:
                suspicious.append((article, candidate))
                break
    return pairs, suspicious


def update_records(
    state: dict,
    articles: list[dict],
    pairs: dict[str, dict],
    visual_plan: dict[str, list[dict]],
) -> tuple[list[dict], list[dict]]:
    old = state.get("articles", {})
    current = {article["path"]: article for article in articles}
    changed, unchanged = [], []
    for article in articles:
        previous = old.get(article["path"], {})
        article["paired_path"] = pairs.get(article["path"], {}).get("path", "")
        article["status"] = previous.get("status", "new")
        article["last_processed_at"] = previous.get("last_processed_at", "")
        article["last_error"] = previous.get("last_error", "")
        article["visual_assets"] = visual_assets(article, previous, visual_plan)
        is_changed = previous.get("fingerprint") != article["fingerprint"] or previous.get("paired_path", "") != article["paired_path"]
        (changed if is_changed or not previous else unchanged).append(article)
    state["articles"] = current
    state["updated_at"] = now()
    return changed, unchanged


def print_report(articles: list[dict], changed: list[dict], suspicious: list[tuple[dict, dict]]) -> None:
    missing = [item for item in articles if not item["paired_path"]]
    pending = [
        asset
        for item in articles
        for asset in item["visual_assets"]
        if asset["source"] == "generated"
        and (not asset["path"] or not shared_asset_path(asset["path"]).exists())
        ]
    missing_manual = [
        asset
        for item in articles
        for asset in item["visual_assets"]
        if asset["source"] in {"manual", "existing"}
        and asset["path"]
        and not shared_asset_path(asset["path"]).exists()
    ]
    print(f"Articles: {len(articles)} | new/changed: {len(changed)} | processed/resources: {sum(bool(item['resources']) for item in articles)}")
    print(f"Visual assets: {sum(len(item['visual_assets']) for item in articles)} | pending generated assets: {len(pending)}")
    if missing_manual:
        unique = {asset["path"] for asset in missing_manual}
        print(f"Missing manual/existing shared assets: {len(unique)}")
        for path in sorted(unique):
            print(f"- {path}")
    if missing:
        print("Missing bilingual pair:")
        for item in missing:
            print(f"- {item['language']}: {item['path']}")
    if suspicious:
        print("Possible slug-mismatched pairs (review manually):")
        for left, right in suspicious:
            print(f"- {left['path']} <-> {right['path']}")


def build_prompt(article: dict, partner: dict | None) -> str:
    partner_title = partner["title"] if partner else ""
    return (
        "Create a clean editorial illustration for a bilingual blog article. "
        "No words, letters, logos, captions, or watermarks. Landscape 16:9 composition, "
        "warm modern palette, clear focal subject, suitable as a Hugo article cover.\n"
        f"Article title: {article['title']}\n"
        f"Chinese/English companion title: {partner_title}\n"
        f"Article language: {article['language']}\n"
        "Use the article subject and learning context as visual inspiration, not literal text."
    )


def generate_for(article: dict, asset: dict, partner: dict | None, force: bool, model: str) -> None:
    if not asset["path"]:
        asset["path"] = f"{SHARED_ASSET_PREFIX}{asset['id']}.webp"
    output = shared_asset_path(asset["path"])
    if asset["source"] != "generated":
        return
    if output.exists() and not force:
        return
    from gemini_image import generate_image

    output.parent.mkdir(parents=True, exist_ok=True)
    generate_image(build_prompt(article, partner), output, model)


def main() -> int:
    args = parse_args()
    if not args.article and not args.all and not args.check:
        print("Choose an article path, --all, or --check. See --help for examples.", file=sys.stderr)
        return 2
    try:
        state = load_state(args.rebuild_state)
        visual_plan = load_visual_plan()
        articles = discover_articles()
        pairs, suspicious = pair_articles(articles)
        changed, _ = update_records(state, articles, pairs, visual_plan)
        selected = articles
        if args.article:
            target = (PROJECT_ROOT / args.article).resolve()
            if target.is_dir():
                target /= "index.md"
            selected = [item for item in articles if (PROJECT_ROOT / item["path"]).resolve() == target]
            if not selected:
                raise ValueError(f"Article not found in content Page Bundles: {args.article}")
        elif not args.all:
            selected = []
        print_report(articles, changed, suspicious)
        if args.check:
            save_state(state)
            return 0
        for article in selected:
            partner = pairs.get(article["path"])
            if not partner:
                print(f"Skipping without bilingual pair: {article['path']}")
                state["articles"][article["path"]]["status"] = "missing_pair"
                continue
            assets = state["articles"][article["path"]].get("visual_assets", [])
            for asset in assets:
                if asset["source"] != "generated":
                    continue
                primary = article if article["language"] == "en" else partner
                primary_record = state["articles"][primary["path"]]
                primary_assets = primary_record.get("visual_assets", [])
                primary_asset = next((item for item in primary_assets if item["id"] == asset["id"]), asset)
                generate_for(primary, primary_asset, pairs.get(primary["path"]), args.force, args.model)
            for path in (article["path"], partner["path"]):
                record = state["articles"][path]
                record["resources"] = image_resources((PROJECT_ROOT / path).parent)
                state["articles"][path]["status"] = "processed"
                state["articles"][path]["last_processed_at"] = now()
                state["articles"][path]["last_error"] = ""
        save_state(state)
        return 0
    except (RuntimeError, ValueError, OSError) as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    raise SystemExit(main())
