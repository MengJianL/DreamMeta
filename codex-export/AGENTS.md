# DreamMeta for Codex

This file explains how to read and maintain the DreamMeta Meta-Department governance framework inside Codex.

> Source: DreamMeta Claude Code canonical at `.claude/` (this `codex-export/` folder is a mirror, not the editing home).

## Human Summary

If you only remember three things:

- DreamMeta is **one Meta-Department governance system** projected into Claude Code and Codex; this `codex-export/` folder is the Codex-facing mirror, not a separate product.
- The Meta-Department is **a "tool that creates tools" / 「创造工具的工具」** — its primary output is **project Agent definitions** (stored in the project's `agents/` folder), not work deliverables.
- Long-term edits belong in `.claude/agents/` and `.claude/commands/meta.md` (the canonical Claude Code source); Codex-facing files in this folder are mirrors that should be re-synced after canonical edits.

## Read This Repository Correctly

Do not interpret DreamMeta as "a folder of unrelated agent prompt files".

Interpret it as:

**one Meta-Department architecture composed of 13 atomic units organized into a three-layer gravity structure, projected into Claude Code (canonical) and Codex (mirror).**

DreamMeta 不是一组散落的 prompt — 它是一个由 13 个原子按三层引力结构组织而成的元部门治理体系，主源在 Claude Code，Codex 只是镜像运行时。

## What "Meta-Department" Means / 什么是元部门

In DreamMeta:

**Meta-Department (元部门) = an organizational system whose only job is to create tools (project Agent definitions) that solve project problems — not to solve project problems directly.**

A valid Meta-Department:

- consists of exactly **13 atomic units** (M01 through M13), no more, no less
- organizes them into a **three-layer gravity structure** (Foundation / Orchestration / Execution)
- separates execution, verification, and evaluation into different agent instances (**三权分立 / Separation of Powers**)
- creates project Agent definitions instead of producing work deliverables itself
- accumulates project-specific Agent definitions in a project's `agents/` folder

## Three-Layer Gravity Structure / 三层引力结构

```
Layer 3 (Execution / 执行层)    : M09-compose  M10-retrieve  M11-invoke  M12-verify  M13-create
Layer 2 (Orchestration / 编排层) : M04-decompose  M05-route  M06-evaluate  M07-synthesize  M08-sequence
Layer 1 (Foundation / 基础层)    : M01-memory  M02-identity  M03-channel
```

- **Foundation** provides storage, identity, and communication continuity
- **Orchestration** decomposes, routes, evaluates, sequences, and synthesizes
- **Execution** performs atomic operations through dispatched Agents (one Codex subagent invocation per atom role)

## "Tool That Creates Tools" Philosophy / 「创造工具的工具」哲学

The single most important rule in DreamMeta:

```
Meta-Department core output  =  project Agent definitions  (in `agents/`)
Meta-Department core output  ≠  work deliverables
```

When Codex receives a task via the meta-orchestration skill:

1. analyze the task (Phase A)
2. **create or reuse a project Agent definition** in the project's `agents/` folder (Phase B)
3. dispatch a Codex subagent invocation that runs **according to that project Agent definition** (Phase C)
4. verify, evaluate, deliver, evolve (Phase D)

The Meta-Department itself never produces the final work deliverable — it always produces the Agent that will produce the deliverable.

## What Codex Is Looking At / Codex 看到什么

When this `codex-export/` folder is loaded into Codex:

- `AGENTS.md` is the project guide you are reading now
- `README.md` is the deployment / migration guide for human operators
- `.codex/skills/meta-orchestration/SKILL.md` is the Codex skill that invokes the 13-atom governance chain
- `.codex/skills/meta-orchestration/references/architecture-index.md` is the architecture index (mirrored from `.claude/agents/CLAUDE.md`)
- `.codex/skills/meta-orchestration/references/migration-notes.md` is the Claude Code → Codex migration guide

Codex is **not** looking at the canonical 13-atom definitions. Those live at `.claude/agents/M##-*.md` and are referenced from the architecture index.

## Canonical vs Mirror / 主源与镜像

| Asset Class | Canonical Home (Claude Code) | Codex Mirror | Edit Where? |
|-------------|------------------------------|--------------|-------------|
| 13 atom definitions | `.claude/agents/M##-*.md` | (referenced, not duplicated) | Claude Code |
| Orchestration command | `.claude/commands/meta.md` | `codex-export/.codex/skills/meta-orchestration/SKILL.md` | Claude Code, then re-mirror |
| Architecture index | `.claude/agents/CLAUDE.md` | `codex-export/.codex/skills/meta-orchestration/references/architecture-index.md` | Claude Code, then re-mirror |
| Project Agent definitions | `agents/*-Agent.md` | (per-project, not exported) | Per project |
| Memory & scars | `memory/`, `~/.claude/scars/` | (per-project / per-user, not exported) | Per project / globally |
| MCP server | `~/.claude/scripts/mcp/` | (Codex needs separate adapter) | See migration-notes |

**Important maintenance rule:**

- `.claude/agents/*.md`, `.claude/agents/CLAUDE.md`, and `.claude/commands/meta.md` are the **canonical sources**.
- Files inside `codex-export/.codex/` are derived mirrors. Do not treat Codex-side edits as authoritative.

## Capability-First Routing / 能力优先路由

DreamMeta's M05-route follows a capability-first, not name-first, dispatch model:

```
Need capability X
-> M05 checks project agents/ for an existing Agent owning X
-> if no match, M05 searches global resources (.claude/skills/, .claude/agents/, references/*/SKILL.md)
-> if still no match, M13 creates a new project Agent definition for X
-> only then dispatch
```

Hardcoding "call Agent X" without the search step violates the **复用优先 / Reuse-First** principle.

## Default Behavior In Codex / Codex 默认行为

The intended default behavior when a user invokes the meta-orchestration skill:

1. user provides raw intent (`$ARGUMENTS`)
2. Phase A: M03 channel intake → A1.5 intent amplification (if fuzzy) → A2 decompose → A3 route → A4 dispatch design book → A5 intent lock-in
3. Phase B: M13 creates / B2 reuses project Agent definitions → B3 verifies definition quality → B3.5 dispatch plan audit (if subTasks ≥ 3)
4. Phase C: dispatch Codex subagent invocations per project Agent definition → C2 verify outputs → C3 evaluate (≥16/20) → C3.5 meta-review (conditional) → C4 iteration closure loop (max 3 rounds)
5. Phase D: D1 synthesize → D2 deliver → D3 evolution writeback → D4 governance health check (conditional)

The Meta-Department orchestrator (you, as the main thread under the meta-orchestration skill) **thinks and dispatches**. It does **not** execute work itself.

## Critical Rule: Dispatch Before You Execute / 关键规则：先派遣再执行

For any standard or heavy task, Codex should behave as the **dispatcher**, not the all-in-one executor.

- **Phase A** (analyze): the orchestrator does this in its own context — this is the only phase where the orchestrator may "do work"
- **Phase B** (create / reuse): the orchestrator writes Agent definition `.md` files; B3 verification is dispatched to an independent subagent
- **Phase C** (execute): the orchestrator dispatches one Codex subagent invocation per project Agent; verification (M12) and evaluation (M06) **must** be different subagent instances with isolated context
- **Phase D** (deliver / evolve): synthesis (M07) is dispatched if there are ≥3 sources; D3 writeback is performed by the orchestrator (infrastructure work)

The core principle is: **Meta-Department thinks, project Agents do.**

## The Eight Iron Laws / 八条铁律

These are reproduced verbatim from `.claude/commands/meta.md`. Violating any one of them is execution failure:

1. **元部门是「创造工具的工具」** — core output is project Agent definitions, not work deliverables.
2. **先创造 Agent，再用 Agent 做事** — standard / heavy tasks must create or reuse project Agents in `agents/` before Phase C; skipping Phase B is forbidden.
3. **复用优先** — M05 must check `agents/` for existing Agent definitions first; do not duplicate.
4. **三权分立** — execution Agent, verify Agent (M12), evaluate Agent (M06) **must** be different subagent instances with isolated context.
5. **并行优先** — independent sub-tasks **must** be dispatched in parallel (≤5 per batch); >5 → split into batches with convergence checkpoints.
6. **微型是唯一的例外** — micro-task exemption requires all three: single clear operation, ≤1 file & ≤10 lines, no verification needed; any doubt → upgrade to standard.
7. **先读后派** — before dispatching any Agent, read `architecture-index.md` and the relevant atom definitions.
8. **后置摘要纪律** — produce the completion summary **after** Edit / Write tool calls have actually returned success; promise-style summaries are forbidden.

## Hidden Skeleton / 治理骨架

Under the readable Phase A → B → C → D flow, DreamMeta also depends on hidden governance state:

- `intentPacket` + `intentGatePacket` (A5 intent lock-in)
- `dispatchPlanAudit` (B3.5)
- `iterationCounter` (C4 iteration closure loop, max 3 rounds)
- `scarPool` (project `memory/scars/` + global `~/.claude/scars/`)
- `evolutionWritebackDecision` (D3 four-dimension audit: Pattern / Scar / Agent Boundary / Routing)
- `governanceHealthCheck` (D4 four-item check: atom integrity / Agent reference validity / scar coverage / chain integrity)

This skeleton is not a second user interface. It exists so runs can be governed without pretending unfinished work is complete.

## Anti-Pattern / 反模式

```text
User: build a notification system
Codex: starts editing 10 files directly without delegation
```

Wrong. The orchestrator must:

1. Phase A: clarify scope, run intent amplification if fuzzy, lock intent
2. Phase B: check `agents/` for existing notification-related Agent; if none, create one (e.g. `Notification-Composer-Agent.md`)
3. Phase C: dispatch a Codex subagent invocation that loads `Notification-Composer-Agent.md` and writes the actual code
4. Phase C: dispatch an independent verify subagent (M12 role); dispatch an independent evaluate subagent (M06 role)
5. Phase D: synthesize, deliver, run D3 writeback (record patterns, scars, capability gaps)

## Maintenance Loop / 维护循环

After editing canonical files at `.claude/`:

1. open the canonical files at `.claude/agents/` and `.claude/commands/meta.md`
2. apply the change there first (Claude Code is the editing home)
3. re-mirror into `codex-export/.codex/skills/meta-orchestration/SKILL.md` and `architecture-index.md`
4. validate that Codex-side path references match the new content
5. commit both canonical and mirror changes together

DreamMeta does not currently ship a `npm run sync:runtimes` script (Meta_Kim does). The mirror sync is manual — the responsibility lives with whoever edits canonical files.

## One-Line Interpretation / 一句话总结

Do not read DreamMeta as "many atom files".

Read it as:

**a Meta-Department architecture for creating project Agents, with Codex as one runtime projection of the same governance system whose canonical source lives in Claude Code.**
