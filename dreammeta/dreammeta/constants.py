"""Static definitions for the Meta-Department architecture."""

from __future__ import annotations

# Layer definitions: layer_number -> (chinese_name, english_name)
LAYERS: dict[int, tuple[str, str]] = {
    1: ("基础设施元", "Foundation"),
    2: ("编排元", "Orchestration"),
    3: ("执行元", "Execution"),
}

# Agent ID -> (chinese_name, english_name, layer, operation_or_none)
AGENT_REGISTRY: dict[str, tuple[str, str, int, str | None]] = {
    "M01": ("记忆元", "Memory Meta", 1, None),
    "M02": ("身份元", "Identity Meta", 1, None),
    "M03": ("通信元", "Channel Meta", 1, None),
    "M04": ("分解元", "Decompose Meta", 2, None),
    "M05": ("路由元", "Route Meta", 2, None),
    "M06": ("评估元", "Evaluate Meta", 2, None),
    "M07": ("聚合元", "Synthesize Meta", 2, None),
    "M08": ("序列元", "Sequence Meta", 2, None),
    "M09": ("构成元", "Compose", 3, "构"),
    "M10": ("检索元", "Retrieve Meta", 3, "查"),
    "M11": ("调用元", "Invoke Meta", 3, "用"),
    "M12": ("验证元", "Verify Meta", 3, "检"),
    "M13": ("创造元", "Create Meta", 3, "创"),
}

# Agents grouped by layer for display
LAYER_AGENTS: dict[int, list[str]] = {
    1: ["M01", "M02", "M03"],
    2: ["M04", "M05", "M06", "M07", "M08"],
    3: ["M09", "M10", "M11", "M12", "M13"],
}

# Standard section headings in agent files (keyword -> canonical key).
# Includes both old Chinese-only and new bilingual heading patterns.
SECTION_MAP: dict[str, str] = {
    # Layer
    "Layer": "layer",
    "层级": "layer",
    # Identity
    "Identity": "identity",
    "身份定位": "identity",
    "身份": "identity",
    # Existential Role
    "Existential Role": "existential_role",
    "存在意义": "existential_role",
    # Core Function
    "Core Function": "core_functions",
    "核心功能": "core_functions",
    "核心职能": "core_functions",
    # Operational Boundary
    "Operational Boundary": "operational_boundary",
    "操作边界": "operational_boundary",
    # Trigger Conditions
    "Trigger Conditions": "trigger_conditions",
    "触发条件": "trigger_conditions",
    # Working Modes
    "Working Modes": "working_modes",
    "工作模式": "working_modes",
    # Input Contract
    "Input Contract": "input_contract",
    "输入契约": "input_contract",
    # Output Contract
    "Output Contract": "output_contract",
    "输出契约": "output_contract",
    # Decision Principles
    "Decision Principles": "decision_principles",
    "决策原则": "decision_principles",
    # Failure Modes
    "Failure Modes": "failure_modes",
    "失效模式": "failure_modes",
    # Quality Criteria
    "Quality Criteria": "quality_criteria",
    "质量标准": "quality_criteria",
    # Neighbor Interaction
    "Interaction with Neighbor Atoms": "neighbor_interaction",
    "邻接交互": "neighbor_interaction",
    "与相邻原子的交互": "neighbor_interaction",
    # Runtime Binding
    "Runtime Binding": "runtime_binding",
    "运行时绑定": "runtime_binding",
    # Self-Evolution
    "Self-Evolution Mechanism": "self_evolution",
    "自演化机制": "self_evolution",
    "自我进化机制": "self_evolution",
    # Minimal Governance Statement
    "Minimal Governance Statement": "governance_statement",
    "最小治理声明": "governance_statement",
    # Legacy headings (old template compatibility)
    "思维模式": "thinking_mode",
    "行为约束": "behavior_constraints",
    "输出规范": "output_spec",
}
