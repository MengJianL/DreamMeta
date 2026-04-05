<div align="center">

# DreamMeta 梦元

**A 13-atom organizational architecture for autonomous AI agent governance**

*"Governance cannot be absent — 协同可以扁平，治理不能缺位。"*

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Built%20with-Claude%20Code-blueviolet)](https://claude.ai/code)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18957649-blue)](https://zenodo.org/records/18957649)

[Paper](#references) · [Architecture](#architecture-three-layer-gravity-structure) · [Quick Start](#quick-start) · [13 Atoms](#the-13-atoms) · [Contributing](#contributing)

</div>

---

## What is DreamMeta?

DreamMeta is a **Meta-Department (元部门)** — an organizational pattern for AI agent systems inspired by real-world corporate structures. Instead of monolithic prompts or ad-hoc agent chains, it decomposes agent coordination into **13 irreducible atomic units** arranged in a three-layer gravity structure.

The Meta-Department is a **"tool that creates tools"** (创造工具的工具). Its primary output is **Project Agent definitions**, not work deliverables — the department creates tools, then uses those tools to do work.

### Why DreamMeta?

- **Governance-first** — Every atom answers: what am I, what am I not, how am I governed, how do I evolve
- **Pure-abstract** — No domain-specific vocabulary; drop into any project and it works
- **Self-evolving** — Built-in feedback loops, scar protocols, and evolution writeback at every layer
- **Separation of powers** — Execution, verification, and evaluation are structurally isolated (三权分立)
- **Five-level creation** — From project agents (L0) to full meta-department replication (L4)

> [!NOTE]
> This is not a traditional software project with build/test commands. It is a **configuration-as-architecture** system where `.md` files define agent behaviors, and the structure itself is the product.

## Quick Start

### 1. Bootstrap a new project

```bash
# Copy the 13 atoms + architecture index into your project
cp -r .claude/agents/ your-project/.claude/agents/
cp -r .claude/commands/ your-project/.claude/commands/
```

### 2. Run the Meta-Department

In [Claude Code](https://claude.ai/code), use the `/meta` slash command:

```
/meta <describe your task here>
```

The Meta-Department will:
1. **Amplify** your intent (expand fuzzy tasks along 3 dimensions)
2. **Analyze** and decompose the task
3. **Create or reuse** Project Agent definitions
4. **Execute** via those Agent definitions
5. **Verify & evaluate** independently (separation of powers)
6. **Deliver** synthesized results

### 3. MCP Server (Optional)

```bash
npm install
npm run mcp:start
```

Exposes `list_atoms` and `get_atom` tools for programmatic access to the 13-atom architecture.

## Architecture: Three-Layer Gravity Structure

```
┌─────────────────────────────────────────────────────────────────┐
│  Layer 3 — Execution                                            │
│  M09 Compose · M10 Retrieve · M11 Invoke · M12 Verify · M13 Create │
├─────────────────────────────────────────────────────────────────┤
│  Layer 2 — Orchestration                                        │
│  M04 Decompose · M05 Route · M06 Evaluate · M07 Synthesize · M08 Sequence │
├─────────────────────────────────────────────────────────────────┤
│  Layer 1 — Foundation                                           │
│  M01 Memory · M02 Identity · M03 Channel                        │
└─────────────────────────────────────────────────────────────────┘
```

| Layer | Role | Atoms |
|-------|------|-------|
| **Foundation** | Storage, identity, communication | M01 Memory · M02 Identity · M03 Channel |
| **Orchestration** | Coordinate, route, evaluate, sequence | M04 Decompose · M05 Route · M06 Evaluate · M07 Synthesize · M08 Sequence |
| **Execution** | Atomic operations | M09 Compose · M10 Retrieve · M11 Invoke · M12 Verify · M13 Create |

### Three-Layer Tool Hierarchy

```
┌────────────────────────────────────────────────┐
│  Project Agent Definitions (agents/)            │  ← Created by Meta-Department
├────────────────────────────────────────────────┤
│  13 Atoms (.claude/agents/)                     │  ← Infrastructure for creating Agents
├────────────────────────────────────────────────┤
│  Claude Code Agent Tool                         │  ← Runtime execution
└────────────────────────────────────────────────┘
```

## The 13 Atoms

| # | Atom | Layer | Core Responsibility |
|---|------|-------|---------------------|
| M01 | **Memory** 记忆元 | Foundation | Layered storage, compression, scar protocol |
| M02 | **Identity** 身份元 | Foundation | Role boundaries, behavioral constraints, capability profiles |
| M03 | **Channel** 通信元 | Foundation | Inter-layer information flow and filtering |
| M04 | **Decompose** 分解元 | Orchestration | Intent amplification and task decomposition |
| M05 | **Route** 路由元 | Orchestration | Capability-matched routing + reuse-before-create |
| M06 | **Evaluate** 评估元 | Orchestration | Multi-dimensional quality assessment + meta-review |
| M07 | **Synthesize** 聚合元 | Orchestration | Multi-source integration and conflict resolution |
| M08 | **Sequence** 序列元 | Orchestration | Pipeline orchestration and attention cost management |
| M09 | **Compose** 构成元 | Execution | Compose candidate content under constraints |
| M10 | **Retrieve** 检索元 | Execution | Locate and extract contextually relevant information |
| M11 | **Invoke** 调用元 | Execution | Trigger external tools/APIs and process results |
| M12 | **Verify** 验证元 | Execution | Constraint verification, anti-SLOP detection, gate decisions |
| M13 | **Create** 创造元 | Execution | Pattern recombination, agent creation (L0–L4) |

### Five Core Chains

```
Standard Task:       M03 → M04 → M05 → M08 → M09/M10/M11 → M12 → M06 → M07 → M03
Candidate Generation: M04 → M05 → M09 → M12 → M06 → M07
Retrieval & Reuse:    M04/M05 → M10 → M12/M06 → M07
External Capability:  M05 → M11 → M12 → M06 → M07
Capability Creation:  M05/M10/M01 → M13 → M12 → M06 → M01 → M05
```

### Two Governance Loops

- **Quality Loop**: Execution → M12 verify → M06 evaluate → reflow → re-execute
- **Evolution Loop**: Historical gaps → M13 create → M12 verify → M06 evaluate → M01 persist → M05 route

## Project Agent System

Each Project Agent is **triple-armed** (Prompt + Skill + Tools) with a **9-section template**:

| Section | Purpose |
|---------|---------|
| **Identity** | Role, domain expertise, decision authority |
| **Atom Mapping** | Which M## atom(s) it instantiates |
| **Input Contract** | Accepted formats, validation, prerequisites |
| **Output Contract** | Normal output, failure reports, downstream |
| **Execution Protocol** | Step-by-step procedure |
| **Behavioral Constraints** | Must-do, must-not-do, context isolation |
| **Quality Standards** | Quantified acceptance criteria |
| **Skill Loadout** | Core + auxiliary skills (auto-matched) |
| **Tool Priority** | Primary, auxiliary, forbidden tools (auto-matched) |

### Routing Priority (M05)

1. **Match in `agents/`** → Reuse existing Project Agent
2. **Match in global resources** → Invoke directly via Skill tool
3. **No match** → Create new Agent → Verify → Execute
4. **Partial match** → Update Agent version

## M13: Five-Level Creation

| Level | Creates | Gate Control |
|-------|---------|-------------|
| **L0** Project Agent | Task-specific agent definitions | None — standard output |
| **L1** Skill | Reusable patterns & modules | 2x validation |
| **L2** Agent | New atomic units with identity | 5-gate process |
| **L3** Meta-Department | Full 13-atom system instances | Lineage tracking |
| **L4** Governance-Aware Replication | Parent-child meta-departments | Structural governance |

> [!TIP]
> L0 is the most common creation — on every task, the Meta-Department first creates or reuses Agent definitions, then dispatches execution. This embodies the "tool that creates tools" philosophy.

## Design Principles

1. **Irreducibility** — Each atom, if further decomposed, loses independent semantic integrity
2. **Pure Abstraction** — No domain-specific vocabulary; cross-domain reusable
3. **Self-Evolution** — Every atom has built-in feedback-driven adaptation
4. **Orthogonality** — Clear boundaries, no functional overlap
5. **Governance First** — Each atom defines what it is, what it isn't, how it's governed, how it evolves
6. **Separation of Powers** — M06 (evaluate) and M12 (verify) are structurally forbidden from writing

## Project Structure

```
DreamMeta/
├── .claude/
│   ├── agents/              # 13 atoms + architecture index (CLAUDE.md)
│   └── commands/            # /meta slash command
├── agents/                  # Project Agent definitions (created by Meta-Department)
├── references/              # Source paper, architecture diagrams, reference implementations
├── scripts/
│   └── mcp/                 # MCP runtime server
├── CLAUDE.md                # Project instructions for Claude Code
└── README.md
```

## Cross-Project Reuse

```bash
# Copy atoms + commands (universal infrastructure)
cp -r .claude/agents/ your-project/.claude/agents/
cp -r .claude/commands/ your-project/.claude/commands/

# Do NOT copy:
# - agents/          → project-specific, accumulates its own
# - .claude/memory/  → each project has its own memory (M01 principle)
```

## Contributing

Contributions are welcome! Areas of interest:

- **New atom proposals** — Must pass the irreducibility and orthogonality tests
- **Project Agent definitions** — Share reusable agent patterns
- **MCP server extensions** — New tools for programmatic architecture access
- **Cross-domain validation** — Test the framework in different project types

## References

> Meng Jian, Jin Zhongxu. *AI Agent Multi-Agent Collaboration Architecture Design Based on "Organizational Mirroring" Theory*. Zenodo, 2025.
>
> 孟健, 金仲旭. *基于"组织镜像"理论的AI智能体多Agent协作架构设计*. Zenodo, 2025.

**DOI**: [10.5281/zenodo.18957649](https://zenodo.org/records/18957649)

## Acknowledgments

- **[KimYx0207](https://github.com/KimYx0207)** — Invaluable contributions, scar protocol inspiration, reference architecture ([Meta_Kim](references/Meta_Kim-v20260403/))
- **[Claude](https://claude.ai)** (Anthropic) — Architecture co-design, documentation, implementation
- **[ChatGPT](https://chatgpt.com)** (OpenAI) — Architecture co-design, documentation, implementation

## License

[MIT](LICENSE)
