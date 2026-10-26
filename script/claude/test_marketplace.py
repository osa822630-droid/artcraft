#!/usr/bin/env python3
"""Lightweight checks for the ArtCraft Claude marketplace and Free skill ZIPs."""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from zipfile import ZipFile


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
MARKETPLACE_PATH = REPOSITORY_ROOT / ".claude-plugin" / "marketplace.json"
PLUGIN_ROOT = REPOSITORY_ROOT / "plugins" / "artcraft-creative-studio"
PLUGIN_MANIFEST_PATH = PLUGIN_ROOT / ".claude-plugin" / "plugin.json"
SKILLS_ROOT = PLUGIN_ROOT / "skills"
PACKAGER_PATH = REPOSITORY_ROOT / "script" / "claude" / "package_free_skills.py"


class MarketplaceTests(unittest.TestCase):
    def test_marketplace_points_to_a_valid_plugin(self) -> None:
        marketplace = json.loads(MARKETPLACE_PATH.read_text(encoding="utf-8"))
        plugin_manifest = json.loads(PLUGIN_MANIFEST_PATH.read_text(encoding="utf-8"))

        self.assertTrue(marketplace["name"])
        self.assertTrue(marketplace["owner"]["name"])
        self.assertGreaterEqual(len(marketplace["plugins"]), 1)

        entry = marketplace["plugins"][0]
        source_path = (REPOSITORY_ROOT / entry["source"]).resolve()
        self.assertEqual(source_path, PLUGIN_ROOT.resolve())
        self.assertEqual(entry["name"], plugin_manifest["name"])
        self.assertTrue((source_path / "README.md").is_file())

    def test_skill_metadata_matches_each_directory(self) -> None:
        skill_dirs = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())
        self.assertGreaterEqual(len(skill_dirs), 1)

        for skill_dir in skill_dirs:
            skill_file = skill_dir / "SKILL.md"
            self.assertTrue(skill_file.is_file())
            text = skill_file.read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"), skill_file)
            match = re.search(r"^name: ([a-z0-9-]+)$", text, re.MULTILINE)
            self.assertIsNotNone(match, skill_file)
            self.assertEqual(match.group(1), skill_dir.name, skill_file)
            self.assertRegex(
                text,
                re.compile(r"^description: .+\S$", re.MULTILINE),
                skill_file,
            )

    def test_free_skill_archives_have_the_expected_root_folder(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            subprocess.run(
                [
                    sys.executable,
                    str(PACKAGER_PATH),
                    "--output-dir",
                    temporary_directory,
                ],
                check=True,
                cwd=REPOSITORY_ROOT,
                capture_output=True,
                text=True,
            )

            archives = sorted(Path(temporary_directory).glob("*.zip"))
            skill_dirs = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())
            self.assertEqual(len(archives), len(skill_dirs))

            for skill_dir in skill_dirs:
                archive_path = Path(temporary_directory) / f"{skill_dir.name}.zip"
                with ZipFile(archive_path) as archive:
                    self.assertIsNone(archive.testzip())
                    expected_names = sorted(
                        f"{skill_dir.name}/{file_path.relative_to(skill_dir).as_posix()}"
                        for file_path in skill_dir.rglob("*")
                        if file_path.is_file()
                    )
                    self.assertEqual(sorted(archive.namelist()), expected_names)
                    self.assertIn(f"{skill_dir.name}/SKILL.md", expected_names)


if __name__ == "__main__":
    unittest.main()
