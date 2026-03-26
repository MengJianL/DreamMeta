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
│  M09-generate(写)  M10-retrieve(查)  M11-invoke(用)                  │
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
| **Execution** | M09 Generate · M10 Retrieve · M11 Invoke · M12 Verify · M13 Create | Atomic operations: write, query, use, check, create |

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
| M09 | Generate 生成元 | 写 | Produce structured content from constraints |
| M10 | Retrieve 检索元 | 查 | Locate and extract contextually relevant information |
| M11 | Invoke 调用元 | 用 | Trigger external tools/APIs and process results |
| M12 | Verify 验证元 | 检 | Constraint-set verification and gate decisions |
| M13 | Create 创造元 | 创 | Pattern recombination, skill engineering, agent creation |

## Design Principles

1. **Irreducibility** — Each of the 13 atoms, if further decomposed, would lose its independent semantic integrity
2. **Pure Abstraction** — All descriptions contain no domain-specific vocabulary, enabling cross-domain reuse
3. **Self-Evolution** — Every atom has a built-in feedback-driven adaptive mechanism
4. **Orthogonality** — Clear responsibility boundaries between atoms with no functional overlap
5. **Thinking Enhancement** — Orchestration layer atoms are equipped with Critical & Deep Thinking mode
6. **Evolvable Architecture** — M13 can create new atoms, making the framework itself growable

## Self-Evolution

Every atom includes a self-evolution mechanism:

```
Trigger   → specific metric thresholds (e.g., hit rate < 60%, pass rate < 50%)
Data      → execution feedback, quality scores, usage statistics
Action    → parameter tuning, strategy adjustment, capability re-calibration
Record    → all evolution actions logged to the atom's evolution journal
```

## M13: The Creator of Creators

M13 (Create) has **dual creation capabilities**:

- **Skill Creation** — Full lifecycle: draft → evaluate → review → improve → package → distribute
- **Agent Creation** — Five-gate process to create new atoms when structural gaps are confirmed

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
    ├── M09-generate.md     # Execution: Generate (写)
    ├── M10-retrieve.md     # Execution: Retrieve (查)
    ├── M11-invoke.md       # Execution: Invoke (用)
    ├── M12-verify.md       # Execution: Verify (检)
    └── M13-create.md       # Execution: Create (创)
```

## License

MIT
