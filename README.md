# IndexFlowing

## Article image workflow

Articles live in bilingual Hugo Page Bundles under `content/en` and `content/zh`.
After writing or editing an article, check the pair and image status:

```text
python scripts/generate_article_image.py --check
```

Generate one article and its paired visual resource with:

```text
python scripts/generate_article_image.py content/en/products/example
```

Process only new or changed articles in batch mode with `--all`. Existing images are skipped; use `--force` to regenerate. The local index at `.agentbridge/article-image-state.json` records fingerprints, language pairs, resources, and processing times and is intentionally ignored by Git. If it is damaged, use `--check --rebuild-state` to recreate it.

Image generation uses the Vertex AI configuration consumed by `scripts/gemini_image.py`; configure `.env` before running a generation command. The script never rewrites article text or front matter.
