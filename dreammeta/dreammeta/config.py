"""Configuration manager — global settings ARE the Meta-Department itself."""

from __future__ import annotations

import json
from pathlib import Path


class DreamMetaConfig:
    """Resolves paths relative to the dreammeta package location.

    The global settings are the 13 atom definitions stored in
    Meta_Creates/.claude/agents/. No user-home-directory configuration
    is used.
    """

    def __init__(self, app_root: Path | None = None) -> None:
        # dreammeta/ (the outer package directory containing pyproject.toml)
        self.app_root = app_root or Path(__file__).parent.parent
        # Meta_Creates/
        self.meta_creates_root = self.app_root.parent
        # .claude/agents/
        self.agents_dir = self.meta_creates_root / ".claude" / "agents"
        # .claude/memory/
        self.memory_dir = self.meta_creates_root / ".claude" / "memory"
        # Project registry
        self.projects_file = self.app_root / "projects.json"
        # Collected materials staging
        self.collected_dir = self.app_root / "collected"
        # User settings (theme, fonts, API config)
        self.settings_file = self.app_root / "user_settings.json"

    def get_agent_files(self) -> list[Path]:
        """Return sorted list of M##-*.md files."""
        if not self.agents_dir.exists():
            return []
        return sorted(self.agents_dir.glob("M[0-9][0-9]-*.md"))

    def get_registered_projects(self) -> list[Path]:
        """Read projects.json for tracked project paths."""
        if not self.projects_file.exists():
            return []
        data = json.loads(self.projects_file.read_text(encoding="utf-8"))
        return [Path(p) for p in data.get("projects", [])]

    def register_project(self, project_path: Path) -> None:
        """Add a project path to the registry."""
        projects = self.get_registered_projects()
        if project_path not in projects:
            projects.append(project_path)
        data = {"projects": [str(p) for p in projects]}
        self.projects_file.write_text(
            json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
        )
