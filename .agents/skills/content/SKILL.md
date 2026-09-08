# Hugo Content Skill

## 1. Purpose

This skill defines the content production rules for the Hugo website.

The website is the personal developer content hub for:

- Personal developer brand
- Product development
- Engineering
- Open source
- Indie development
- Growth experiments
- Build in Public

All articles created for this Hugo project MUST follow the rules in this document.

The canonical article lives in the Hugo repository.

External platforms such as X, Medium, LinkedIn, Reddit, and other distribution channels may use adapted versions of the canonical article, but should NOT blindly duplicate the original article.

------

# 2. Content Architecture

The website uses five top-level categories.

These categories are fixed and should NOT be expanded without explicit approval.

```text
Products
Engineering
Growth
Thoughts
Open Source
```

## Category meanings

### Products

Use for content primarily about products being built, launched, improved, or operated.

Examples:

- Product launches
- Product updates
- Feature announcements
- Product decisions
- Product experiments
- Product roadmaps
- Lessons from building a product

Example:

```yaml
categories:
  - Products
```

------

### Engineering

Use for technical implementation and engineering knowledge.

Examples:

- Architecture
- Rust
- Go
- Hugo
- Cloudflare
- Database design
- APIs
- Performance
- Infrastructure
- Development techniques
- Technical debugging

Example:

```yaml
categories:
  - Engineering
```

------

### Growth

Use for traffic, SEO, GEO, distribution, marketing, audience building, and indie developer growth.

Examples:

- SEO
- GEO
- Content distribution
- Search indexing
- Growth experiments
- Building an audience
- X growth
- Product marketing
- Content marketing

Example:

```yaml
categories:
  - Growth
```

------

### Thoughts

Use for personal opinions, decisions, reflections, and lessons that are not primarily technical.

Examples:

- Why I started a project
- Independent developer reflections
- Business decisions
- Lessons learned
- Opinions about AI development
- Personal development philosophy
- Build in Public reflections

Example:

```yaml
categories:
  - Thoughts
```

------

### Open Source

Use for content primarily focused on open-source projects and the open-source ecosystem.

Examples:

- Open-source project releases
- Open-source architecture
- GitHub project updates
- Open-source contribution
- Community building
- Release announcements
- Lessons from maintaining open source

Example:

```yaml
categories:
  - Open Source
```

------

# 3. Category Rules

Categories describe WHAT KIND OF CONTENT the article is.

Rules:

1. Use exactly one primary category whenever possible.
2. Do NOT create new top-level categories.
3. Do NOT use product names as categories.
4. Do NOT use technologies as categories.
5. Do NOT create categories such as:
   - SEO
   - AI
   - Rust
   - Technology
   - Tutorials
   - Projects
   - Development
6. Those concepts belong in tags.

When an article could fit multiple categories, choose the category representing its primary purpose.

------

# 4. Tags

Tags describe the subjects, products, technologies, or concepts discussed in an article.

Multiple tags are allowed.

## Product tags

Product names are important tags.

Current products:

```text
IndexFlow
MandarinClips
AgentBridge
```

IMPORTANT:

Use:

```text
IndexFlow
```

NOT:

```text
IndexFlowing
```

`IndexFlowing` refers to the broader brand/project ecosystem.

`IndexFlow` is the product name.

------

# 5. Technology Tags

Technology names may be used as tags when relevant.

Examples:

```text
Rust
Go
Hugo
MCP
TypeScript
JavaScript
Next.js
Cloudflare
Docker
Kubernetes
PostgreSQL
SQLite
```

Only add a technology tag when the article meaningfully discusses that technology.

Do NOT add technology tags merely for SEO.

------

# 6. Topic Tags

Relevant topic tags may include:

```text
AI
SEO
GEO
Open Source
Indie Hacker
Build in Public
Content Marketing
Search Indexing
Developer Tools
```

Only use tags that are genuinely relevant to the article.

Avoid excessive tags.

Recommended:

```yaml
tags:
  - IndexFlow
  - Rust
  - SEO
  - GEO
```

Avoid:

```yaml
tags:
  - IndexFlow
  - Rust
  - SEO
  - GEO
  - AI
  - Technology
  - Programming
  - Software
  - Internet
  - Developer
  - Website
  - Tools
```

The goal is meaningful taxonomy, not keyword stuffing.

------

# 7. Front Matter

Every article should have a complete Front Matter.

Recommended structure:

```yaml
---
title: "Article Title"
date: 2026-09-08
description: "A concise description of the article."
categories:
  - Engineering
tags:
  - IndexFlow
  - Rust
---
```

Use the project's existing Hugo Front Matter conventions when they already exist.

Do NOT introduce a new Front Matter format unnecessarily.

------

# 8. Title Rules

Titles should be:

- Clear
- Specific
- Human-readable
- Useful to readers
- Suitable for search engines

Avoid:

```text
The Ultimate Guide to Everything About...
```

Avoid excessive clickbait.

Prefer:

```text
Why I Built IndexFlow Instead of Using Another SEO Tool
```

or:

```text
How I Designed IndexFlow's URL Indexing Pipeline
```

------

# 9. Description Rules

The description should explain the article clearly in one or two sentences.

It should:

- Describe the actual article
- Be useful for search results
- Avoid keyword stuffing
- Avoid repeating the title mechanically

Example:

```yaml
description: "The engineering decisions behind IndexFlow's URL indexing pipeline and why I chose an open-source approach."
```

------

# 10. Slug Rules

Use short, readable, stable URLs.

Prefer:

```text
why-i-built-indexflow
indexflow-indexing-pipeline
hugo-multilingual-site
```

Avoid:

```text
article-2026-09-08-final-version-2
my-new-blog-post
```

Do not change an existing published URL unless there is a strong reason.

URL stability is important.

------

# 11. Article Structure

Long-form articles should generally follow a clear information structure.

Recommended structure:

```text
Problem
↓
Context
↓
Approach
↓
Implementation / Experience
↓
Result
↓
Lessons
↓
Conclusion
```

When appropriate, use the SCQA framework:

```text
Situation
Complication
Question
Answer
```

The writing should remain natural.

Do NOT force SCQA headings into every article.

------

# 12. GEO-Friendly Writing

Articles should be easy for both humans and AI systems to understand.

Prefer:

- Clear definitions
- Explicit statements
- Structured sections
- Concrete examples
- Technical details
- First-hand experience
- Specific conclusions

Avoid:

- Vague marketing language
- Keyword stuffing
- Artificial repetition
- Empty claims
- Excessive generic introductions

When describing a technical decision, clearly explain:

```text
What was the problem?
Why did I choose this approach?
What alternatives did I consider?
What happened after implementation?
```

First-hand experience is valuable.

------

# 13. Product References

Products should be mentioned naturally.

Do not turn articles into advertisements.

For example:

```text
I built IndexFlow to solve this problem for my own projects.
```

is preferable to repeatedly writing:

```text
Try IndexFlow now.
IndexFlow is the best SEO tool.
Use IndexFlow today.
IndexFlow is amazing.
```

A normal article should generally contain only the product links that are genuinely useful to the reader.

------

# 14. Internal Links

Use internal links when they provide useful context.

Good examples:

```text
Related article
Project documentation
Product page
Previous article in the series
```

Do not add links purely to increase link density.

Internal links should help readers discover related content.

------

# 15. External Platform Distribution

The Hugo article is the canonical version.

After publication, the article may be adapted for:

```text
X
Medium
LinkedIn
Reddit
小红书
Dev.to
```

The external version should NOT simply copy the Hugo article.

Adapt:

- Length
- Opening
- Tone
- Structure
- Platform conventions
- Call to action

The canonical Hugo article should remain the source of truth.

------

# 16. Series Articles

When an article belongs to a series:

- Keep a consistent naming convention.
- Link to previous and next articles when appropriate.
- Use the same relevant product tag.
- Do not create a new category for the series.
- Consider using a dedicated series taxonomy only if the project already supports it.

Example:

```yaml
categories:
  - Engineering

tags:
  - IndexFlow
  - Rust
  - Open Source
```

A series is NOT a category.

------

# 17. Multilingual Content

The website supports:

```text
English
中文
```

When an article has both English and Chinese versions:

- Keep the two versions connected through Hugo's multilingual translation mechanism.
- Keep the meaning consistent.
- Do NOT mechanically translate sentence by sentence when natural rewriting is better.
- Preserve technical terminology.
- Preserve product names.

Product names should remain:

```text
IndexFlow
MandarinClips
AgentBridge
```

Do not translate product names.

------

# 18. Images

Images should be used when they improve understanding or presentation.

Useful image types include:

- Product screenshots
- Architecture diagrams
- Workflow diagrams
- Charts
- UI screenshots
- Relevant illustrations

Do not add decorative images merely to increase image count.

When an image is required, ensure the image path works correctly with Hugo.

------

# 19. SEO Rules

Every article should have:

- Unique title
- Useful description
- Stable URL
- Correct canonical URL
- Correct language metadata
- Correct translation relationship when multilingual
- Appropriate internal links
- Appropriate tags

Do NOT keyword-stuff the article.

The primary goal is useful content.

------

# 20. Publishing Checklist

Before publishing an article, verify:

```text
[ ] Correct category
[ ] Existing category used
[ ] Relevant product tag
[ ] Relevant technology tags
[ ] No unnecessary tags
[ ] Title is clear
[ ] Description is useful
[ ] URL is stable
[ ] Article has a clear structure
[ ] Internal links are useful
[ ] Product links are natural
[ ] English/Chinese translation relationship is correct when applicable
[ ] Images work
[ ] Hugo builds successfully
```

Run:

```bash
hugo --minify
```

The article should not be considered ready if the Hugo build fails.

------

# 21. AI Content Generation Rules

When an AI generates an article for this project:

1. Read this Skill first.
2. Inspect existing articles when necessary.
3. Reuse existing categories.
4. Reuse existing tags whenever possible.
5. Never invent a new top-level category without explicit approval.
6. Never rename existing product tags.
7. Use `IndexFlow` as the IndexFlow product tag.
8. Avoid keyword stuffing.
9. Write for humans first.
10. Prefer first-hand experience and concrete information.
11. Follow the existing Hugo structure.
12. Do not modify unrelated files.
13. Run Hugo validation after structural changes.

------

# 22. Current Taxonomy Reference

## Categories

```text
Products
Engineering
Growth
Thoughts
Open Source
```

## Products

```text
IndexFlow
MandarinClips
AgentBridge
```

## Common Technology Tags

```text
Rust
Go
Hugo
MCP
TypeScript
JavaScript
Next.js
Cloudflare
Docker
Kubernetes
PostgreSQL
SQLite
```

## Common Topic Tags

```text
AI
SEO
GEO
Open Source
Indie Hacker
Build in Public
Content Marketing
Search Indexing
Developer Tools
```

This list is a reference, not a requirement to use every tag.

The taxonomy should grow slowly and intentionally.