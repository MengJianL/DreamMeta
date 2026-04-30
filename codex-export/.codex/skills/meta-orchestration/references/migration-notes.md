# Migration Notes: Claude Code → Codex / 迁移说明

> **Source / 来源**: This file accompanies the DreamMeta Codex mirror under `codex-export/.codex/skills/meta-orchestration/references/`. The canonical DreamMeta home is Claude Code (`.claude/`); this Codex projection is generated for portability.
> **Canonical home / 正典之家**: Long-term edits belong in `.claude/agents/`, `.claude/agents/CLAUDE.md`, and `.claude/commands/meta.md`. The Codex mirror in `codex-export/` is regenerated from those sources.

---

## 1. 核心定位 / Core Positioning

- DreamMeta 的 canonical home 是 Claude Code (`.claude/`)
- Codex 版是 mirror（同步而非主源）
- 改进应先在 Claude Code 端落地，然后回流到 Codex mirror

**Why this matters / 为何如此**：DreamMeta 是一个 Meta-Department 治理体系，它的 13 原子定义、命令链、架构索引共同构成正典。Codex 版本只承载同样的治理逻辑在 Codex 平台上的运行投影；治理逻辑（八条铁律 / 三层引力 / 三权分立 / 进化落盘）跨平台一致，只有派遣机制与工具语法需平台适配。

---

## 2. 目录结构对照 / Directory Mapping

| Claude Code | Codex |
|---|---|
| `.claude/agents/M##-*.md` | `codex-export/.codex/agents/M##-*.toml` |
| `.claude/agents/CLAUDE.md` | `codex-export/.codex/skills/meta-orchestration/references/architecture-index.md` |
| `.claude/commands/meta.md` | `codex-export/.codex/skills/meta-orchestration/SKILL.md` |
| `agents/*-Agent.md` | `codex-export/.codex/agents/project/*-Agent.toml` |
| `memory/` | (项目特定，不导出 / project-specific, not exported) |
| `.claude/skills/` | (Codex 全局 skills 由 Codex 用户自管 / Codex global skills are user-maintained) |
| `~/.claude/scars/` | (Codex 用户在 `~/.codex/scars/` 自建等价目录 / equivalent set up by Codex user) |
| `~/.claude/agents/` | `~/.codex/agents/` |
| `~/.claude/agent-registry/` | (Codex 用户自建跨项目 Agent 索引 / user-maintained cross-project Agent index) |

**Note / 注意**：13 原子定义（`M01-memory.md` ~ `M13-create.md`）**不重复**导出到 codex-export。它们在 `.claude/agents/` 保持权威，Codex 用户可选择按需手动转换为 `.toml` 格式以获得 Codex 原生 subagent 集成。

---

## 3. 概念语法对照 / Concept Syntax Mapping

| Claude Code | Codex Equivalent |
|---|---|
| `Agent tool`（派遣 subagent） | Codex 内置 subagent invocation 机制 / Codex-native subagent invocation |
| `Skill tool`（调用 skill） | Codex skill invocation；frontmatter 中 `trigger` 字段触发 |
| `AskUserQuestion` 工具 | Codex 用户提问机制 / Codex's native user-prompt mechanism |
| `Read / Write / Edit / Glob / Grep / Bash` 工具 | Codex 同名工具 / Codex tools with identical names |
| `~/.claude/scars/` 全局伤疤池 | (Codex 用户可在 `~/.codex/` 下建立等价目录 / user can create equivalent path under `~/.codex/`) |
| `~/.claude/agents/` 全局原子 | `~/.codex/agents/` |
| `~/.claude/scripts/mcp/` MCP 服务 | 需另行配置 Codex-side MCP adapter / requires Codex-side MCP adapter |

**Behavioral contract / 行为契约一致性**：
尽管表面工具名不同，治理契约保持一致：派遣 subagent → 上下文隔离 → 三权分立 → 结构化报告。Codex 平台变体只影响调用语法，不影响治理结构。

---

## 4. 转移步骤 / Transfer Steps

1. 把 `codex-export/` 整个文件夹拷贝到 Codex 工作目录
2. 重命名 `codex-export/` 为 `.codex/`（或保持 `codex-export/` 作为 staging）
3. 把 `codex-export/AGENTS.md` 复制到 Codex 项目根目录作为 `AGENTS.md`
4. 把 `codex-export/.codex/agents/M##-*.toml` 复制到 Codex 全局或项目 agents 目录（如选择 TOML 转换路径）
5. 把 `codex-export/.codex/skills/meta-orchestration/` 复制到 Codex skills 目录
6. 验证：在 Codex 中执行触发关键词（`元部门` / `13 原子` / `治理链`），确认 `meta-orchestration` skill 被激活

**Smoke test / 烟雾测试**：
Codex 中输入"用 13 原子治理链处理一个微型任务：修复一个拼写错误"，验证：
- meta-orchestration skill 是否成功激活
- A2 微型判定路径是否正确触发（豁免治理链）
- 后置摘要是否在 Edit 工具调用成功后才产出（Post-Modify Summary Discipline）

---

## 5. 已知差异 / Known Differences

- MCP server (`dreammeta-runtime`) 的 Codex 集成方式与 Claude Code 不同，需另行配置
- Skill tool 调用语法在 Codex 下需调整（具体语法参考 Codex 官方文档）
- Hook 系统 (`settings.json`) Codex 端无直接等价物——治理性 hook（如 `stop-completion-guard`）需以 SKILL.md 内嵌规则形式表达
- TOML 格式 agents 在 Codex 中通过 `name` 字段被路由识别，Markdown 内容嵌入 `developer_instructions` 字符串
- MCP 触发 trigger 字段在 SKILL.md frontmatter 中，与 Claude Code 的 trigger 表达可能在语义边界上略有差异
- Codex 跨项目 Agent 注册表（对应 `~/.claude/agent-registry/`）需 Codex 用户自建

---

## 6. 回流原则 / Backflow Principle

> 在 Codex 端发现的改进，应遵循以下回流路径 / Improvements observed on Codex side should follow this backflow path:

1. 在 Codex 端调试验证机制 / debug and validate the mechanism on Codex side
2. 把改进**先**转回 Claude Code 的 `.claude/`（canonical） / port the improvement back to Claude Code `.claude/` first
3. 用 `cp` 同步项目→全局 `~/.claude/` / sync from project to global `~/.claude/` via `cp`
4. 重新生成 `codex-export/` 镜像 / regenerate the `codex-export/` mirror

**Why backflow first to canonical / 为何先回流到正典**：
直接在 Codex mirror 改动会在下一次镜像同步时被覆盖。canonical 优先原则确保治理改进沉淀在主源，所有 runtime 投影都从主源衍生。

---

## 7. 限制与排除 / Limits and Exclusions

- DreamMeta 的 `memory/` 目录是项目特定，不应跨项目转移 / project-specific, not transferable across projects
- `references/` 是参考资料，不导出（Codex 用户可独立 git clone 这些参考项目） / reference materials are not exported; Codex users can clone them independently
- DreamMeta 全局部署相关（`~/.claude/scars/`、`~/.claude/agent-registry/`）在 Codex 中需对应自建 / global-deployment paths must be re-established under `~/.codex/` by the user
- 项目 `agents/` 文件夹**不**通过 codex-export 携带——每次 Codex 部署从空 `agents/` 开始，由 `/meta` 调用按需生成项目专属 Agent 定义 / project `agents/` is **not** carried by codex-export; each Codex deployment starts with an empty `agents/` and accumulates project Agent definitions on demand
- 项目记忆（伤疤、模式、能力缺口）跨项目不应共享——这是治理设计的核心原则之一 / project memories should not cross-pollinate — this is a core governance design principle

**One-line summary / 一句话总结**：框架可移动，经验不可移动 / the framework travels, the experience does not.
