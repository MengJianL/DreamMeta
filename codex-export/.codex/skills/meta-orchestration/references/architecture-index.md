# DreamMeta Architecture Index (Codex Mirror)

> **Source / 来源**: This is the Codex-facing architecture index, mirrored from `.claude/agents/CLAUDE.md` of the canonical DreamMeta source.
> **Canonical home / 正典之家**: DreamMeta's canonical home is Claude Code (`.claude/`). This Codex mirror is for reference and transferable use.
> **Maintenance / 维护**: Improvements discovered in Codex should flow back to `.claude/agents/CLAUDE.md` first, then sync here.

---

# Meta-Department 元部门架构索引

> 元部门是「创造工具的工具」，不是「做事的工具」。它为项目创造规范化的 Agent 定义，而不是直接产出工作成果物。Agent 定义存于项目 `agents/` 目录，可复用、可迭代、可积累。

---

## 一、总纲

本元部门由 **13 个不可拆分的原子元**组成，分为三层引力结构。

**核心运转原则：元部门是「创造工具的工具」——它为项目创造 Agent，而不是自己做事。**

- **基础层（L1）**由元部门直接维护——记忆、身份、通道是基础设施，不委派给临时 Agent
- **编排层（L2）**由元部门自身完成分析与设计——拆解、路由、编排是"设计 Agent 团队"的过程
- **执行层（L3）**的每个原子是**项目 Agent 的角色模板**——元部门为项目创造 Agent 定义（存于项目 `agents/` 目录），Agent 按定义执行，元部门不自行执行

13 原子回答五类核心问题：

1. **系统如何持续存在** — M01 / M02 / M03（元部门直接维护）
2. **系统如何把问题组织起来** — M04 / M05 / M08（元部门分析设计，产出 Agent 团队蓝图）
3. **系统如何判断做得是否足够好、是否成立** — M06 / M12（由独立 Agent 执行，三权分立）
4. **系统如何真正产出与推进结果** — M09 / M10 / M11 / M07（由派遣的 Agent 团队执行）
5. **系统如何扩展自身能力边界** — M13（由独立 Agent 执行创造）

---

## 二、三层引力结构

### Layer 1 — Foundation / 基础层

> 提供系统得以存在的三个连续性条件。由元部门直接维护，在所有层运行期间持续提供底座约束。

| 编号 | 原子 | 文件 | 连续性 | 核心职责 |
|------|------|------|--------|---------|
| M01 | memory | `codex-export/.codex/agents/M01-memory.toml` | 时间连续性 | 沉淀并治理组织记忆的连续性基础设施 |
| M02 | identity | `codex-export/.codex/agents/M02-identity.toml` | 存在连续性 | 定义并维持实体身份与职责边界的治理锚点 |
| M03 | channel | `codex-export/.codex/agents/M03-channel.toml` | 交互连续性 | 管理系统与外界交互边界与通道秩序的基础设施 |

基础层闭环：不失忆（M01）· 不失我（M02）· 不断联（M03）

### Layer 2 — Orchestration / 编排层

> 元部门的"大脑"——分析任务、设计 Agent 团队、制定推进秩序、裁决质量。编排层的产出是 Agent 团队设计书与治理决策，不是执行结果。

| 编号 | 原子 | 文件 | 组织操作 | 核心职责 |
|------|------|------|---------|---------|
| M04 | decompose | `codex-export/.codex/agents/M04-decompose.toml` | 结构化 | 将整体目标转化为可治理任务结构的拆解原子 |
| M05 | route | `codex-export/.codex/agents/M05-route.toml` | 归属化 | 将任务需求映射到合适执行 Agent 的归属原子 |
| M06 | evaluate | `codex-export/.codex/agents/M06-evaluate.toml` | 裁决化 | 对 Agent 产物质量与达标性进行独立裁决的评估原子（**必须**由独立 Agent 执行） |
| M07 | synthesize | `codex-export/.codex/agents/M07-synthesize.toml` | 复合化 | 将多个 Agent 结果整合为可追溯复合结果的综合原子 |
| M08 | sequence | `codex-export/.codex/agents/M08-sequence.toml` | 秩序化 | 为 Agent 团队建立推进秩序的时序编排原子 |

### Layer 3 — Execution / 执行层

> 五种本质不同的执行角色，由被派遣的独立 Agent 实例承担。元部门不在自身上下文中执行这些操作。

| 编号 | 原子 | 文件 | Agent 角色 | 核心职责 |
|------|------|------|-----------|---------|
| M09 | compose | `codex-export/.codex/agents/M09-compose.toml` | 构成 Agent | 在约束下构成候选内容对象 |
| M10 | retrieve | `codex-export/.codex/agents/M10-retrieve.toml` | 检索 Agent | 从既有来源召回对象、模式与依据 |
| M11 | invoke | `codex-export/.codex/agents/M11-invoke.toml` | 调用 Agent | 将任务需求接合到现成能力上 |
| M12 | verify | `codex-export/.codex/agents/M12-verify.toml` | 核验 Agent | 检查对象成立性与符合性（**不得**与生产者共享上下文） |
| M13 | create | `codex-export/.codex/agents/M13-create.toml` | 创造 Agent | 将稳定需求转化为新可复用能力组织 |

---

## 三、Agent 团队运转模型

### 元部门的三种角色

| 角色 | 谁做 | 做什么 |
|------|------|--------|
| **基础设施维护者** | 元部门自身 | M01 记忆管理、M02 身份定义、M03 通道治理 |
| **Agent 团队设计者** | 元部门自身 | M03 接入分析、M04 拆解、M05 路由设计、M08 编排设计 |
| **调度中心** | 元部门自身 | 派遣 Agent、接收结果、回流重派、综合交付 |

### Agent 团队的三种角色

| 角色 | 对应原子 | 隔离要求 |
|------|---------|---------|
| **执行 Agent** | M09 / M10 / M11 / M13 | 每个子任务一个独立实例 |
| **核验 Agent** | M12 | **不得**与执行 Agent 共享上下文（含内联产出） |
| **评估 Agent** | M06 | **不得**与执行/核验 Agent 共享上下文 |

**三权分立：执行、核验、评估必须由不同 Agent 实例完成，上下文完全隔离。**

---

## 三½、项目 Agent 体系

> 元部门的核心产出不是工作成果物，而是**项目 Agent 定义**——为特定项目创造的可复用执行工具。

### 三层工具体系

```
┌─────────────────────────────────────────────────┐
│  项目 Agent 定义                                   │  ← 元部门为项目创造的工具
│  存于项目 agents/ 文件夹，可复用、可迭代、可积累       │
├─────────────────────────────────────────────────┤
│  元部门 13 原子（codex-export/.codex/agents/）      │  ← 创造 Agent 的基础设施
│  角色模板，不直接产出工作成果                          │
├─────────────────────────────────────────────────┤
│  Codex subagent invocation                        │  ← 运行时执行机制
│  临时子进程，按项目 Agent 定义的指令执行                │
└─────────────────────────────────────────────────┘
```

> **Codex note**: bottom layer in canonical Claude Code is the `Agent tool` [Codex equivalent: subagent invocation]. Middle and top layers are platform-agnostic.

### 项目 Agent 与 13 原子的关系

| 概念 | 13 原子 | 项目 Agent |
|------|---------|-----------|
| **本质** | 抽象角色模板 | 项目专属执行工具 |
| **存储** | `codex-export/.codex/agents/M##-xxx.toml` | 项目 `agents/[名称]-Agent.md` |
| **创建者** | 架构设计者（人类） | 元部门（自动） |
| **生命周期** | 随架构演化，极少变动 | 随项目需求创建/复用/迭代 |
| **复用范围** | 跨项目通用 | 项目内复用 |
| **关系** | — | 每个项目 Agent 实例化一个或多个原子角色 |

### 项目 Agent 定义模板

```markdown
---
name: [Agent 名称]
atom: [M##-xxx]
type: project-agent
version: 1.0
created: [日期]
---

# [Agent 名称]

## 身份定位
[一句话角色定位]

**专业领域**：[该 Agent 的专业知识范围]
**决策权限**：[可自主决策的范围 vs 需上报的事项]

## 原子映射
[基于哪个/哪些 M## 原子角色，以及如何实例化该原子的能力]

## 输入契约

### 接受的输入
[具体格式、结构、必填字段]

### 输入验证规则
[何时拒绝输入、何时要求澄清、何时可接受不完整输入]

### 必要前置条件
[执行前必须完成的前序步骤/其他 Agent 产出]

## 输出契约

### 正常产出
[标准格式、结构、存放位置]

### 异常产出
[失败时的报告格式、回流条件、升级路径]

### 下游接收方
[哪些 Agent/流程步骤接收此输出]

## 执行规程
[命令式操作步骤——你**必须**按以下步骤执行：1. 2. 3. ...]

## 行为约束

### 你必须做什么
[命令式要求清单]

### 你禁止做什么
[显式禁止清单]

### 上下文隔离要求
[是否可引用其他 Agent 的产物、是否必须独立上下文执行]

### 约束表达原则 / Constraint Expression Principles
> 来源洞察：项目实战反思——原则性声明（"请不要X"）对 LLM 几乎无约束力，有效约束 = 白名单枚举 + 具体数值 + 独立核验。
> Source insight: Project reflection — principled statements ("please don't X") have near-zero enforcement on LLMs. Effective constraints = whitelist enumeration + concrete numeric values + independent verification.

Agent 定义中的约束**必须**优先使用白名单模式：
- ✅ 白名单（推荐）："Experience 栏目**只允许**写入以下内容：[枚举]"
- ❌ 黑名单（避免）："**不得**编造用户未提供的经历"
- ✅ 具体数值："头像尺寸 = 96px"
- ❌ 模糊声明："头像不要太大"

每条约束**必须**满足可验证性：M12 核验时能逐项对照检查。
无法逐项验证的约束 = 无效约束。

## 质量标准

### 量化验收条件
[具体可测量的通过/失败标准]

### SLOP 检测条件 / Anti-SLOP Checks
> 来源启发：外部治理系统中的领域特定套话检测——每个角色有其专属的空洞内容信号。
> Source: Domain-specific boilerplate detection — each role has its own hollow-content signals.

[该 Agent 角色特定的 AI 套话检测信号——至少 2 条，从下方 SLOP 信号表中根据原子映射选取]

| 原子角色 | 可选 SLOP 信号 |
|---------|---------------|
| M09-compose | 候选产物换名字还成立 = 无领域特异性 |
| M10-retrieve | 检索结果全标记为"相关"无排序 = 没做相关性排序 |
| M11-invoke | 调用报告全是"成功" = 没检查副作用 |
| M12-verify | 只有整体评级无断言列表 = 印象式核验 |
| M06-evaluate | 四维全给 4 分无差异 = 随手打分 |
| M07-synthesize | 综合结果 = 简单拼接 = 没做冲突消解 |
| M13-create | 新创能力与现有能力高度重叠 = 没做正交性检查 |
| 通用 (所有原子) | SLOP-09: Agent 定义换名为"Generic Agent"后仍成立 = 缺乏领域深度（Replaceability Test FAIL） |

**通用 SLOP 信号（适用于所有角色）：**
- Agent 定义中出现具体项目名称/路径硬编码 → 违反抽象纯度（五标准「可复用」失败）
- Agent 输入契约依赖具名上游 Agent 而非抽象契约 → 违反独立性（五标准「独立」失败）

### 核验方式
[由谁以何种方式检查——M12 核验 Agent / 自动化测试 / 人工审查]

## 技能装备

### 核心技能（你必须在相关场景中主动调用）
- `[skill-name]` — [一句话说明何时触发]

### 辅助技能（在遇到特定情况时可调用）
- `[skill-name]` — [触发条件]

### 调用方式
你**必须**通过 Skill 工具 [Codex equivalent: skill invocation] 调用技能：`Skill(skill="[skill-name]")`。
你**禁止**凭记忆复述技能内容——每次使用时**必须**实际调用 Skill 工具加载最新版本。

## 工具优先级

### 主力工具（执行核心职责时优先使用）
| 工具 | 用途 | 优先级 |
|------|------|--------|
| [Tool] | [在此 Agent 角色下的具体用途] | ★★★ |

### 辅助工具（在特定场景下使用）
| 工具 | 用途 | 触发场景 |
|------|------|---------|
| [Tool] | [用途] | [何时使用] |

### 禁用工具（你在此角色下禁止使用）
- [Tool] — [禁用理由]

### 使用原则
你**必须**优先使用主力工具完成核心任务。当主力工具无法满足需求时，方可使用辅助工具。
你**禁止**使用禁用工具列表中的工具，除非收到显式的例外指令。
```

### 填充规则

技能装备和工具优先级的填充规则：禁止手动猜测或凭经验填充——必须基于亲和表查表填充（见 §九 原子—技能亲和表 + 原子—工具优先级表）。

**抽象纯度规则（你必须遵循）：**
1. Agent 定义中**禁止**出现具体项目名称、具体文件路径、具体系统名称的硬编码引用
2. 输入契约中需要指定外部来源时，**必须**使用参数化占位符（如 `[源系统路径]`、`[参考文件]`）而非具体值
3. 输入验证规则中引用上游依赖时，**必须**基于抽象契约（如"符合诊断报告契约的报告"）而非具名 Agent（如"XX-Agent 的报告"）
4. 质量标准中的验收条件**必须**使用参数化表达（如"所有指定资产都已暴露"）而非具体数量（如"暴露了 13 个原子"）
5. **五标准快速自检**：创建完成后，对照「独立 Independent」和「可复用 Reusable」两项标准自检——若 Agent 定义换一个项目无法直接使用（需修改具体名称/路径），则违反抽象纯度

### Agent 命名规范 / Agent Naming Convention
> 来源洞察：项目 Agent 命名应体现原子映射关系，而非人类职业标签，以保持纯抽象性。

| 模式 | 示例 | 适用性 |
|------|------|--------|
| ✅ `[角色]-Agent` 基于功能抽象 | `Content-Composer-Agent`、`Governance-Verifier-Agent` | 推荐 |
| ⚠️ `M##-[角色]-Agent` 显式原子映射 | `M09-Content-Agent`、`M12-Verify-Agent` | 可选（当需要强调原子归属时） |
| ❌ 人类职业标签 | `Frontend-Engineer-Agent`、`Content-Writer-Agent` | 禁止——违反纯抽象原则 |

命名应体现功能本质而非领域身份。抽象命名 ≠ 含糊命名。

### 复用优先原则

路由时**先检查**项目 `agents/` 目录中已有的 Agent 定义：

1. 有匹配 → 直接复用，不重复创建
2. 无匹配 → 搜索全局资源（Codex 全局 skills/agents 路径、`references/` SKILL.md），匹配则通过 Skill tool [Codex equivalent: skill invocation] / M11-invoke 直接调用
3. 全局也无匹配 → 创建新 Agent 定义 → 核验 → 再用其执行
4. 部分匹配 → 更新 Agent 定义版本，记录变更

### 项目 Agent 生命周期

```
需求识别 → 创建 Agent 定义 → M12 核验定义质量 → 存入 agents/ → 按定义派遣执行 → 积累复用 → 迭代更新
```

### 视觉字符协议 / Visual Character Protocol

> 来源启发：外部纯 ASCII 视觉规约实践——视觉锚点的字符约束应跨平台兼容、可独立核验。
> Source inspiration: External pure-ASCII visual conventions — visual anchors must be cross-platform compatible and independently verifiable.

所有治理文档（13 原子、Project Agent 定义、命令、伤疤、记忆等）以及 Agent 输出**必须**遵守以下视觉字符白名单：

| 字符类 / Class | 允许的字符 / Allowed |
|---|---|
| 树形结构 / Tree | `│ ├ └ ─` |
| 符号标识 / Symbols | `⛔ ✅ ❌ ⚠️ 🔄 ⏸️ 🌟 🤔 🚫 📋 🎯 📦 📊 📁 🔒 🏗️ 🔄 🏥 🎉 🔐` |
| 列表标记 / List | `• ◦ ▸` |
| 任务状态 / Task Status | `[ ]` `[x]` |

**禁用 / Forbidden**：
- 超出此白名单的特殊 Unicode 装饰符号
- 过度审美字符（如花式分隔符、艺术字符变体）

**扩展规则 / Extension Rule**：如确需使用白名单外的字符，**必须**在文档头部显式声明扩展，并标注理由。

**应用范围 / Scope**：13 原子定义、Project Agent 定义、`.claude/` 与 `memory/`、`agents/` 下所有治理文档以及 Agent 的最终输出文档。对话过程中可宽松使用，但落盘文件**必须**符合白名单。

**理由 / Rationale**：跨平台兼容性（markdown、PDF、终端显示）、独立可核验性（M12 可逐字符对照检查）、避免视觉装饰对治理语义的稀释。

---

## 四、五条核心系统链路

所有链路中，元部门负责分析与调度（→），创造项目 Agent（⊕创），Agent 按定义执行（⊕执）。

### 主链 1：标准任务治理链

```
[元部门] M03 接入 → M04 拆解 → M05 路由（检查已有项目 Agent）→ M08 编排
                                                    ↓ 创造/复用项目 Agent
[元部门] ⊕创 在 agents/ 中创建 Agent 定义 → ⊕ M12 核验定义
                                                    ↓ 按定义派遣执行
[Agent]  ⊕执 M09/M10/M11 执行 → ⊕ M12 核验产物 → ⊕ M06 评估
                                                    ↓ 返回元部门
[元部门] M07 综合（或派遣综合 Agent）→ M03 交付
```

### 主链 2：候选生成治理链

```
[元部门] M04 拆解 → M05 路由 → 派遣构成 Agent
[Agent]  ⊕ M09 构成 → ⊕ M12 核验 → ⊕ M06 评估
[元部门] M07 综合 → 交付
```

### 主链 3：检索复用链

```
[元部门] M04/M05 分析路由 → 派遣检索 Agent
[Agent]  ⊕ M10 检索 → ⊕ M12/M06 核验评估
[元部门] M07 综合 → 交付
```

### 主链 4：外部能力接合链

```
[元部门] M05 路由 → 派遣调用 Agent
[Agent]  ⊕ M11 调用 → ⊕ M12 核验 → ⊕ M06 评估
[元部门] M07 综合 → 交付
```

### 主链 5：能力创造与制度化链

```
[元部门] M05/M10/M01 缺口发现 → 派遣创造 Agent
[Agent]  ⊕ M13 创造 → ⊕ M12 核验 → ⊕ M06 评估
[元部门] M01 沉淀 → M05 路由复用
```

---

## 五、五类关系网络

### 1. 支撑关系（垂直）

- **Layer 1 → Layer 2**：记忆锚点、身份边界、交互入口。没有基础层，编排层会变成短时临时组织。
- **Layer 2 → Layer 3**：任务结构、执行归属、推进秩序、结果裁决接口。没有编排层，Agent 团队会退化为散乱动作。
- **Layer 3 → Layer 2 / Layer 1**（反向反馈）：Agent 产物进入 M06 评估、M07 综合、M01 沉淀、M13 扩展。

### 2. 交接关系（横向）

每个原子把输出显式组织为下一个原子可接手的对象：

- M04 输出任务结构 → M05 / M08 接手（设计 Agent 团队）
- M05 输出执行归属 → 派遣 Agent 团队接手
- Agent 团队（M09/M10/M11）输出对象 → M12/M06 Agent 接手
- M12/M06 Agent 输出裁决结果 → 元部门接手（M08 回流 / M07 综合 / M03 交付）
- M13 Agent 输出新对象 → M12/M06 Agent 接手 → 元部门 M01 沉淀 / M05 路由

### 3. 制衡关系（对偶）

| 制衡对 | 张力 |
|--------|------|
| M09 ↔ M10 | 新构成 vs 已存在召回 |
| M10 ↔ M11 | 召回既有对象 vs 激活既有能力 |
| M06 ↔ M12 | 质量裁决 vs 成立核验 |
| M04 ↔ M08 | 任务结构 vs 推进秩序 |
| M09 ↔ M13 | 候选内容构成 vs 能力组织创造 |

### 4. 回流关系

| 失败类型 | 回流方式 |
|---------|---------|
| 评估不通过 | 元部门重新派遣对应执行 Agent |
| 核验失败 | 元部门重新派遣对应执行 Agent |
| 路由失配 | 元部门回到 M05 重新设计 Agent 归属 |
| 编排失衡 | 元部门回到 M08 重新编排 |
| 结构不可治理 | 元部门回到 M04 重新拆解 |
| 能力缺口稳定存在 | 元部门派遣 M13 创造 Agent |

### 5. 演化关系

Agent 执行经验 → 元部门 M01 沉淀 → 反复缺口 → 元部门 M05/M10 识别能力候选 → 派遣 M13 Agent 创造固化 → M12/M06 Agent 核验评估 → 元部门 M05 纳入路由复用 → M01 再沉淀

---

## 六、两条治理闭环

### 闭环 A：质量治理闭环

```
Agent 执行产物 → 派遣 M12 核验 Agent → 派遣 M06 评估 Agent → 不通过则重新派遣执行 Agent
```

避免"输出即完成"。

### 闭环 B：能力演化闭环

```
历史缺口 → 派遣 M13 创造 Agent → 派遣 M12 核验 Agent → 派遣 M06 评估 Agent → M01 沉淀 → M05 路由复用
```

让系统真正成长，而不是每次临时应对。

---

## 七、元部门复制链

```
模式积累/能力缺口/母体模板 → 派遣 M13 创造 Agent → M02 身份定义 → 派遣 M12 核验 Agent → 派遣 M06 评估 Agent → M01 沉淀 → M05 路由
```

元部门不是单一固定组织，而是：可派生、可特化、可分叉、可继承、可再纳入治理。

---

## 八、Codex 运行绑定 / Codex Runtime Binding

> **Source note**: This section in canonical Claude Code is titled "Claude Code 运行绑定". In the Codex mirror, Agent tool [Codex equivalent: subagent invocation] semantics are platform-mapped while the governance contract is unchanged.

### 核心原则

**元部门是「创造工具的工具」：(1) 维护基础设施 (2) 为项目创造 Agent 定义 (3) 按定义派遣执行。元部门不直接产出工作成果物。**

### Agent 委派规则

| 原子 | 运行绑定规则 |
|------|------------|
| M04 | 标准/重量拆解**必须**通过 Agent 工具 [Codex equivalent: subagent invocation] 创建独立子任务执行器 |
| M05 | 路由**必须**先检查项目 `agents/` 中已有 Agent 定义，匹配则复用；无匹配则创建新 Agent 定义后再派遣 |
| M06 | 评估**必须**由独立 Agent 完成，且与执行/核验上下文隔离 |
| M07 | 综合来源 ≥ 3 个时**必须**委派独立 Agent；跨批次并行产物汇合**必须**委派 Agent |
| M08 | 并行**必须**体现为单条消息内多个 Agent 执行实体，单批并发上限 5 个 |
| M09 | 非微型任务**必须**由独立 Agent 执行构成；多候选（≥3）**必须**委派 |
| M10 | 跨 ≥ 2 来源检索**必须**委派独立 Agent；跨项目检索**必须**委派 |
| M11 | 非微型调用**必须**由独立 Agent 执行；涉及外部系统/API 调用**必须**委派 |
| M12 | 核验者**永远不得**与生产者共享同一执行上下文（无论生产行为是否由独立 Agent 完成） |
| M13 | Skill 级创造**必须**由独立 Agent 执行；Agent/Meta-Department 级**必须**多 Agent 协作 |

### 微型任务例外

**仅在以下条件全部满足时**，允许元部门不构建 Agent 团队而直接执行：

- 单一明确操作，无需拆解（如：改一个拼写错误、添加一行注释）
- 无需核验或评估（产出不影响其他组件）
- 文件 ≤ 1，变更 ≤ 10 行

**有任何疑问即升级为标准模式，构建 Agent 团队执行。**

### 并行度约束

单批并发 Agent ≤ 5，超出则分批执行，批次间设汇合检查点。

---

## 九、Skill 融合映射

| 外部能力 | 融合至 | 融合方式 |
|---------|--------|---------|
| `find-skills` | M05 路由元 + M10 检索元 | 路由元在能力缺口时触发技能发现；检索元在技能库中执行搜索匹配 |
| `writing-skills` | M13 创造元 | 全生命周期技能工程：创建 → 评估 → 迭代 → 打包 |
| `awesome-claude-prompts` | M09 构成元 + M02 身份元 + M10 检索元 | 提示词框架融合至构成元；身份方法论融合至身份元；模板库注册为检索元参考资源 |

### 原子—技能亲和表（Atom-Skill Affinity Table）

M13 创建项目 Agent 时**必须**查此表自动填充「技能装备」section。

| 原子 | 核心技能 (Core) — 必须在相关场景中主动调用 | 辅助技能 (Auxiliary) — 遇到特定情况时可调用 |
|------|------------------------------------------|-------------------------------------------|
| M09-compose | `brainstorming`, `verification-before-completion` | `writing-plans` |
| M10-retrieve | `systematic-debugging` (Phase 1-2 方法论) | `verification-before-completion` |
| M11-invoke | `dispatching-parallel-agents` | `using-git-worktrees`, `finishing-a-development-branch` |
| M12-verify | `verification-before-completion`, `requesting-code-review` | `systematic-debugging`, `test-driven-development` |
| M06-evaluate | `verification-before-completion` | `requesting-code-review` |
| M07-synthesize | （无） | `executing-plans` |
| M13-create | `writing-skills`, `writing-plans` | `brainstorming`, `test-driven-development` |

多原子映射规则：若 Agent 映射多个原子，核心技能取**并集**，辅助技能取**并集**（去重）。

### 原子—工具优先级表（Atom-Tool Priority Table）

M13 创建项目 Agent 时**必须**查此表自动填充「工具优先级」section。

| 原子 | 主力工具 ★★★ | 辅助工具 ★★ | 禁用工具 |
|------|-------------|------------|---------|
| M09-compose | Write, Edit, Read | Glob, Grep, Bash, Skill | （无） |
| M10-retrieve | Read, Grep, Glob | Bash, WebFetch, WebSearch | Write, Edit |
| M11-invoke | Bash, Skill, WebFetch | Read, Grep | （无） |
| M12-verify | Read, Bash, Grep | Glob, WebFetch | **Write, Edit** |
| M06-evaluate | Read | Grep, Glob | **Write, Edit, Bash** |
| M07-synthesize | Write, Read | Grep, Glob | Bash |
| M13-create | Write, Read, Skill | Grep, Glob, Bash | （无） |

多原子映射规则：主力工具取**并集**，辅助工具取**并集**，禁用工具取**交集**（仅当所有映射原子都禁用某工具时才禁用）。

**⛔ 三权分立结构执行**：M12-verify 和 M06-evaluate 的禁用工具列表中**必须**包含 Write 和 Edit——核验者和评估者禁止修改被检查的产物。

### 任务关键词→技能追加表（Task Keyword Augmentation Table）

派遣时（Phase C）扫描子任务描述关键词，追加匹配的额外技能。仅**追加**，不替换 Agent 定义中的核心/辅助技能。

| 关键词信号 | 追加技能 |
|-----------|---------|
| 调试 / debug / bug / 修复 | + `systematic-debugging` |
| 测试 / test / TDD | + `test-driven-development` |
| 代码审查 / review / PR | + `requesting-code-review` |
| 并行 / parallel / 批量 | + `dispatching-parallel-agents` |
| 计划 / plan / 规划 | + `writing-plans`, + `executing-plans` |
| 分支 / branch / merge | + `using-git-worktrees`, + `finishing-a-development-branch` |
| 创建技能 / skill | + `writing-skills` |
| 头脑风暴 / brainstorm / 设计 | + `brainstorming` |
| 完成 / 交付 / 收尾 | + `verification-before-completion` |

---

## 十、Agent 创建机制

M13 具备**五级创造能力**：

| 级别 | 创建类型 | 存储位置 | 触发条件 | 门控要求 |
|------|---------|---------|---------|---------|
| **L0** | 项目 Agent | 项目 `agents/` | 每次 `/meta` 调用时按需创建 | 无门控，是元部门标准工作产出 |
| **L1** | Skill | 元部门内 | 能力缺口 + 2次验证通过 + I/O 契约明确 | 最小可复用条件 |
| **L2** | Agent（原子级） | `codex-export/.codex/agents/` | 结构性缺口（≥3次同类需求）+ 需要独立身份/状态/进化 | 五道门控（缺口→Skill不足→层归属→正交性→人类确认）|
| **L3** | Meta-Department | 独立目录 | 领域特化需求 + 完整13原子实例化 | 谱系追踪 + 治理同步 + 独立演化 |
| **L4** | Governance-Aware Replication | 独立目录 | 已有元部门需要在新环境中复制并保持治理同步 | 谱系追踪 + 治理版本同步 + 独立演化 + 停止规则体系 |

**L0 项目 Agent 是元部门最常见的创造行为**——每次处理任务时，元部门先在项目 `agents/` 中创造或复用 Agent 定义，再按定义派遣执行。这体现了「创造工具的工具」的核心哲学。

架构膨胀安全阀：原子总数超过 18 时触发架构审查。

---

## 十一、设计原则

1. **创造工具的工具**：元部门的核心产出是项目 Agent 定义（存于项目 `agents/`），不是工作成果物。先创造 Agent，再用 Agent 做事
2. **不可拆分性**：13 元中任何一个若再拆分，将丧失独立语义完整性
3. **纯抽象性**：所有描述不含具象领域词汇，可复用于任意业务域
4. **三权分立**：执行 Agent、核验 Agent、评估 Agent 必须上下文隔离
5. **自我进化**：每个元内建基于反馈的自适应机制
6. **正交性**：各元职责边界清晰，无功能重叠
7. **治理优先**：每个原子同时回答"我是什么、我不是什么、我如何被治理、我如何演化"
8. **可演化架构**：M13 具备创造新原子与新元部门的能力，使框架本身可生长

---

## 十二、原子健康诊断工具 / Atom Health Diagnostics

> 借鉴自 Meta_Kim 五标准四死法，以本元部门术语重新表述。用于诊断原子或项目 Agent 的健康度，以及识别架构腐化信号。

### 五标准检查表 / Five-Standard Checklist

每个原子（13 atoms）和项目 Agent（`agents/`）都应通过以下五项健康检查：

| 标准 Standard | 检查问题 Check Question | 不通过信号 Failure Signal |
|--------------|----------------------|------------------------|
| **独立 / Independent** | 这个原子/Agent 能否脱离其他原子单独被理解和调用？ | 解释时必须引用另一个原子才能说清楚 |
| **足够小 / Minimal** | 再拆分后的子部分是否仍然有独立语义？ | 拆出来的子部分无法单独命名或定义 |
| **边界清晰 / Bounded** | 能否一句话说出"只管什么"和"不碰什么"？ | 存在"也可以做X"这样的模糊地带 |
| **可替换 / Replaceable** | 换掉这个原子/Agent 后系统是否仍能运行？ | 多个其他原子硬依赖此原子的内部实现 |
| **可复用 / Reusable** | 这个原子/Agent 在另一个项目中是否有意义？ | 高度绑定特定项目的特定场景 |

**通过标准**：5/5 全部通过 = 健康；4/5 = 需关注；≤3/5 = 需立即修复。

### 四死法诊断 / Four Anti-Pattern Diagnostics

用于识别架构腐化的四种典型反模式：

| 反模式 Anti-Pattern | 症状 Symptom | 修复方向 Remedy |
|--------------------|-------------|----------------|
| **一锅炖 / Kitchen Sink** | 原子/Agent 定义中出现 ≥3 个不相关的核心功能 | 拆分为多个正交原子/Agent |
| **碎成渣 / Over-Fragmentation** | 两个原子/Agent 总是被一起调用且从不单独使用 | 合并为一个原子/Agent |
| **只执行无治理 / Execution Without Governance** | 执行后无 M12 核验 / M06 评估环节 | 补全治理尾链（M12 → M06） |
| **只追结果无结构 / Results Without Structure** | 方案可复制但无人知道为什么有效 | 补全进化落盘（Evolution Writeback → M01 沉淀） |

### PRIN-01~05 + Replaceability Test 健康诊断扩展

> 来源启发：Meta_Kim PRIN 原则 + Replaceability Test——给 §十二 五标准检查表配套一组**操作性强**的执行版核验工具。

#### PRIN 检查清单（适用于原子 + Project Agent）

| 原则 / Principle | 检查问题 / Check Question |
|---|---|
| PRIN-01 Configurable | 是否存在硬编码值（具体路径、特定用户名、固定数字阈值无参数化）？ |
| PRIN-02 Single Source | 同一规则是否在多处独立定义（导致漂移风险）？ |
| PRIN-03 Layering | 是否存在越层调用（如执行层原子直接修改基础层文件）？ |
| PRIN-04 Decoupling | 是否依赖具体 Agent 名而非抽象契约？ |
| PRIN-05 i18n | 文档是否符合双语中英风格？ |

#### Replaceability Test（适用于 Project Agent）

执行步骤：
1. 把 Project Agent 的名称替换为 "Generic Agent"
2. 重新阅读定义全文
3. 评估：
   - 定义仍然有意义、可执行 → **FAIL**（违反"独立"和"可复用"标准）
   - 定义变得空洞、需要 Agent 名才能理解 → **PASS**（领域深度足够）

#### 使用场景
- M12-verify 在核验 Project Agent 定义时（Phase B3）必须执行 PRIN 检查 + Replaceability Test
- 架构自检（`/meta` 诊断类任务）作为系统性诊断框架的扩展

### 时间表达健康检查 / Time Expression Health Check

> 来源启发：外部洁癖治理实践——把抽象原则转化为一条独立 Agent 可执行的具体测试。
> Source inspiration: External hygiene-governance practice — turning abstract principles into a concrete test runnable by an independent Agent.

**诊断项 / Diagnostic Item**：所有治理文件（`memory/`、`.claude/`）的内容**必须**使用绝对日期 YYYY-MM-DD（如 `2026-04-30`），**禁止**使用相对时间词。

**检测命令 / Detection Command**：
```
grep -nE "今天|昨天|刚刚|最近|上周|today|yesterday|recently|last week" memory/ .claude/
```

**判定原则 / Judgment Rule**：
- 发现匹配 → 诊断 **FAIL**，必须修正为绝对日期表达
- 例外说明：对话过程中可使用相对时间；治理产出物（落盘文件）中**禁止**

**应用范围 / Scope**：所有治理文件，包括 `memory/`（记忆与伤疤）、`.claude/`（原子定义、命令、Agent 注册表）等需要跨会话保持语义稳定的文件。

**理由 / Rationale**：跨会话记忆最易腐烂的是相对时间表达——三十天后"最近"已无明确所指。绝对日期保障文档的跨时间可读性与独立可核验性。

### 反元叙事黑名单 / Anti-Meta-Narrative Blacklist

> 来源启发：外部 Anti-SLOP 治理实践——"自我宣告深度"反而戳破深度，真正的深度由具体证据体现。
> Source inspiration: External Anti-SLOP practice — self-announcing depth undermines depth; real depth is shown by concrete evidence.

**诊断项 / Diagnostic Item**：检测被审查的治理文档/Agent 输出中是否包含「自我宣告深度」的元叙事词汇。

**黑名单词 / Blacklist Vocabulary**：
- 「再深入一层」、「最深的一层」、「更进一步」、「深度剖析」
- 「让我们深入分析…」、「下面我将进一步…」
- 「核心本质是…」（无具体证据支撑时）

**检测命令 / Detection Command**：
```
grep -nE "再深入一层|最深的一层|更进一步|深度剖析|让我们深入" .claude/ memory/ agents/
```

**判定原则 / Judgment Rule**：
- 发现匹配 → 标注**疑似 SLOP-11（元叙事自标深度）**，需替换为具体证据或删除
- 「说『我要深入了』反而把深入戳破了」——真正的深度由下一句的具体内容自然显出，而非由前置宣告造出
- 与 SLOP-09（Replaceability Test）/ Replaceability Test 同级的横切诊断项

**应用范围 / Scope**：
- 13 原子定义、Project Agent 定义、治理记忆、伤疤文档
- M12-verify 核验阶段、M06-evaluate 评估阶段均可调用此诊断

**修复方向 / Remedy**：以具体观察、数据、案例替代抽象的"深度"宣告。不写"再深入一层"，直接给出第二层的具体内容。

### 使用场景 / When to Apply

1. **架构自检**：`/meta` 诊断类任务时，作为系统性诊断框架
2. **新原子准入**：M13 创建新原子（L2）时，五标准作为准入检查——不通过则不得创建
3. **Agent 定义核验**：M12 核验项目 Agent 定义（Phase B3）时，五标准 + 四死法作为参考标准
4. **架构演化审查**：原子总数接近 18 时（架构膨胀安全阀），用四死法诊断是否存在过度碎片化

---

## 十三、跨项目治理 / Cross-Project Governance

> 当元部门部署为全局（`~/.claude/` 在 Claude Code 主源；Codex 端对应 `~/.codex/`）时，以下机制确保跨项目经验的有效流通与安全隔离。

### 全局伤疤池 / Global Scar Pool

全局路径 `~/.claude/scars/` 存储跨项目普适性伤疤（Codex 用户在 `~/.codex/scars/` 自建等价目录）。每个项目的 C2 伤疤审计步骤同时扫描项目 `memory/scars/` 和全局伤疤池。伤疤的全局化由 D3 进化落盘阶段判定（不含项目特定上下文 → 全局化）。

### 全局进化门控 / Global Evolution Gating

任何对 `~/.claude/` 下文件的修改必须经用户确认。D3 进化写回区分项目级（直接写入项目目录）与全局级（需用户确认后写入 `~/.claude/`）。

### 跨项目 Agent 发现 / Cross-Project Agent Discovery

全局 `~/.claude/agent-registry/` 存储各项目注册的可复用 Agent 摘要（`.yml` 格式）。M05 在 Step 2.5 全局资源搜索中扫描此注册表，发现匹配后复制到当前项目 `agents/` 并标记来源。注册条件：Agent 评估 ≥ 16/20 且具有跨项目复用价值。Codex 用户需在 Codex 全局目录建立等价的注册表机制。

### 全局 vs 项目级资产对照 / Global vs Project-Level Assets

| 资产类型 | 全局路径 (`~/.claude/`) | 项目路径 | 说明 |
|---------|----------------------|---------|------|
| 原子定义 | `agents/M##-xxx.md` | — | 全局共享，跨项目通用 |
| 治理链 | `commands/meta.md` | — | 全局共享 |
| 项目 Agent | — | `agents/*.md` | 项目独立，不自动共享 |
| Agent 注册表 | `agent-registry/*.yml` | — | 项目 Agent 的跨项目发现索引 |
| 伤疤 | `scars/*.md` | `memory/scars/*.md` | 全局=普适性伤疤，项目=含项目上下文的伤疤 |
| 记忆 | — | `memory/` | 项目独立，不跨项目 |
| MCP server | `scripts/mcp/` | — | 全局服务（Codex 端需另行适配） |

---

## 十四、统一术语约束

| 术语 | 归属原子 | 禁止混用 |
|------|---------|---------|
| Candidate / 候选 | M09 | 不要把 M10 检索结果叫 candidate |
| Existing Object / 既有对象 | M10 | 不要把能力也叫 existing object |
| Existing Capability / 既有能力 | M11 | 不要把可召回对象和可调用能力混为一个词 |
| Evaluate / 评估 | M06 | 质量裁决，不判断真实性 |
| Verify / 核验 | M12 | 成立性检查，不判断质量优劣 |
| Decompose / 拆解 | M04 | 只管"拆成什么"，不管"谁做""何时做" |
| Sequence / 编排 | M08 | 只管推进秩序，不管任务本体 |
| Synthesize / 综合 | M07 | 只整合结果，不吞并其他原子职责 |
| Created Capability / 新创能力 | M13 | 不要把单次输出升级叫 created capability |
| Agent 团队 | 元部门整体 | 元部门派遣的独立执行实体集合，不是元部门自身 |
| 项目 Agent / Project Agent | 元部门产出 | 元部门为项目创造的规范化 Agent 定义文件，存于项目 `agents/` 目录 |
| 13 原子 | 元部门基础设施 | 抽象角色模板，不是项目 Agent，不直接产出工作成果 |
