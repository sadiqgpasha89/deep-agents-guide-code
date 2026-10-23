---
name: blog-post
description: Write a long-form blog post with research, a hero image and a quality checklist. Use when the user asks for a blog article.
metadata:
  include_tools: "web_search generate_cover"   # space-separated string, NOT a YAML list
---

# Blog post workflow
1. Delegate research to the `researcher` subagent.
2. Read the findings, then write `blogs/<slug>/post.md`.
3. Generate a cover image into the same folder.
4. Run the quality checklist in `references/checklist.md`.
