---
name: artcraft-image-prompting
description: Draft or refine ArtCraft-ready prompts for text-to-image, reference-based image generation, image editing, compositing, and masked inpainting. Use when planning or revising a still image in ArtCraft.
---

# ArtCraft image prompting

Turn the user's visual intent into a focused prompt they can paste into an appropriate still-image workflow in ArtCraft. This skill writes prompts and workflow notes; it does not run ArtCraft or generate the image.

## Workflow

1. Identify the task: create a new image, edit a supplied image, compose layers, or change a masked region. If the user has not supplied an image needed for an edit, ask for it; otherwise do not block on optional details.
2. Preserve the user's stated subject, identity, style, framing, and must-keep details. If a reference is attached, use it as the source of truth for details the user wants preserved. Never claim exact identity or pixel-perfect preservation is guaranteed.
3. Make the prompt concrete and internally consistent. Prioritize the main subject and action, composition and camera viewpoint, environment, lighting, materials or visual style, then any important constraints. Avoid adjective piles and contradictory instructions.
4. For editing, state what should change and what should remain unchanged. Keep the edit scoped to the requested area. For canvas masks or inpainting, describe the contents of the masked area and how its edges, lighting, perspective, and shadows should blend with the unmasked image.
5. If exact lettering matters, quote the text exactly and mention placement; warn briefly that image models may misspell it and suggest adding final typography in a design tool.
6. Do not invent model names, aspect-ratio options, negative-prompt fields, or other controls. ArtCraft's available models and controls can change; tell the user to choose a currently available model that supports the requested workflow in the app.

## Response format

Use the user's language for explanations and for the prompt unless they request another language. Keep the answer concise:

- **Workflow:** the relevant ArtCraft workflow, stated at a high level.
- **Prompt:** one polished, paste-ready prompt in a fenced text block.
- **Setup notes:** only the useful notes, such as which supplied image to use as a reference or which area to mask. Do not list controls you cannot verify.

If the request is already specific, provide the prompt directly. Ask at most one short question when a missing decision would materially change the image; otherwise make and label a reasonable assumption.
