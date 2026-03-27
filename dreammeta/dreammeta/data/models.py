"""Pydantic data models for Meta-Department entities."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from pydantic import BaseModel, Field


class AgentSection(BaseModel):
    """A single section within an agent definition file."""

    heading_cn: str  # Original Chinese heading, e.g. "核心职能"
    key: str  # Canonical English key, e.g. "core_functions"
    content: str  # Raw markdown content of the section


class EvolutionMechanism(BaseModel):
    """Parsed self-evolution mechanism from an agent file."""

    trigger: str = ""
    data_sources: str = ""
    actions: str = ""
    log_target: str = ""
    raw: str = ""  # Full raw text of the code block


class Agent(BaseModel):
    """A parsed Meta-Department atom agent."""

    id: str  # "M01" through "M13"
    name_cn: str  # "记忆元"
    name_en: str  # "Memory Meta"
    layer: int  # 1, 2, or 3
    layer_name: str  # "基础设施元（第一层）"
    operation: str | None = None  # "写"/"查"/"用"/"检"/"创" (Layer 3 only)
    sections: dict[str, AgentSection] = Field(default_factory=dict)
    evolution: EvolutionMechanism = Field(default_factory=EvolutionMechanism)
    source_path: Path | None = None

    @property
    def display_name(self) -> str:
        """Short display name like 'M06 评估'."""
        # Strip '元' suffix for compact display
        short = self.name_cn.replace("元", "")
        return f"{self.id} {short}"

    @property
    def full_title(self) -> str:
        """Full title like 'M06 评估元 (Evaluate Meta)'."""
        return f"{self.id} {self.name_cn} ({self.name_en})"


class MemoryEntry(BaseModel):
    """A single memory fact stored in a topic's items.json."""

    id: str
    fact: str
    timestamp: str
    status: str = "active"


class MemoryTopic(BaseModel):
    """A collection of memory entries under one topic."""

    name: str
    entries: list[MemoryEntry] = Field(default_factory=list)
    path: Path | None = None


class ProjectInfo(BaseModel):
    """Metadata about a project that uses Meta-Department architecture."""

    name: str
    root_path: Path
    agents_path: Path | None = None
    agent_count: int = 0  # out of 13
    missing_agents: list[str] = Field(default_factory=list)
    memory_path: Path | None = None
    topic_count: int = 0
    last_modified: datetime | None = None
    has_claude_md: bool = False
