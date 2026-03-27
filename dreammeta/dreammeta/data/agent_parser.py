"""Markdown parser for M##-*.md agent definition files."""

from __future__ import annotations

import re
from pathlib import Path

from dreammeta.constants import AGENT_REGISTRY, SECTION_MAP
from dreammeta.data.models import Agent, AgentSection, EvolutionMechanism

# Regex for legacy title format:
#   # M06 评估元 (Evaluate Meta)
#   # M13 创造元 (Create Meta) — 创
_TITLE_RE = re.compile(
    r"^#\s+(M\d{2})\s+(.+?)\s+\((.+?)\)(?:\s*[—–\-]+\s*(.+))?$"
)

# Regex for new title format:
#   # M01-memory
#   # M09-compose
_TITLE_RE_NEW = re.compile(r"^#\s+(M\d{2})-(\S+)\s*$")

# Regex for section headings: ## Core Function / 核心功能
_SECTION_RE = re.compile(r"^##\s+(.+)$")


def parse_agent_file(path: Path) -> Agent:
    """Parse a single agent markdown file into an Agent model."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    # --- Parse title ---
    agent_id = ""
    name_cn = ""
    name_en = ""
    operation = None

    for line in lines:
        stripped = line.strip()
        # Try legacy format first
        m = _TITLE_RE.match(stripped)
        if m:
            agent_id = m.group(1)
            name_cn = m.group(2).strip()
            name_en = m.group(3).strip()
            if m.group(4):
                operation = m.group(4).strip()
            break
        # Try new format: # M01-memory
        m2 = _TITLE_RE_NEW.match(stripped)
        if m2:
            agent_id = m2.group(1)
            # Look up names from AGENT_REGISTRY
            reg = AGENT_REGISTRY.get(agent_id)
            if reg:
                name_cn = reg[0]
                name_en = reg[1]
                operation = reg[3]
            else:
                name_cn = m2.group(2)
                name_en = m2.group(2)
            break

    # --- Split into sections by ## headings ---
    sections_raw: list[tuple[str, list[str]]] = []
    current_heading: str | None = None
    current_lines: list[str] = []

    for line in lines:
        sm = _SECTION_RE.match(line.strip())
        if sm:
            if current_heading is not None:
                sections_raw.append((current_heading, current_lines))
            current_heading = sm.group(1).strip()
            current_lines = []
        elif current_heading is not None:
            current_lines.append(line)

    if current_heading is not None:
        sections_raw.append((current_heading, current_lines))

    # --- Build AgentSection dict ---
    sections: dict[str, AgentSection] = {}
    layer_text = ""
    evolution = EvolutionMechanism()

    for heading, body_lines in sections_raw:
        content = "\n".join(body_lines).strip()

        # Find canonical key
        key = _heading_to_key(heading)

        if key == "layer":
            layer_text = content
        elif key == "self_evolution":
            evolution = _parse_evolution(content)

        sections[key] = AgentSection(
            heading_cn=heading,
            key=key,
            content=content,
        )

    # --- Determine layer number ---
    layer = _detect_layer(layer_text)

    return Agent(
        id=agent_id,
        name_cn=name_cn,
        name_en=name_en,
        layer=layer,
        layer_name=layer_text,
        operation=operation,
        sections=sections,
        evolution=evolution,
        source_path=path,
    )


def parse_all_agents(agents_dir: Path) -> list[Agent]:
    """Parse all M##-*.md files in a directory, sorted by ID."""
    files = sorted(agents_dir.glob("M[0-9][0-9]-*.md"))
    return [parse_agent_file(f) for f in files]


def _heading_to_key(heading: str) -> str:
    """Convert a section heading to its canonical key.

    Handles bilingual headings like 'Core Function / 核心功能' by checking
    if any SECTION_MAP keyword appears in the heading text.
    """
    for keyword, key in SECTION_MAP.items():
        if keyword in heading:
            return key
    # Fallback: use the heading itself as key
    return heading


def _detect_layer(layer_text: str) -> int:
    """Detect layer number from the layer section text."""
    if "第一层" in layer_text or "Foundation" in layer_text or "基础" in layer_text:
        return 1
    if "第二层" in layer_text or "Orchestration" in layer_text or "编排" in layer_text:
        return 2
    if "第三层" in layer_text or "Execution" in layer_text or "执行" in layer_text:
        return 3
    return 0


def _parse_evolution(content: str) -> EvolutionMechanism:
    """Parse the self-evolution mechanism section.

    Supports both legacy code-block format and new prose format.
    """
    # Try to extract content inside ``` fences (legacy format)
    code_match = re.search(r"```\n?(.*?)```", content, re.DOTALL)
    raw = code_match.group(1).strip() if code_match else content

    trigger = ""
    data_sources = ""
    actions = ""
    log_target = ""

    # Best-effort extraction of structured fields (legacy format)
    for line in raw.splitlines():
        line_s = line.strip()
        if line_s.startswith("触发条件："):
            trigger = line_s[len("触发条件："):]
        elif line_s.startswith("数据源："):
            data_sources = line_s[len("数据源："):]
        elif line_s.startswith("记录："):
            log_target = line_s[len("记录："):]
        elif line_s.startswith("进化动作："):
            actions = line_s[len("进化动作："):]

    # Re-extract actions block (multi-line, legacy format)
    actions_match = re.search(
        r"进化动作：\n?(.*?)(?=记录：|$)", raw, re.DOTALL
    )
    if actions_match:
        actions = actions_match.group(1).strip()

    return EvolutionMechanism(
        trigger=trigger,
        data_sources=data_sources,
        actions=actions,
        log_target=log_target,
        raw=raw,
    )
