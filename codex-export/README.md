# DreamMeta — Codex Export / Codex 移植版本

This folder is the **Codex-portable mirror** of the DreamMeta Meta-Department governance framework. It is **not** the canonical home — the canonical source lives in `.claude/` of the parent DreamMeta project.

> Source: DreamMeta Claude Code canonical at `.claude/` (this folder is a mirror generated for Codex deployment).

## What This Folder Is / 这个文件夹是什么

DreamMeta is a 13-atom Meta-Department architecture originally authored for Claude Code. This `codex-export/` folder packages the parts that need to travel to a Codex environment:

- the top-level `AGENTS.md` (Codex's project guide)
- the `meta-orchestration` Codex skill (the 13-atom governance chain)
- two reference files: the architecture index and migration notes

The folder is **self-contained for transfer** — copy it whole into a Codex workspace and the meta-orchestration skill becomes available there.

## Folder Layout / 文件清单

```
codex-export/
├── AGENTS.md                                     ← Codex top-level project guide
├── README.md                                     ← this file
└── .codex/
    └── skills/
        └── meta-orchestration/
            ├── SKILL.md                          ← Codex skill (mirror of .claude/commands/meta.md)
            └── references/
                ├── architecture-index.md         ← mirror of .claude/agents/CLAUDE.md
                └── migration-notes.md            ← Claude Code → Codex migration guide
```

## Source-to-Mirror Mapping / 源到镜像对应关系

| Codex Mirror File | Canonical Source (Claude Code) | Note |
|---|---|---|
| `codex-export/AGENTS.md` | (newly authored for Codex) | DreamMeta-Codex equivalent of Meta_Kim's `AGENTS.md` |
| `codex-export/.codex/skills/meta-orchestration/SKILL.md` | `.claude/commands/meta.md` | Codex skill format with frontmatter |
| `codex-export/.codex/skills/meta-orchestration/references/architecture-index.md` | `.claude/agents/CLAUDE.md` | Mirror with Codex-aware path & concept rewording |
| `codex-export/.codex/skills/meta-orchestration/references/migration-notes.md` | (newly authored) | Migration guide |

The 13 atom definition files (`M01-memory.md` through `M13-create.md`) are **not** duplicated into this export. They remain authoritative at `.claude/agents/M##-*.md`. The architecture index references them by Codex-mapped path (`codex-export/.codex/agents/M##-*.toml`) for users who choose to convert atoms into Codex-native subagent TOML files.

## Deployment Steps / 部署步骤

To deploy DreamMeta into a Codex workspace:

1. **Copy this folder** into the target Codex project root, or unpack its contents:
   - Place `AGENTS.md` at the project root (or merge with an existing one).
   - Place `.codex/skills/meta-orchestration/` at `<project>/.codex/skills/meta-orchestration/`.

2. **Adapt the 13 atom definitions** (one-time work, optional but recommended):
   - The 13 atom files at `.claude/agents/M##-*.md` are markdown.
   - For deeper Codex integration, convert each atom into a Codex subagent TOML at `.codex/agents/M##-*.toml`. (See `architecture-index.md` for the Codex-mapped paths.)
   - If you skip TOML conversion, the meta-orchestration skill still works — it just delegates to Codex's generic subagent invocation rather than to atom-specific subagents.

3. **Verify the skill loads** in Codex:
   - Check that `.codex/skills/meta-orchestration/SKILL.md` is recognized by your Codex installation.
   - Trigger phrases include: `元部门`, `13 原子`, `治理链`, `项目 Agent`, `三权分立`, `Meta-Department`, `13 atoms`, `governance chain`, `project Agent`, `separation of powers`, `intent lock-in`, `evolution writeback`, etc. (full list in the SKILL.md frontmatter).

4. **Initialize per-project assets** (created on first invocation):
   - `agents/` — for project Agent definitions (auto-created on first `/meta` task).
   - `memory/` — for project-specific scars, patterns, capability gaps (auto-created on first D3 evolution writeback).

## Differences From Claude Code Version / 与 Claude Code 版本的差异

| Concept | Claude Code Version | Codex Version |
|---|---|---|
| Subagent dispatch | `Agent` tool (Claude Code's named subagent_type) | Codex subagent invocation (per Codex platform conventions) |
| Skill invocation | `Skill` tool with skill name | Codex skill invocation mechanism |
| User questions | `AskUserQuestion` tool | Codex's user-prompt mechanism (varies by Codex frontend) |
| MCP server | `~/.claude/scripts/mcp/` | Requires Codex-side MCP adapter; not part of this export |
| Hooks | `.claude/settings.json` | Codex's equivalent permissions / hooks layer |

The **governance logic** (eight iron laws, four phases, three-layer gravity structure, separation of powers, scar pool, evolution writeback) is **identical** across both versions — that is intentional. Only the surface tool names and platform mechanics differ.

## Limitations / 限制与注意事项

The following are **deliberately not exported** because they are project-specific or user-specific:

- **`agents/`** — every project accumulates its own project Agent definitions. The Meta-Department creates them on demand; do not seed them from another project.
- **`memory/`** — scars, patterns, and capability gaps are project-specific. Cross-pollination defeats the purpose of project-level governance.
- **`~/.claude/scars/`** — global scar pool is per-user, not per-project. Codex users would maintain their own equivalent global scar pool.
- **`~/.claude/agent-registry/`** — global cross-project Agent registry is per-user.

In short: **the framework travels, the experience does not.** Each Codex deployment of DreamMeta starts with a clean `agents/` and `memory/` and accumulates its own.

## Known Gaps / 已知差距

- **MCP server adapter**: the canonical DreamMeta ships a Claude Code MCP server (under `~/.claude/scripts/mcp/`). The Codex-equivalent has not been built. Tasks that require MCP integration in Codex must use Codex-native MCP wiring; see `migration-notes.md` for guidance.
- **Skill ↔ subagent name mappings**: trigger keywords in the SKILL.md frontmatter are tuned for Claude Code's `Skill` tool. Codex's skill discovery may handle them differently — verify after deployment.
- **`Agent` tool semantics**: where the canonical meta.md says "use the Agent tool", the Codex mirror notes this as "Codex subagent invocation". The exact Codex syntax depends on the Codex installation; treat the mirror as **conceptually equivalent**, not syntactically identical.

## Maintenance Workflow / 维护流程

When DreamMeta evolves on the Claude Code side:

1. **Edit canonical files first**: changes go into `.claude/agents/`, `.claude/commands/meta.md`, or `.claude/agents/CLAUDE.md`.
2. **Re-mirror into `codex-export/`**: regenerate `SKILL.md` and `architecture-index.md` from their canonical counterparts.
3. **Test in Codex**: after re-mirroring, run a smoke test (e.g. invoke meta-orchestration with a simple task) inside Codex.
4. **Commit both sides together**: a single commit should contain canonical edits and their mirror updates, so the two never drift.

Codex-side observations or fixes should **flow back** to `.claude/` first, then re-mirror. Direct edits to `codex-export/.codex/` are discouraged because they get overwritten on the next mirror cycle.

## One-Line Summary / 一句话总结

`codex-export/` is the portable Codex projection of DreamMeta — copy it into a Codex workspace, accept that `agents/` and `memory/` start empty, and treat `.claude/` as the canonical editing home.
