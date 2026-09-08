# Image Skill

## Purpose

This skill defines how visual assets are planned, generated, stored, referenced, and maintained for Hugo articles.

The goal is not to generate an image for every article.

The goal is to determine whether an article benefits from visual content, decide how many visual assets are appropriate, define the purpose of each asset, and generate a coherent visual system that improves comprehension, presentation, SEO, and GEO value.

Visual assets are article resources, not decorative attachments.

------

# 1. Core Principles

## 1.1 One article does not equal one image

An article may require:

- 0 images
- 1 image
- 2 images
- 3 images
- multiple images

The number of images must be determined by the article's information structure and visual communication needs.

Never generate images merely to satisfy a fixed image count.

------

## 1.2 Images must provide information value

Generate an image only when it provides at least one meaningful benefit:

- explains a concept
- visualizes a process
- shows relationships between concepts
- explains architecture
- illustrates a workflow
- communicates comparison
- presents data
- provides a concrete example
- improves understanding of a complex section
- provides a strong editorial hero image
- improves the visual hierarchy of a long-form article

Avoid decorative images that do not contribute to understanding.

Bad:

> Article: How to Use IndexNow

Image:

> A generic programmer sitting in front of a computer.

Good:

> A visual workflow showing a website submitting URLs through IndexNow to supported search engines.

------

## 1.3 Visual planning must happen before generation

Do not directly send the article to an image model with a generic prompt.

The workflow must be:

```text
Article
  ↓
Article Analysis
  ↓
Visual Planning
  ↓
Visual Brief
  ↓
Image Prompt
  ↓
Image Generation
  ↓
WebP Resource
  ↓
Page Bundle
  ↓
Markdown Reference
```

The visual plan determines:

- whether images are needed
- how many images are needed
- the purpose of each image
- the image type
- the placement
- the composition
- the visual style
- the relationship between multiple images

------

# 2. Visual Planning

For every article, determine:

```text
image_required
image_count
visual_assets
```

A visual plan should conceptually look like:

```json
{
  "image_required": true,
  "image_count": 2,
  "visual_assets": [
    {
      "id": "hero",
      "type": "editorial",
      "purpose": "Introduce the core idea",
      "placement": "article-intro",
      "required": true
    },
    {
      "id": "workflow",
      "type": "diagram",
      "purpose": "Explain the process",
      "placement": "after-workflow-section",
      "required": true
    }
  ]
}
```

The actual implementation may use a different JSON structure, but the semantic information must be preserved.

## 2.1 Visual Asset Placement

Each visual asset must state both why it exists and where it belongs. `purpose` explains the information or editorial job; `placement` describes its structural location in the article. Placement is not inferred from the filename and must not be reduced to "the article image".

Supported placement values are:

```text
hero             Article header or page-cover position; at most one is normally appropriate.
after_heading    Immediately after the matching heading and before that section's body.
before_heading   Immediately before the matching heading to introduce the section.
after_paragraph Immediately after a named or identified paragraph that the asset explains.
existing         An already-present resource whose location is preserved and not regenerated.
manual           A human-managed resource whose location and contents are preserved.
```

`after_heading`, `before_heading`, and `after_paragraph` should include a stable target identifier when the workflow inserts references. A plan may contain zero or any number of assets, and each asset is tracked independently with at least:

```json
{
  "id": "workflow",
  "type": "workflow",
  "source": "generated",
  "placement": "after_heading",
  "purpose": "Explain the submission sequence",
  "required": true,
  "path": "workflow.webp"
}
```

The workflow must preserve the distinction between the asset's semantic `type`, its ownership `source`, and its article `placement`. It must not use an article-level image count or a default filename as a substitute for this information.

## 2.2 Asset Ownership and Source

Every planned asset has one source:

```text
generated  Created by the configured image-generation workflow when explicitly planned.
manual     Supplied or maintained by a person; never overwritten or regenerated automatically.
existing   Already in the Page Bundle or a shared resource; inventory only unless explicitly re-planned.
```

`manual` and `existing` assets are read-only to the visual workflow. They must not be replaced during normal processing or `--force`. An existing screenshot, diagram, or other resource remains an asset even when it is not generated by Gemini.

English and Chinese versions should share the same asset identity and generated bytes where possible. Mirroring a generated resource must not change its type, purpose, or placement, and a manual/existing resource must not be copied over or replaced merely because its translation partner lacks a file. Resolve that difference explicitly.

------

# 3. When to Generate Zero Images

An article may legitimately require no images.

Use zero images when:

- the article is very short
- the content is primarily textual
- the article is a simple announcement
- images would add little information
- the article is primarily a reference page
- the content already contains sufficient real screenshots
- the article's subject is difficult to represent visually without creating misleading imagery

Do not force a hero image into every article.

------

# 4. Image Count Guidelines

Image count should depend on information density rather than word count.

### Simple article

Typical:

```text
0–1 images
```

Examples:

- short opinion
- announcement
- simple definition
- brief product update

### Standard article

Typical:

```text
1–3 images
```

Examples:

- practical tutorial
- product explanation
- learning guide
- conceptual article

### Complex technical article

Typical:

```text
2–5 images
```

Examples:

- system architecture
- engineering tutorial
- data pipeline
- SEO/GEO technical guide
- multi-stage workflow

### Very long technical or educational article

More than five images may be appropriate when each image provides distinct information.

Never split one visual concept into multiple images merely to increase image count.

------

# 5. Image Types

Use the following semantic image types.

## 5.1 Hero

Purpose:

- establish the article's visual identity
- communicate the main topic
- support article header presentation
- support social sharing when applicable

Typical count:

```text
0–1
```

Hero images should be visually strong but not overloaded with text.

------

## 5.2 Concept

Purpose:

Explain an abstract concept through visual metaphor or structured composition.

Examples:

- search indexing
- language acquisition
- knowledge graphs
- AI agents
- semantic search

------

## 5.3 Diagram

Purpose:

Represent:

- architecture
- components
- relationships
- system structure
- technical dependencies

Diagrams should prioritize information clarity over decoration.

------

## 5.4 Workflow

Purpose:

Explain a sequence or process.

Typical structure:

```text
Input
  ↓
Processing
  ↓
Transformation
  ↓
Output
```

Use this type for:

- tutorials
- automation
- SEO workflows
- deployment workflows
- data pipelines
- learning processes

------

## 5.5 Comparison

Purpose:

Show differences or relationships between multiple alternatives.

Examples:

- tools comparison
- framework comparison
- learning methods
- architecture alternatives

------

## 5.6 Example

Purpose:

Make an abstract explanation concrete.

Examples:

- example workflow
- example data structure
- example UI
- example learning scenario

------

## 5.7 Screenshot

Purpose:

Show a real interface, product, tool, or actual system.

Screenshots should be used when factual UI representation matters.

Do not generate fake screenshots when an actual screenshot is available or required.

------

## 5.8 Chart

Purpose:

Represent quantitative information.

Charts should only be generated when the underlying data is known and accurate.

Never invent data for a chart.

------

## 5.9 Editorial

Purpose:

Provide a high-quality editorial illustration for an article or section.

Use when a conceptual visual is valuable but a strict diagram is unnecessary.

------

# 6. Hero vs Inline Images

Hero images and inline images serve different purposes.

## Hero

Focus on:

- topic recognition
- visual identity
- composition
- editorial quality
- strong first impression

## Inline images

Focus on:

- explanation
- information density
- process
- relationships
- examples
- comprehension

Do not use a hero image as a substitute for explanatory diagrams.

------

# 7. Multiple Image Coherence

When an article requires multiple images, they must form a coherent visual system.

Maintain consistency in:

- visual language
- illustration style
- lighting
- perspective
- color palette
- typography treatment if any
- level of abstraction
- subject representation

For example:

```text
Article
├── hero.webp
├── architecture.webp
└── workflow.webp
```

These should look like they belong to the same article.

Do not generate three unrelated visual styles.

------

# 8. Text in Generated Images

Generated images should normally avoid readable text.

Default rule:

```text
No text
No labels
No fake UI text
No fake Chinese characters
No fake English paragraphs
```

Exceptions are allowed when text is essential to the visual explanation.

For diagrams, short labels may be useful if the image model can render them accurately.

If exact text accuracy is required, prefer:

- HTML
- Markdown
- SVG
- programmatically generated diagrams
- real screenshots

rather than relying on an image generation model.

------

# 9. Logos and Brands

Do not generate fake or distorted logos.

Avoid:

- invented company logos
- incorrect product logos
- fake trademarks
- distorted brand marks

When a real brand or product must be shown, prefer a real screenshot or approved brand asset when available.

------

# 10. AI Image Generation

The current default image generation backend is:

```text
Google Vertex AI
Gemini 3.1 Flash Image
```

The implementation should use the existing Gemini image generation wrapper rather than duplicating authentication and API logic.

The image generation layer should remain separate from article analysis and visual planning.

Conceptually:

```text
generate_article_visuals.py
        ↓
Visual Planner
        ↓
Gemini Image Client
```

The Gemini client is responsible for:

- authentication
- model invocation
- image output
- WebP conversion/output

The article workflow is responsible for:

- article analysis
- visual planning
- resource naming
- resource placement
- Markdown references
- processing state

------

# 11. Visual Brief

Before generating an image, create a structured visual brief.

A visual brief should contain, where relevant:

```text
Subject
Purpose
Visual type
Composition
Perspective
Main elements
Visual hierarchy
Style
Mood
Color direction
Background
Aspect ratio
Negative constraints
```

Example:

```text
Subject:
A Mandarin learner progressing from vocabulary acquisition to
real-world listening and conversation.

Purpose:
Visually communicate the progression from structured study to
authentic language exposure.

Type:
Editorial illustration.

Composition:
A clear left-to-right progression with three learning stages.

Style:
Modern editorial illustration suitable for a technology and
education publication.

Mood:
Focused, optimistic, intelligent.

Constraints:
No readable text, no logos, no watermark, no fake Chinese
characters, no excessive decorative elements.
```

The visual brief should be derived from the article, not invented independently of the content.

------

# 12. Prompt Generation

Image prompts should describe the visual solution rather than simply restating the article title.

Bad:

```text
Create an image about learning Chinese.
```

Good:

```text
Create a modern editorial illustration showing the progression
from structured Mandarin vocabulary study to authentic listening
through film dialogue and finally real-world conversation.

Use a clear visual progression, restrained composition, subtle
Chinese cultural references, and a professional educational
publication aesthetic.

Avoid readable text, logos, watermarks, fake Chinese characters,
and generic stock-photo aesthetics.
```

------

# 13. Page Bundle Storage

All article-specific visual resources should be stored inside the article's Page Bundle.

Preferred structure:

```text
content/en/products/my-article/
├── index.md
├── hero.webp
├── workflow.webp
└── example.webp
```

Do not place new article-specific images into:

```text
static/images/
```

unless the resource is genuinely shared across multiple unrelated pages.

------

# 14. File Naming

Image filenames must be:

- lowercase when practical
- stable
- descriptive
- URL-safe
- without spaces
- without unnecessary timestamps
- without random IDs

Preferred:

```text
hero.webp
workflow.webp
architecture.webp
comparison.webp
example.webp
```

Avoid:

```text
AI Image 2026.webp
gemini-test.webp
image123.webp
final-final-v2.webp
```

The Page Bundle provides the article context, so image filenames should remain concise.

------

# 15. WebP

WebP is the default generated image format for article assets.

Reasons:

- good web quality/size tradeoff
- broadly supported by modern browsers
- suitable for Hugo image processing
- appropriate for generated editorial assets

The workflow should prefer WebP unless a specific asset requires another format.

------

# 16. Markdown References

Images should be placed at the section where they provide the most value.

Example:

```markdown
The core idea behind the workflow is simple.

![Visual overview of the workflow](workflow.webp)

## How the process works

The first stage collects...
```

Do not automatically place every generated image at the top of the article.

Hero placement may depend on the Hugo theme/template.

------

# 17. Bilingual Articles

English and Chinese versions of the same article should share the same visual resources whenever possible.

Example:

```text
content/en/products/my-article/
├── index.md
└── hero.webp

content/zh/products/my-article/
└── index.md
```

If Hugo multilingual resource sharing permits a shared resource, use the shared resource.

Otherwise, duplicate the same generated asset into the corresponding language Page Bundle rather than generating a visually different image.

The important rule is:

> One article concept should have one visual identity across languages.

Do not independently generate unrelated EN and ZH versions of the same article unless there is a strong editorial reason.

------

# 18. Bilingual Source Direction

The source language may be either English or Chinese.

The workflow must not assume:

```text
English → Chinese
```

or:

```text
Chinese → English
```

Instead, identify the relationship between the two articles.

Possible states:

```text
EN only
ZH only
EN + ZH paired
Potentially paired but different slug
```

If both versions exist, generate the visual plan from the article concept rather than from one language alone.

------

# 19. State Tracking

The article visual workflow should maintain a local state index.

Recommended location:

```text
.agentbridge/article-image-state.json
```

The state file is a local processing cache and must not be required by Hugo.

It should normally be ignored by Git.

The state should track concepts such as:

```text
article path
language
paired article
content hash
visual plan
generated resources
processing status
last processed time
```

Example conceptual structure:

```json
{
  "version": 1,
  "articles": {
    "content/en/products/my-article/index.md": {
      "language": "en",
      "paired_article": "content/zh/products/my-article/index.md",
      "content_hash": "...",
      "status": "processed",
      "resources": [
        "hero.webp",
        "workflow.webp"
      ]
    }
  }
}
```

The exact implementation may evolve.

------

# 20. Incremental Processing

The workflow must be incremental.

Do not regenerate all article visuals on every execution.

A resource should be considered for reprocessing when:

- the article is new
- the article content changed
- the visual plan changed
- the paired article changed
- the expected image resource is missing
- the user explicitly requests regeneration

Otherwise:

```text
skip
```

------

# 21. Force Regeneration

Provide an explicit force mechanism.

Example:

```bash
python scripts/generate_article_visuals.py --force content/en/products/my-article/index.md
```

`--force` means:

> Ignore the current image processing state and regenerate the requested visual resources.

It must not silently rewrite unrelated articles.

------

# 22. Check Mode

Provide a non-generating inspection mode.

Example:

```bash
python scripts/generate_article_visuals.py --check
```

Check mode must not call the image generation API.

It should report:

- total articles
- new articles
- changed articles
- processed articles
- pending visual resources
- missing English/Chinese pairs
- potentially mismatched pairs
- missing image resources
- stale state entries

Example:

```text
Articles: 14
Paired: 14
New/changed: 2
Processed: 12

Pending visual planning: 2
Pending images: 4

Missing EN: 0
Missing ZH: 0
Potential pair mismatches: 1
```

------

# 23. Error Handling

The visual workflow must fail safely.

If:

- Gemini generation fails
- the state file is corrupted
- an article cannot be parsed
- a Page Bundle cannot be identified
- bilingual pairing is ambiguous

the workflow must report the problem clearly.

Do not silently delete resources.

Do not silently rewrite article content.

Do not mark an article as successfully processed if generation failed.

------

# 24. Article Content Safety

The image workflow must not rewrite the article body automatically except for narrowly scoped image-reference insertion.

Never automatically:

- rewrite paragraphs
- change article meaning
- change titles
- change descriptions
- change tags
- change categories
- translate articles
- restructure headings

Those are separate content operations.

------

# 25. Image Quality Review

Generated images should be evaluated for:

### Relevance

Does the image represent the actual article concept?

### Clarity

Can the reader understand what the image is communicating?

### Composition

Is the visual hierarchy clear?

### Consistency

Does it match the site's editorial visual language?

### Accuracy

Does it avoid false or misleading technical information?

### Artifacts

Check for:

- distorted objects
- malformed interfaces
- unreadable fake text
- broken diagrams
- strange hands/faces
- incorrect logos
- accidental watermarks

### Web suitability

Check:

- WebP output
- reasonable dimensions
- reasonable file size
- correct Page Bundle location

------

# 26. Technical Diagrams

Do not automatically use an image generation model for precise technical diagrams.

For diagrams requiring:

- exact labels
- exact arrows
- exact API names
- exact architecture
- exact data values

prefer deterministic generation such as:

- SVG
- Mermaid
- HTML/CSS
- programmatic SVG
- chart libraries

Gemini-generated illustrations are appropriate for conceptual diagrams, but not for information where exact textual accuracy is critical.

------

# 27. Screenshots

Screenshots should normally come from the actual product or application.

Do not use AI-generated screenshots as factual evidence.

Use AI-generated imagery for:

- editorial illustration
- conceptual visualization
- visual metaphor
- non-factual atmosphere

Use real screenshots for:

- UI tutorials
- product walkthroughs
- configuration instructions
- software documentation

------

# 28. SEO and GEO Considerations

Images should support the article's information architecture.

Good visual assets can:

- clarify concepts
- increase content comprehension
- improve page presentation
- create useful semantic context
- provide visual summaries
- support human readers

However:

> Do not generate images solely because they may improve SEO.

Search engines should not be manipulated with meaningless image volume.

The article remains the primary information source.

------

# 29. Visual Asset Planning Examples

## Example A — Simple Product Article

```text
Article:
What Is IndexFlow?

Visual plan:
hero
```

Result:

```text
my-article/
├── index.md
└── hero.webp
```

------

## Example B — Tutorial

```text
Article:
How to Submit a Sitemap

Visual plan:
hero
workflow
```

Result:

```text
my-article/
├── index.md
├── hero.webp
└── workflow.webp
```

------

## Example C — Technical Architecture

```text
Article:
How IndexFlow Processes URLs

Visual plan:
hero
architecture
data-flow
```

Result:

```text
my-article/
├── index.md
├── hero.webp
├── architecture.webp
└── data-flow.webp
```

------

## Example D — Text-First Article

```text
Article:
Why I Started Building IndexFlow

Visual plan:
no generated image
```

This is valid.

------

# 30. User Workflow

The normal workflow should be simple.

## Write the article

```text
content/en/products/my-article/index.md
```

and optionally:

```text
content/zh/products/my-article/index.md
```

## Check the visual state

```bash
python scripts/generate_article_visuals.py --check
```

## Generate visuals for one article

```bash
python scripts/generate_article_visuals.py content/en/products/my-article/index.md
```

## Generate all pending visuals

```bash
python scripts/generate_article_visuals.py --all
```

## Force regeneration

```bash
python scripts/generate_article_visuals.py --force content/en/products/my-article/index.md
```

The user should not need to manually construct Gemini prompts during normal operation.

------

# 31. Separation of Responsibilities

The system should maintain clear boundaries.

### Content Skill

Responsible for:

- article structure
- front matter
- writing quality
- SEO
- GEO
- categories
- tags
- multilingual content

### Image Skill

Responsible for:

- visual planning
- image count
- image type
- visual brief
- image prompts
- visual consistency
- image resources
- image quality

### Gemini Image Client

Responsible for:

- Vertex AI authentication
- Gemini model calls
- image generation
- WebP output

### Article Visual Workflow

Responsible for:

- connecting content and image systems
- bilingual pairing
- incremental state
- resource generation
- Markdown references
- batch processing

This separation must be preserved.

------

# 32. Final Principle

The system should optimize for:

```text
Useful visuals
>
More visuals
```

and:

```text
One coherent visual system
>
Many unrelated AI images
```

The objective is not:

> "Every article must have an AI image."

The objective is:

> "Every article should have the visual resources it actually needs to communicate its ideas effectively."
