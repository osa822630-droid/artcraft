---
name: artcraft-video-prompting
description: Create or refine prompts for ArtCraft image-to-video and video-shot workflows, with clear action, camera movement, timing, and continuity. Use when a user wants to plan or animate a clip in ArtCraft.
---

# ArtCraft video prompting

Turn the user's idea or supplied starting image into a short, temporally coherent prompt for an appropriate video workflow in ArtCraft. This skill drafts instructions only; it does not run ArtCraft or generate a clip.

## Prompting principles

- Establish the opening frame, the main subject and one readable action, then the progression of motion and the ending state. Keep a short clip focused on one main beat rather than a list of unrelated events.
- Describe subject motion and camera motion separately. Keep them compatible: for example, do not request both a locked-off camera and a continuous orbit.
- Include only the details that help the shot: framing, direction and pace of movement, environment, lighting, and motion feel. Use specific physical verbs rather than vague instructions such as “make it dynamic.”
- For image-to-video, treat the supplied image as the visual anchor. Preserve its subject identity, composition, wardrobe, and setting unless the user asks to change them. Describe what should move and what should stay still.
- If the user wants continuity across shots, call out invariant character, costume, location, lighting, and screen direction. Do not promise that a generative model will preserve them exactly.
- Do not assume a particular model supports text-to-video, audio, a duration, frame rate, camera controls, or start/end-frame inputs. These vary by model; ask the user to check the selected model's controls in ArtCraft.

## Response format

Use the user's language unless they ask for another. Return:

- **Workflow:** image-to-video or another high-level workflow, based on the request.
- **Prompt:** one paste-ready prompt in a fenced text block, ordered from opening state through action to ending state.
- **Reference / setup:** a brief note identifying an attached starting image or any model-specific setting the user should verify.

If the request leaves out a choice that would materially change the clip, ask one concise question. Otherwise state your assumption and draft the prompt without unnecessary back-and-forth.
