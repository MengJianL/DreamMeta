# Vibe-Skills 学习摘要 / Study Summary for DreamMeta

> Source: https://github.com/foryourhealth111-pixel/Vibe-Skills (v3.0.0, snapshot 2026-04-11)
> 本快照为精选子集（961KB / 119 files），原项目 50MB / 3400+ files。
> 排除了 `bundled/`（340+ 薄封装 skill）、`scripts/`、`tests/`、`adapters/` 等执行层。

## 一、项目定位

Vibe-Skills (VCO — Vibe Code Orchestrator) 自定义为「个人 AI 操作系统」，核心不是 skill 集合，而是 **治理运行时 (governed runtime)**。哲学：governance over freedom。

## 二、对 DreamMeta 有价值的 7 个模式

### 1. 六阶段状态机 (6-Stage Runtime)

`skeleton_check → deep_interview → requirement_doc → xl_plan → plan_execute → phase_cleanup`

**与 DreamMeta 的映射**：DreamMeta `/meta` 四阶段（A→B→C→D）覆盖了类似流程，但 VCO 的 `skeleton_check`（先探测仓库结构再做任何事）和 `phase_cleanup`（强制清理临时产物+审计轨迹）是 DreamMeta 当前未显式覆盖的端点。

**可吸收点**：
- Phase A 前增加 skeleton_check 概念（M10-retrieve 探测项目状态）
- Phase D 后增加 cleanup 步骤（清理临时文件、生成审计轨迹）

### 2. Closure-First Contract (2 Probes + 1 Verify)

任务前 3 个动作必须完成：Probe#1 (glob 探测仓库形态) → Probe#2 (rg 搜索关键词) → Verify#1 (验证至少 1 个关键假设)。

**与 DreamMeta 的映射**：「先读后派」原则的操作化版本。DreamMeta 要求「读 CLAUDE.md + 原子定义」，VCO 更进一步要求 probe 项目实际状态。

**可吸收点**：强化 Phase A 或 Phase C dispatch 前的实际项目状态探测。

### 3. M/L/XL 执行分级 (Execution Topology Grades)

| Grade | 特征 |
|-------|------|
| M (单 Agent) | 窄范围，无委派，顺序执行 |
| L (串行原生) | 多步串行，从冻结计划执行，有限委派单元 |
| XL (波次顺序) | 多 Agent 编排，步级有界并行（max 2 并行单元），每步检查点 |

**与 DreamMeta 的映射**：DreamMeta 有 micro/standard/heavy 三级，但缺少执行拓扑的正式规则（如 max 并行数、检查点频率）。

**可吸收点**：在 meta.md 的复杂度判定中引入更精确的执行拓扑约束。

### 4. Root/Child 治理车道 + 委派信封 (Delegation Envelope)

XL 模式下：
- `root_governed`：拥有需求/计划的唯一真相，发出最终完成声明
- `child_governed`：继承冻结上下文，只发射局部收据，不能创建第二个需求/计划表面

委派信封格式：`run_id, phase, owner, deadline_minutes, retry_budget, deliverable, memory`

**与 DreamMeta 的映射**：DreamMeta 的三权分立（执行/核验/评估分离）确保了角色隔离，但 Agent dispatch 时缺少结构化的「委派信封」。当前 dispatch 是自然语言 prompt。

**可吸收点**：为 Phase C 的 Agent dispatch 设计结构化委派格式（而非纯自然语言 prompt）。

### 5. Anti-Drift Guardrails（防漂移护栏）

显式的代理目标漂移防护：
- 不得优化可见代理信号而放弃冻结目标
- 不得未经批准将验证材料吸收为产品真相
- 不得将有界修复重标签为通用完成
- 保持有界专业化，不擅自扩展范围

**与 DreamMeta 的映射**：DreamMeta 有 A5 意图锁定 + C2 过早完成防护，但缺少 VCO 这种显式的「漂移类型清单」。

**可吸收点**：在 M12-verify 或 meta.md C2 中增加漂移类型枚举。

### 6. Evidence-Based Communication (P5 模式)

绝不说 "should work"。公式：`[Command] → [Output] → [Claim]`。

**与 DreamMeta 的映射**：RPT-001 已建立 fabrication check 绝对优先级，P5 是更具体的操作模式。

**可吸收点**：作为 M12-verify 的标准核验格式参考。

### 7. Skill 契约体系 (Skill Contract Schema)

每个 skill 有正式 JSON 契约（`schemas/skill-contract.v1.schema.json`），包含：schema_version, skill_id, status (canonical/experimental/deprecated), sources, frontmatter invariants。

**与 DreamMeta 的映射**：DreamMeta 的 Agent 定义用 markdown 模板（9-section），缺少机器可读的契约层。

**可吸收点**：未来可考虑为 Project Agent 定义增加可选的 JSON 契约（用于自动化路由匹配、兼容性检查）。

## 三、不适合直接吸收的部分

| 方面 | 原因 |
|------|------|
| 单一权威运行时 | VCO 强调 single canonical router，DreamMeta 是 13 原子分布式权威，哲学冲突 |
| 340+ bundled skills | 大多是薄封装，对 DreamMeta 无直接价值（M10 可按需发现） |
| Host adapters | DreamMeta 当前绑定 Claude Code，无需多 host 适配 |
| 内存系统具体实现 | VCO 依赖 Serena/ruflo/Cognee 等外部服务，DreamMeta 用 M01-memory 原子 |
| 6 阶段强制状态机 | DreamMeta 的 4 阶段治理链已足够，且更灵活（micro 可跳过） |

## 四、快照内容索引

```
protocols/          — 6 个协议定义 (runtime/think/do/review/team/retro)
core/skills/        — 7 个核心 skill 定义
core/skill-contracts/ — JSON 契约
schemas/            — JSON Schema 定义
config/             — 6 个核心治理/路由配置文件
docs/               — 架构文档 + 宣言
agents/templates/   — Agent 模板
templates/          — 计划/需求模板
SKILL.md            — 根 skill 定义
README.md           — 项目说明
```

## 五、评估结论

**学习有效性：有效（选择性吸收）**

Vibe-Skills 是一个成熟的治理框架，其核心治理模式（closure-first、anti-drift、delegation envelope、execution grading、evidence-based communication）对 DreamMeta 有参考价值。但两者的治理哲学不同（单一权威 vs 13 原子分布式），不宜整体移植，适合模式级借鉴。
