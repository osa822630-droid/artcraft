#!/usr/bin/env python3
"""Package each ArtCraft skill as a ZIP that Free Claude can upload."""

from __future__ import annotations

import argparse
from pathlib import Path, PurePosixPath
from zipfile import ZIP_DEFLATED, ZipFile


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
SKILLS_ROOT = REPOSITORY_ROOT / "plugins" / "artcraft-creative-studio" / "skills"
DEFAULT_OUTPUT_DIR = REPOSITORY_ROOT / "target" / "claude-free-skills"


def package_skill(skill_dir: Path, output_dir: Path) -> Path:
    """Create a Claude Skills-compatible ZIP with the skill folder at its root."""
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        raise ValueError(f"Missing required skill file: {skill_file}")

    archive_path = output_dir / f"{skill_dir.name}.zip"
    with ZipFile(archive_path, "w", compression=ZIP_DEFLATED) as archive:
        for file_path in sorted(skill_dir.rglob("*")):
            if file_path.is_file():
                relative_path = file_path.relative_to(skill_dir)
                archive_name = PurePosixPath(skill_dir.name, *relative_path.parts)
                archive.write(file_path, archive_name.as_posix())

    return archive_path


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Build one uploadable ZIP per ArtCraft Claude skill."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for the ZIP files (default: target/claude-free-skills).",
    )
    args = parser.parse_args()

    output_dir = args.output_dir
    if not output_dir.is_absolute():
        output_dir = REPOSITORY_ROOT / output_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    skill_dirs = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())
    if not skill_dirs:
        raise SystemExit(f"No skill folders found under {SKILLS_ROOT}")

    for skill_dir in skill_dirs:
        archive_path = package_skill(skill_dir, output_dir)
        print(f"Created {archive_path}")


if __name__ == "__main__":
    main()
