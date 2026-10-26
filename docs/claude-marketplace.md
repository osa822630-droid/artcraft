# Claude web marketplace for ArtCraft

This package is for **Claude on the web at claude.ai**, not a Claude Code-only extension. It adds a GitHub-hosted ArtCraft plugin marketplace to this repository. Claude Free users can add it through the same **Add marketplace** flow.

## What the plugin does

**ArtCraft Creative Studio** gives Claude three focused skills for:

- Writing or refining still-image prompts for new images, reference-based edits, compositing, and inpainting.
- Structuring image-to-video prompts around a clear action, camera movement, and continuity.
- Planning 2D/3D compositions, locations, character poses, props, meshes, and multi-shot scenes.

The plugin is a prompt-writing and planning aid. It does not control the ArtCraft desktop app, generate media, or connect to an ArtCraft account. It contains no MCP server, executable scripts, hooks, or API keys. Copy the prompt or scene plan into the relevant workflow in ArtCraft; the app's model picker determines which models and controls are currently available.

## Add the marketplace to Claude web (including Free)

Once these changes are present on the repository's default branch:

1. Open **Customize > Plugins** in Claude at [claude.ai](https://claude.ai/).
2. Select **Add > Add marketplace > Add from a repository**.
3. Enter the public GitHub repository that contains this marketplace, for example `osa822630-droid/artcraft` (or its full URL, `https://github.com/osa822630-droid/artcraft`).
4. Find **ArtCraft Creative Studio** in the marketplace and select **Add**.

The repository must be public and the marketplace files must be on its default branch for Claude to fetch them by repository. This repository's marketplace manifest is `.claude-plugin/marketplace.json`.

## Optional: upload an individual skill

If you want only one skill instead of adding the whole marketplace, the skill folders can also be uploaded individually in Claude. This route does not require Claude Code:

1. Enable **Code execution and file creation** (also labeled **Create and edit files**) under **Settings > Capabilities**.
2. From the repository root, run:

   ```bash
   python3 script/claude/package_free_skills.py
   ```

3. The script creates one ZIP per skill under `target/claude-free-skills/`. Upload any or all of them from **Customize > Skills > + > Create skill > Upload a skill**, then turn the skill on.

Each ZIP contains the skill folder at its root, as required for a Claude custom skill. The ZIPs are build outputs and are not checked into the repository. If you do not use Python, download the repository, then ZIP an individual folder inside `plugins/artcraft-creative-studio/skills/` so the ZIP contains that folder and its `SKILL.md`.

## Check the package

Run the standard-library tests from the repository root:

```bash
python3 script/claude/test_marketplace.py
```

The tests check the marketplace-to-plugin path, the skill frontmatter and folder names, and the ZIP layout used by the Claude Free upload route.

## Claude format references

- [Plugin structure and testing](https://claude.com/docs/plugins/build)
- [Create custom skills](https://claude.com/docs/skills/how-to)
