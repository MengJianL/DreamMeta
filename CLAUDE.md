# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Meta_Creates is a **Meta-Department (元部门) architecture framework** — a 13-atom organizational system for autonomous agent coordination and governance. It implements the "Organizational Mirroring" theory from the reference paper (`Knowledge/LaoJin_paper.pdf`), providing a pure-abstract, domain-agnostic, self-evolving agent infrastructure.

This is not a traditional software project with build/test commands. It is a **configuration-as-architecture** system where `.md` files define agent behaviors, and the structure itself is the product.

## Architecture: Three-Layer Gravity Structure

```
Layer 3 (Execution)  : M09-compose  M10-retrieve  M11-invoke  M12-verify  M13-create
Layer 2 (Orchestration): M04-decompose  M05-route  M06-evaluate  M07-synthesize  M08-sequence
Layer 1 (Foundation) : M01-memory  M02-identity  M03-channel
```

- **Foundation** provides storage, identity, and communication infrastructure
- **Orchestration** coordinates, routes, evaluates, and sequences
- **Execution** performs atomic operations: compose, retrieve, invoke, verify, create

Detailed architecture index: `.claude/agents/CLAUDE.md`

## Key Conventions

- **Agent file naming**: `M##-[name].md` (e.g., `M04-decompose.md`)
- **Agent file structure**: each file follows a 16-section template — Layer → Identity → Existential Role → Core Function → Operational Boundary → Trigger Conditions → Working Modes → Input Contract → Output Contract → Decision Principles → Failure Modes → Quality Criteria → Neighbor Interaction → Runtime Binding → Self-Evolution → Minimal Governance Statement. Some atoms include optional Special Protocols (e.g., Escalation Ladder in M08, Human Channel Protocol in M03, Capability Gap Protocol in M05).
- **Quality scale**: 0–5 per dimension (Accuracy, Completeness, Actionability, Format), 16/20 passing threshold
- **Language**: bilingual Chinese/English documentation
- **All descriptions are pure-abstract** — no domain-specific vocabulary, to ensure cross-domain reusability

## Commands

| Command | Purpose |
|---|---|
| `/meta <task>` | 元部门构建 Agent 团队执行任务：分析→设计团队→派遣执行→独立核验→独立评估→综合交付 |

Defined in `.claude/commands/meta.md`.

## DreamMeta (梦元) Desktop App

`dreammeta/` contains a PySide6 desktop GUI for visualizing and managing the 13-atom architecture. See `dreammeta/CLAUDE.md` for detailed architecture.

```bash
cd dreammeta && pip install -e .
dreammeta                # or: python -m dreammeta
pytest tests/            # run tests
```

## Skill Integration

| External Skill | Integrated Into | Purpose |
|---|---|---|
| `find-skill` | M05 (Route) + M10 (Retrieve) | Discover reusable patterns when capability gaps detected |
| `skill-create` | M13 (Create) | Package validated new patterns into reusable skill modules |

## Runtime Binding: Claude Code Environment

**Core principle: the Meta-Department is an orchestrator, not an executor. It builds Agent teams to do work.**

When operating within Claude Code CLI, abstract atom operations bind to concrete tools:

| Atom Concept | Claude Code Implementation |
|---|---|
| M04 标准/重量模式执行 | **Must** use `Agent` tool to create independent sub-task executors |
| M05 路由至执行实体 | **Must** form real execution ownership via `Agent` instances |
| M06 独立评估 | **Must** use a separate `Agent` instance, NO shared context with executor. No exceptions. |
| M07 综合 (>3 sources) | **Must** delegate to independent `Agent` for context isolation |
| M08 并行执行 | Spawn multiple `Agent` tool calls in a single message (max 5 per batch) |
| M09 非微型生成 | **Must** use independent `Agent` for all non-trivial composition tasks |
| M10 跨源检索 (≥2 sources) | **Must** delegate to independent `Agent` for cross-source retrieval |
| M11 非微型调用 | **Must** use independent `Agent` for external system/API invocations |
| M12 独立核验 | Verifier **must never** share execution context with producer (regardless of how production happened) |
| M13 所有级别创造 | Skill-level **must** use independent `Agent`; Agent/Meta-Dept level **must** use multi-Agent collaboration |

**Single-entity execution is only permitted for "micro" tasks** (single clear operation, ≤1 file, ≤10 lines changed, no verification needed). Any doubt → upgrade to standard mode with Agent team.

**Parallelism cap**: Max 5 concurrent Agent instances per batch. If > 5 parallel tasks exist, split into batches with convergence checkpoints between them.

## Cross-Project Reuse

When starting a new project, copy `.claude/agents/` (the 13 atoms + index). Do **not** copy `.claude/memory/` — each project accumulates its own memory to maintain isolation (M01 principle).

## Reference Materials

- `Knowledge/LaoJin_paper.pdf` — source paper defining 8 architectural principles and 10-phase workflow
- `Knowledge/2.png` — three-layer gravity structure visual
- `Knowledge/1.png` — agent file structure reference
- `Renovation/` — design source documents for the 16-section template rewrite (术语表, 总览图表, 模板, M01-M13 specifications)
