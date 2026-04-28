# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

DreamMeta is a **Meta-Department (元部门) architecture framework** — a 13-atom organizational system for autonomous agent coordination and governance. It implements the "Organizational Mirroring" theory from the reference paper (`references/base/LaoJin_paper.pdf`), providing a pure-abstract, domain-agnostic, self-evolving agent infrastructure.

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

Detailed architecture index (五类关系网络, 五条核心链路, 两条治理闭环, Agent 团队运转模型, 项目 Agent 体系, Claude Code 运行绑定, Skill 融合映射, Agent 创建机制, 设计原则, 统一术语约束): **`.claude/agents/CLAUDE.md`**

## Commands

| Command | Purpose |
|---|---|
| `/meta <task>` | 元部门为项目创造 Agent：意图放大→分析→检查/创造项目 Agent→按 Agent 定义执行→核验→评估→交付 |

Defined in `.claude/commands/meta.md`.

## Critical Rules (Runtime Binding)

**Core principle: the Meta-Department is a "tool that creates tools" (创造工具的工具). Its primary output is Project Agent definitions (stored in `agents/`), not work deliverables.**

1. **三权分立** — Execution Agent, Verify Agent (M12), and Evaluate Agent (M06) must be separate `Agent` instances with fully isolated context. No exceptions.
2. **Agent delegation is mandatory** — All non-micro tasks must use independent `Agent` tool instances. Micro requires ALL THREE: (1) single clear operation, no decomposition needed; (2) ≤1 file, ≤10 lines; (3) no verification needed. Any doubt → upgrade to standard mode.
3. **Reuse before create** — M05 must check project `agents/` for existing Agent definitions before creating new ones. If no match found, search global resources (`.claude/skills/`, `.claude/agents/`, `references/` SKILL.md files) for directly invokable Skills/Agents before creating new project Agents.
4. **Parallelism** — Independent sub-tasks must be dispatched in parallel (max 5 Agent instances per batch). > 5 → split into batches with convergence checkpoints.
5. **先读后派** — Before dispatching Agents, read `.claude/agents/CLAUDE.md` (architecture index) and the relevant atom definitions.
6. **Phase gate-checks** — `/meta` enforces hard gate-checks between phases. Standard/heavy tasks are forbidden from entering Phase C (execution) without first completing Phase B (creating/reusing project Agent definitions in `agents/`). See `meta.md` for the full ⛔ gate-check system.

Full runtime binding table: `.claude/agents/CLAUDE.md` § 八
M13 five-level creation system (L0 Project Agent → L4 Governance-Aware Replication): `.claude/agents/CLAUDE.md` § 十

## Atom File Conventions

- **Naming**: `M##-[name].md` (e.g., `M04-decompose.md`)
- **15-section template** (do not remove or reorder sections): Layer → Identity (includes Existential Role) → Core Function → Operational Boundary → Trigger Conditions → Working Modes → Input Contract → Output Contract → Decision Principles → Failure Modes → Quality Criteria → Neighbor Interaction → Runtime Binding → Self-Evolution → Minimal Governance Statement
- Optional Special Protocols: Escalation Ladder (M08), Human Channel Protocol (M03), Capability Gap Protocol (M05), and domain-specific protocols per atom
- **Quality scale**: 0–5 per dimension (Accuracy, Completeness, Actionability, Format), 16/20 passing threshold
- **Language**: bilingual Chinese/English
- **Pure-abstract** — no domain-specific vocabulary, to ensure cross-domain reusability

## Project Agent System

The Meta-Department produces **Project Agent definitions** — standardized `.md` files stored in the project's `agents/` directory. Each Agent is **triple-armed** (Prompt + Skill + Tools) with a **9-section template**: 身份定位 → 原子映射 → 输入契约 → 输出契约 → 执行规程 → 行为约束 → 质量标准 → 技能装备 → 工具优先级. Skill bindings and Tool priorities are auto-matched from atom affinity tables in `.claude/agents/CLAUDE.md` § 九.

| Concept | 13 Atoms | Project Agents |
|---------|----------|---------------|
| **Nature** | Abstract role templates | Project-specific execution tools |
| **Location** | `.claude/agents/M##-xxx.md` | `agents/[Name]-Agent.md` |
| **Created by** | Architecture designer (human) | Meta-Department (automatic) |
| **Reuse scope** | Cross-project universal | Within-project reuse |

The `agents/` directory is created on first `/meta` invocation and accumulates project-specific Agent definitions over time.

## Cross-Project Reuse

Copy `.claude/agents/` (13 atoms + index) to bootstrap a new project. Do **not** copy `agents/` (project-specific) or `.claude/memory/` — each project accumulates its own.

## Skill Integration

**Global resource discovery**: When M05 finds no matching project Agent in `agents/`, it searches global resources before creating new Agents. Matching global Skills/Agents are invoked directly (via Skill tool or M11-invoke), not wrapped in project Agent definitions.

| External Skill | Integrated Into | Purpose |
|---|---|---|
| `find-skills` | M05 + M10 | Discover reusable patterns when capability gaps detected |
| `writing-skills` | M13 | Package validated new patterns into reusable skill modules |
| `awesome-claude-prompts` | M09 + M02 + M10 | Prompt frameworks, identity methodology, template library |
| Global `.claude/skills/` | M05 route | 14 superpowers skills, searched on capability gap |
| Global `.claude/agents/` | M05 route | Global agents (e.g. code-reviewer), searched on capability gap |
| `references/*/SKILL.md` | M05 route | Reference skill files, searched on capability gap |

## Reference Materials

- `references/base/LaoJin_paper.pdf` — source paper (8 architectural principles, 10-phase workflow)
- `references/base/2.png` — three-layer gravity structure visual
- `references/base/1.png` — agent file structure reference
- `references/` — also contains `agent-teams-playbook/`, `awesome-claude-prompts/`, `superpowers/`, `Vibe-Skills-v20260411/` reference skills
- `references/Vibe-Skills-v20260411/` — governed runtime framework (selective snapshot): 7 transferable patterns (closure-first, anti-drift, delegation envelope, execution grading, evidence-based communication, skill contract schema, 6-stage state machine). See `DREAMMETA-STUDY.md` for mapping to DreamMeta atoms.
