---
name: artcraft-scene-planning
description: Plan ArtCraft 2D or 3D compositions, locations, camera framing, character poses, props, image-to-3D assets, and multi-shot continuity. Use when blocking or designing a scene before generation.
---

# ArtCraft scene planning

Help the user make a visual scene controllable before they generate it in ArtCraft. ArtCraft supports workflows such as 2D and 3D compositing, image-to-location, character posing, image-to-3D mesh, background removal, and mixed-asset scenes. Translate the goal into a practical plan; do not claim to operate the app or guarantee a model result.

## Build a useful plan

1. Clarify the deliverable: a single image, a reusable location, a 3D mesh, a set of shots, or a staged composite. If the user already specified it, proceed.
2. Describe the scene in spatial terms: foreground, middle distance, background; left/right placement; relative scale; contact with the ground; and clear separation between subject and props.
3. Specify the camera in visual terms: shot size, height, angle, direction, and perspective. Keep camera placement consistent across shots when continuity matters.
4. Add only relevant art direction: lighting direction and quality, palette, materials, atmosphere, and depth cues. Avoid conflicting or over-detailed requirements.
5. For characters, list the identity and costume traits that must stay fixed, then describe pose, expression, and gaze separately. For pose or identity transfer, state which reference provides identity and which provides pose; do not imply the transfer is exact.
6. For image-to-3D or mesh briefs, emphasize silhouette, proportions, key geometry, material, and details that must survive from the reference. Do not invent topology, export, or model controls.
7. For a reusable location or world, specify a coherent layout, landmarks, paths or sightlines, lighting, and viewpoints. For a multi-shot sequence, give each shot its own framing and action while repeating only the continuity invariants.
8. Break a complex result into ArtCraft-sized steps when that gives the user more control—for example, establish the location, place or pose the subject, block the camera, then generate or composite the final image. Describe this as a suggested workflow, not as exact UI instructions.

## Response format

Use the user's language. Provide only the sections that fit:

- **Scene brief:** the intended final image or asset.
- **Layout:** foreground / subject / background with relative positions.
- **Camera and lighting:** concise, actionable direction.
- **Continuity locks:** identity, wardrobe, location, or other details to preserve.
- **ArtCraft prompts:** separate paste-ready prompts for distinct assets or shots, if requested.
- **Suggested workflow:** a short sequence of high-level steps; remind the user that exact controls depend on the current app and chosen model.

Do not force a long template onto a simple request. Ask at most one clarifying question if the subject, deliverable, or reference roles are genuinely ambiguous; otherwise make a reasonable, explicit assumption.
