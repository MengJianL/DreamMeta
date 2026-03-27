# CLAUDE.md — DreamMeta v0.4.0

This file provides guidance to Claude Code when working with `dreammeta/`.

## Overview

DreamMeta (梦元) is a PySide6 desktop GUI for visualizing and managing the Meta-Department 13-atom architecture. Pure local filesystem operations — no backend/API.

## Commands

```bash
cd dreammeta && pip install -e .
dreammeta                  # or: python -m dreammeta
pytest tests/              # smoke tests
```

## Pages (3 total)

| # | Page | Icon | Shortcut | Purpose |
|---|------|------|----------|---------|
| 1 | Atoms | ◈ | Ctrl+1 | 3-layer gravity graph, atom health indicators (⚠/✗/?), markdown detail panel, refresh, aggregate health summary, file watcher auto-refresh, "Open in Editor" |
| 2 | Projects | ▣ | Ctrl+2 | Project cards (agent count/13, missing agents, CLAUDE.md status, memory topic count), "Initialize New Project" with backup safety |
| 3 | Settings | ⚙ | Ctrl+3 | Theme preset selector (Obsidian/Catppuccin Mocha/Nord/Dracula), accent color hex input, font size spinner |

## File Structure

```
dreammeta/
├── __init__.py            # version via importlib.metadata
├── __main__.py            # entry point
├── app.py                 # QMainWindow, sidebar nav, 3 pages via QStackedWidget
├── config.py              # DreamMetaConfig (path resolution, projects.json)
├── constants.py           # AGENT_REGISTRY, LAYERS, LAYER_AGENTS, SECTION_MAP
├── theme.py               # ThemeManager, ThemeColors (27 fields), 4 presets, QSS generation
├── data/
│   ├── models.py          # Agent, AgentSection, EvolutionMechanism, ProjectInfo, MemoryEntry/Topic
│   ├── agent_parser.py    # parse M##-*.md → Agent models (regex on ## headings)
│   └── project_scanner.py # scan/init projects (copies agents, never memory; backup safety)
├── screens/
│   ├── dashboard.py       # Atoms page: 3-layer graph, health checks, detail panel, QFileSystemWatcher
│   ├── projects.py        # Projects page: cards, initialization
│   └── settings.py        # Settings page: preset, accent, font size
└── tests/
    └── test_smoke.py      # smoke tests
```

## Architecture

### Agent file format (v0.4.0 — 16-section template)

Agent files use the title format `# M##-name` (e.g., `# M01-memory`) with bilingual section headings (e.g., `## Core Function / 核心功能`).

The parser (`agent_parser.py`) supports both legacy format (`# M06 评估元 (Evaluate Meta)`) and new format. For new format titles, names are looked up from `AGENT_REGISTRY`.

### Section mapping

`SECTION_MAP` in `constants.py` maps heading keywords to canonical keys. It supports 16 standard sections plus legacy headings for backward compatibility:

- `identity`, `existential_role`, `core_functions`, `operational_boundary`
- `trigger_conditions`, `working_modes`, `input_contract`, `output_contract`
- `decision_principles`, `failure_modes`, `quality_criteria`, `neighbor_interaction`
- `runtime_binding`, `self_evolution`, `governance_statement`
- Legacy: `thinking_mode`, `behavior_constraints`, `output_spec`

### Health check (8-point)

Dashboard checks 8 key sections for each atom: identity, existential_role, core_functions, operational_boundary, decision_principles, failure_modes, runtime_binding, self_evolution. Score 8 = healthy, 6-7 = warning, <6 = error.

### Theme system

`ThemeColors` dataclass (27 color fields) → `ThemeManager.generate_stylesheet()` → single QSS string applied to entire app. 4 presets (Obsidian, Catppuccin Mocha, Nord, Dracula). Persisted as JSON.

### Data flow

`.md` files on disk → `agent_parser.parse_all_agents()` → `Agent` models → pages render as HTML.

`config.py` resolves all paths relative to `__file__`, never `~/.config/`. The 13 atom `.md` files in `../.claude/agents/` ARE the configuration.

### Project isolation

`init_project()` copies `.claude/agents/` but never `.claude/memory/` — each project accumulates its own memory (M01 principle).

## Conventions

- All data models in `data/models.py` (Pydantic)
- Static agent metadata in `constants.py:AGENT_REGISTRY` for fast lookup without parsing
- Pages are QWidget subclasses with `_build_ui()` constructor pattern
- Project registry: `dreammeta/projects.json`

## v0.4.0 Changes

- Adapted to 16-section atom template (was 6-section)
- M09 renamed from 生成元/Generate to 构成元/Compose
- Health check expanded from 5-point to 8-point
- Parser handles both old and new title formats
- Detail panel renders all 16 sections in template order
