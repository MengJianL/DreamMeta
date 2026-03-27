"""Project scanner — discovers and introspects Meta-Department projects."""

from __future__ import annotations

import shutil
from datetime import datetime
from pathlib import Path

from dreammeta.constants import AGENT_REGISTRY
from dreammeta.data.models import ProjectInfo


def scan_project(root_path: Path) -> ProjectInfo:
    """Introspect a single project directory for Meta-Department usage."""
    agents_path = root_path / ".claude" / "agents"
    memory_path = root_path / ".claude" / "memory"

    # Count agents
    all_ids = set(AGENT_REGISTRY.keys())
    found_ids: set[str] = set()
    last_mod: datetime | None = None

    if agents_path.exists():
        for f in agents_path.glob("M[0-9][0-9]-*.md"):
            agent_id = f.name[:3]  # "M01", "M02", etc.
            found_ids.add(agent_id)
            mtime = datetime.fromtimestamp(f.stat().st_mtime)
            if last_mod is None or mtime > last_mod:
                last_mod = mtime

    missing = sorted(all_ids - found_ids)

    # Count memory topics
    topic_count = 0
    topics_dir = memory_path / "areas" / "topics"
    if topics_dir.exists():
        topic_count = sum(1 for d in topics_dir.iterdir() if d.is_dir())

    return ProjectInfo(
        name=root_path.name,
        root_path=root_path,
        agents_path=agents_path if agents_path.exists() else None,
        agent_count=len(found_ids),
        missing_agents=missing,
        memory_path=memory_path if memory_path.exists() else None,
        topic_count=topic_count,
        last_modified=last_mod,
        has_claude_md=(root_path / "CLAUDE.md").exists(),
    )


def init_project(
    source_agents_dir: Path,
    target_root: Path,
) -> ProjectInfo:
    """Initialize a new project by copying agents (not memory).

    Copies .claude/agents/ from source to target. Creates an empty
    .claude/memory/ structure. Does NOT copy existing memory.
    """
    target_agents = target_root / ".claude" / "agents"
    target_memory = target_root / ".claude" / "memory" / "areas" / "topics"

    # Copy agents directory (backup existing if present)
    if target_agents.exists():
        backup = target_agents.with_name("agents_backup")
        if backup.exists():
            shutil.rmtree(backup)
        target_agents.rename(backup)
    shutil.copytree(source_agents_dir, target_agents)

    # Create empty memory structure
    target_memory.mkdir(parents=True, exist_ok=True)

    return scan_project(target_root)
