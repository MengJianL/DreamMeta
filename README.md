# Meta-Creates 元部门

> "协同可以扁平，治理不能缺位。"

**Meta-Creates** is a **Meta-Department (元部门) architecture framework** — a 13-atom organizational system for autonomous AI agent coordination and governance. It provides a pure-abstract, domain-agnostic, self-evolving infrastructure where `.md` files define agent behaviors, and the structure itself is the product.

## What is a Meta-Department?

A Meta-Department is an organizational pattern inspired by real-world corporate structures, applied to AI agent systems. Instead of monolithic prompts or ad-hoc agent chains, Meta-Creates decomposes agent coordination into **13 irreducible atomic units** ("atoms") arranged in a three-layer gravity structure — mirroring how real organizations separate infrastructure, management, and execution.

The key insight: **governance cannot be absent**. Just as a company needs clear roles, communication channels, and quality oversight, an AI agent system needs the same — formalized, self-evolving, and domain-agnostic.

## Architecture: Three-Layer Gravity Structure

```
┌─────────────────────────────────────────────────────────────────────┐
│  Layer 3 — Execution (原子操作)                                      │
│  M09-compose(写)   M10-retrieve(查)  M11-invoke(用)                  │
│  M12-verify(检)    M13-create(创)                                    │
├─────────────────────────────────────────────────────────────────────┤
│  Layer 2 — Orchestration (编排协调) [Critical & Deep Thinking]       │
│  M04-decompose  M05-route  M06-evaluate  M07-synthesize  M08-sequence│
├─────────────────────────────────────────────────────────────────────┤
│  Layer 1 — Foundation (基础设施)                                      │
│  M01-memory        M02-identity        M03-channel                   │
└─────────────────────────────────────────────────────────────────────┘
```

| Layer | Atoms | Role |
|-------|-------|------|
| **Foundation** | M01 Memory · M02 Identity · M03 Channel | Storage, identity, and communication infrastructure |
| **Orchestration** | M04 Decompose · M05 Route · M06 Evaluate · M07 Synthesize · M08 Sequence | Coordinate, route, evaluate, and sequence — all with Critical & Deep Thinking |
| **Execution** | M09 Compose · M10 Retrieve · M11 Invoke · M12 Verify · M13 Create | Atomic operations: compose, query, invoke, verify, create |

## The 13 Atoms

| # | Atom | Op | Core Responsibility |
|---|------|----|---------------------|
| M01 | Memory 记忆元 | — | Layered storage, compression, and isolated retrieval |
| M02 | Identity 身份元 | — | Role boundaries, behavioral constraints, capability profiles |
| M03 | Channel 通信元 | — | Inter-layer information flow control and filtering |
| M04 | Decompose 分解元 | — | Intent decomposition and Intent Amplification Ratio (IAR) |
| M05 | Route 路由元 | — | Capability-matched routing + skill discovery |
| M06 | Evaluate 评估元 | — | Multi-dimensional independent quality assessment |
| M07 | Synthesize 聚合元 | — | Multi-source deduplication, integration, conflict detection |
| M08 | Sequence 序列元 | — | Pipeline orchestration and stage gating |
| M09 | Compose 构成元 | 写 | Compose candidate content objects under constraints |
| M10 | Retrieve 检索元 | 查 | Locate and extract contextually relevant information |
| M11 | Invoke 调用元 | 用 | Trigger external tools/APIs and process results |
| M12 | Verify 验证元 | 检 | Constraint-set verification and gate decisions |
| M13 | Create 创造元 | 创 | Pattern recombination, skill engineering, agent creation |

## Five Core Questions

The 13 atoms are not 13 parallel actions — they form a complete structure from **continuous existence → organized progression → independent governance → result formation → capability extension**:

1. **How does the system persist?** — M01 / M02 / M03
2. **How does the system organize problems?** — M04 / M05 / M08
3. **How does the system judge quality and validity?** — M06 / M12
4. **How does the system produce and advance results?** — M09 / M10 / M11 / M07
5. **How does the system extend its own capabilities?** — M13

## Five Core Chains

```
Chain 1 (Standard Task):     M03 → M04 → M05 → M08 → M09/M10/M11 → M12 → M06 → M07 → M03
Chain 2 (Candidate Generation): M04 → M05 → M09 → M12 → M06 → M07
Chain 3 (Retrieval & Reuse):    M04/M05 → M10 → M12/M06 → M07
Chain 4 (External Capability):  M05 → M11 → M12 → M06 → M07
Chain 5 (Capability Creation):  M05/M10/M01 → M13 → M12 → M06 → M01 → M05
```

## Two Governance Loops

- **Quality Loop**: Execution output → M12 verify → M06 evaluate → reflow to origin → re-execute
- **Evolution Loop**: Historical gaps → M13 create → M12 verify → M06 evaluate → M01 persist → M05 route for reuse

## M06 vs M12: Evaluate vs Verify

A critical architectural distinction:

| | M06 Evaluate | M12 Verify |
|---|---|---|
| **Question** | "Is it good enough?" | "Does it hold up?" |
| **Judges** | Quality, completeness, actionability | Validity, consistency, constraint satisfaction |
| **Output** | Score + pass/fail + improvement direction | Pass/fail per condition + failure points |

## Design Principles

1. **Irreducibility** — Each atom, if further decomposed, loses independent semantic integrity
2. **Pure Abstraction** — No domain-specific vocabulary; cross-domain reusable
3. **Self-Evolution** — Every atom has built-in feedback-driven adaptation
4. **Orthogonality** — Clear boundaries, no functional overlap
5. **Governance First** — Each atom answers: what am I, what am I not, how am I governed, how do I evolve
6. **Evolvable Architecture** — M13 can create new Skills, Agents, and Meta-Departments

## M13: Three-Level Creation

M13 (Create) has **three-level creation capabilities**:

| Level | What | Gate |
|-------|------|------|
| **Skill** | Reusable patterns & modules | 2x validation + clear I/O contract |
| **Agent** | New atomic units with identity & evolution | 5-gate process (gap → skill insufficient → layer → orthogonality → human confirm) |
| **Meta-Department** | Full 13-atom system instances | Lineage tracking + governance sync + independent evolution |

Architecture safety valve: when total atoms exceed 18, an architecture review is triggered.

## Cross-Project Reuse

To bootstrap a new project with the Meta-Department framework:

```bash
# Copy the 13 atoms + index
cp -r .claude/agents/ your-project/.claude/agents/

# Do NOT copy memory — each project maintains isolation (M01 principle)
```

## Project Structure

```
.claude/
└── agents/
    ├── CLAUDE.md           # Architecture index
    ├── M01-memory.md       # Foundation: Memory
    ├── M02-identity.md     # Foundation: Identity
    ├── M03-channel.md      # Foundation: Channel
    ├── M04-decompose.md    # Orchestration: Decompose
    ├── M05-route.md        # Orchestration: Route
    ├── M06-evaluate.md     # Orchestration: Evaluate
    ├── M07-synthesize.md   # Orchestration: Synthesize
    ├── M08-sequence.md     # Orchestration: Sequence
    ├── M09-compose.md      # Execution: Compose (写)
    ├── M10-retrieve.md     # Execution: Retrieve (查)
    ├── M11-invoke.md       # Execution: Invoke (用)
    ├── M12-verify.md       # Execution: Verify (检)
    └── M13-create.md       # Execution: Create (创)
```

## License

MIT
