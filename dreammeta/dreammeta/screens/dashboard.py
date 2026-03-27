"""Dashboard page — Meta-Department overview with 3-layer gravity graph."""

from __future__ import annotations

import re

from PySide6.QtCore import Qt, QUrl, QTimer, QFileSystemWatcher
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import (
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from dreammeta.config import DreamMetaConfig
from dreammeta.constants import AGENT_REGISTRY, LAYER_AGENTS, LAYERS
from dreammeta.data.agent_parser import parse_all_agents
from dreammeta.data.models import Agent


# ---------------------------------------------------------------------------
# Health scoring
# ---------------------------------------------------------------------------

_HEALTH_KEYS = [
    "identity",
    "existential_role",
    "core_functions",
    "operational_boundary",
    "decision_principles",
    "failure_modes",
    "runtime_binding",
    "self_evolution",
]

_HEALTH_MAX = len(_HEALTH_KEYS)  # 8

# Human-readable section names for tooltips
_SECTION_DISPLAY_NAMES: dict[str, str] = {
    "identity": "身份定位",
    "existential_role": "存在意义",
    "core_functions": "核心功能",
    "operational_boundary": "操作边界",
    "decision_principles": "决策原则",
    "failure_modes": "失效模式",
    "runtime_binding": "运行时绑定",
    "self_evolution": "自演化机制",
}


def _health_score(agent: Agent) -> int:
    """Return 0-N health score based on which key sections are present."""
    score = 0
    for key in _HEALTH_KEYS:
        if key in agent.sections:
            score += 1
    return score


def _missing_sections(agent: Agent) -> list[str]:
    """Return list of human-readable names for missing sections."""
    missing = []
    for key in _HEALTH_KEYS:
        if key not in agent.sections:
            missing.append(_SECTION_DISPLAY_NAMES[key])
    return missing


def _health_indicator(score: int) -> str:
    """Return a suffix string for the button label based on health score."""
    if score >= _HEALTH_MAX:
        return ""  # healthy — clean label
    if score >= _HEALTH_MAX - 2:
        return " \u26a0"  # warning
    return " \u2717"  # error


# ---------------------------------------------------------------------------
# Markdown-to-HTML converter
# ---------------------------------------------------------------------------

_RE_BOLD = re.compile(r"\*\*(.+?)\*\*")
_RE_INLINE_CODE = re.compile(r"`([^`]+)`")


def _inline(text: str) -> str:
    """Process inline markdown: **bold** and `code`."""
    text = _RE_BOLD.sub(r"<b>\1</b>", text)
    text = _RE_INLINE_CODE.sub(r"<code>\1</code>", text)
    return text


def _convert_md_block(content: str) -> str:
    """Convert a markdown content block to HTML.

    Handles: headings (###), bold, inline code, ordered lists, unordered
    lists (including nested), blockquotes, fenced code blocks, and
    paragraph breaks.  Regex-based — intentionally not a full parser.
    """
    lines = content.split("\n")
    out: list[str] = []

    # State trackers
    in_ul = False
    in_nested_ul = False
    in_ol = False
    in_code_block = False
    in_blockquote = False
    code_lines: list[str] = []

    def _close_ul() -> None:
        nonlocal in_ul, in_nested_ul
        if in_nested_ul:
            out.append("</ul>")
            in_nested_ul = False
        if in_ul:
            out.append("</ul>")
            in_ul = False

    def _close_ol() -> None:
        nonlocal in_ol
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def _close_blockquote() -> None:
        nonlocal in_blockquote
        if in_blockquote:
            out.append("</blockquote>")
            in_blockquote = False

    def _close_lists() -> None:
        _close_ul()
        _close_ol()

    for line in lines:
        stripped = line.strip()

        # --- fenced code block ---
        if stripped.startswith("```"):
            if in_code_block:
                # closing fence
                out.append("<pre>" + "\n".join(code_lines) + "</pre>")
                code_lines.clear()
                in_code_block = False
            else:
                _close_lists()
                _close_blockquote()
                in_code_block = True
            continue
        if in_code_block:
            code_lines.append(line)
            continue

        # --- sub-heading ### ---
        if stripped.startswith("### "):
            _close_lists()
            _close_blockquote()
            out.append(f"<h3>{_inline(stripped[4:])}</h3>")
            continue

        # --- blockquote ---
        if stripped.startswith("> "):
            _close_lists()
            if not in_blockquote:
                out.append("<blockquote>")
                in_blockquote = True
            out.append(f"<p>{_inline(stripped[2:])}</p>")
            continue
        else:
            _close_blockquote()

        # --- ordered list ---
        ol_match = re.match(r"^(\d+)\.\s+(.+)$", stripped)
        if ol_match:
            _close_ul()
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{_inline(ol_match.group(2))}</li>")
            continue

        # --- nested unordered list (2+ spaces then - or *) ---
        nested_match = re.match(r"^(\s{2,})[-*]\s+(.+)$", line)
        if nested_match:
            _close_ol()
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            if not in_nested_ul:
                out.append("<ul>")
                in_nested_ul = True
            out.append(f"<li>{_inline(nested_match.group(2))}</li>")
            continue

        # --- top-level unordered list ---
        if stripped.startswith("- ") or stripped.startswith("* "):
            _close_ol()
            if in_nested_ul:
                out.append("</ul>")
                in_nested_ul = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{_inline(stripped[2:])}</li>")
            continue

        # --- not a list line: close any open lists ---
        _close_lists()

        # --- empty line = paragraph break ---
        if not stripped:
            out.append("<br/>")
            continue

        # --- plain paragraph ---
        out.append(f"<p>{_inline(stripped)}</p>")

    # Close any remaining open structures
    if in_code_block:
        out.append("<pre>" + "\n".join(code_lines) + "</pre>")
    _close_lists()
    _close_blockquote()

    return "\n".join(out)


def _agent_to_html(agent: Agent) -> str:
    """Convert an Agent model to styled HTML for QTextBrowser."""
    layer_class = f"layer-{agent.layer}"
    parts = [
        f"<h1>{agent.full_title}</h1>",
        f"<p><b>Layer</b>: <span class='{layer_class}'>{agent.layer_name}</span></p>",
    ]
    if agent.operation:
        parts.append(f"<p><b>Operation</b>: {agent.operation}</p>")

    # Health badge
    score = _health_score(agent)
    parts.append(
        f"<p><b>Health</b>: {score}/{_HEALTH_MAX}"
        f"{' \u2714' if score == _HEALTH_MAX else ''}</p>"
    )

    # Display sections in template order
    _DISPLAY_ORDER = [
        "identity",
        "existential_role",
        "core_functions",
        "operational_boundary",
        "trigger_conditions",
        "working_modes",
        "input_contract",
        "output_contract",
        "decision_principles",
        "failure_modes",
        "quality_criteria",
        "neighbor_interaction",
        "runtime_binding",
        "self_evolution",
        "governance_statement",
        # Legacy sections (shown if present)
        "thinking_mode",
        "behavior_constraints",
        "output_spec",
    ]

    for key in _DISPLAY_ORDER:
        section = agent.sections.get(key)
        if section:
            parts.append(f"<h2>{section.heading_cn}</h2>")
            parts.append(_convert_md_block(section.content.strip()))

    # Show any remaining sections not in the display order
    shown_keys = set(_DISPLAY_ORDER) | {"layer"}
    for key, section in agent.sections.items():
        if key not in shown_keys:
            parts.append(f"<h2>{section.heading_cn}</h2>")
            parts.append(_convert_md_block(section.content.strip()))

    return "\n".join(parts)


# ---------------------------------------------------------------------------
# Dashboard widget
# ---------------------------------------------------------------------------

class DashboardPage(QWidget):
    """Main dashboard showing the 3-layer gravity structure."""

    def __init__(self, config: DreamMetaConfig, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._config = config
        self._agents: dict[str, Agent] = {}
        self._selected_id: str | None = None
        self._atom_buttons: dict[str, QPushButton] = {}
        self._base_labels: dict[str, str] = {}  # button base labels without indicators
        self._current_agent_path: str | None = None  # for "Open in Editor"
        self._debounce_pending: bool = False  # file-watcher debounce flag

        self._build_ui()
        self._load_agents()
        self._update_health_indicators()
        self._update_health_summary()

        # --- US-08: File watcher auto-refresh ---
        self._file_watcher = QFileSystemWatcher(self)
        agents_dir = str(config.agents_dir)
        self._file_watcher.addPath(agents_dir)
        self._file_watcher.directoryChanged.connect(self._on_directory_changed)

    def set_detail_style(self, css: str) -> None:
        """Update the HTML style used by the detail browser."""
        self._detail_browser.document().setDefaultStyleSheet(css)

    # -- UI construction ----

    def _build_ui(self) -> None:
        root = QHBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # -- Left: layer graph --
        graph_panel = QWidget()
        graph_layout = QVBoxLayout(graph_panel)
        graph_layout.setContentsMargins(24, 24, 24, 24)
        graph_layout.setSpacing(4)

        # Refresh button row with health summary (US-06)
        refresh_row = QHBoxLayout()

        # Health summary label (left-aligned)
        self._health_summary = QLabel("System Health: --/13")
        self._health_summary.setObjectName("health-summary")
        self._health_summary.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
        refresh_row.addWidget(self._health_summary)

        refresh_row.addStretch()

        # Refresh button (right-aligned)
        self._refresh_btn = QPushButton("\u21bb Refresh")
        self._refresh_btn.setObjectName("refresh-btn")
        self._refresh_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self._refresh_btn.setFixedHeight(28)
        self._refresh_btn.clicked.connect(self._on_refresh)
        refresh_row.addWidget(self._refresh_btn)

        graph_layout.addLayout(refresh_row)

        # Render top to bottom: Layer 3, 2, 1
        layer_order = [3, 2, 1]
        for idx, layer_num in enumerate(layer_order):
            cn_name, en_name = LAYERS[layer_num]

            # Layer label with styled background (US-06: layer-specific color)
            lbl = QLabel(f"  LAYER {layer_num}  \u2014  {en_name}  /  {cn_name}  ")
            lbl.setObjectName("layer-label")
            lbl.setProperty("layer", str(layer_num))
            lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)
            graph_layout.addWidget(lbl)

            # Atom buttons row
            row = QHBoxLayout()
            row.setAlignment(Qt.AlignmentFlag.AlignCenter)
            row.setSpacing(8)
            for agent_id in LAYER_AGENTS[layer_num]:
                cn, en, _, op = AGENT_REGISTRY[agent_id]
                # US-11: 2-line compact format — ID + operation char or short name
                short_name = cn.replace("\u5143", "")
                if op:
                    line2 = op
                else:
                    line2 = short_name
                label = f"{agent_id}\n{line2}"
                btn = QPushButton(label)
                btn.setProperty("layer", str(layer_num))
                btn.setCursor(Qt.CursorShape.PointingHandCursor)
                btn.clicked.connect(
                    lambda checked=False, aid=agent_id: self._on_atom_clicked(aid)
                )
                # US-11: Full name in tooltip (will be enriched with health info later)
                full_name = f"{agent_id} {cn} ({en})"
                btn.setToolTip(full_name)
                row.addWidget(btn)
                self._atom_buttons[agent_id] = btn
                self._base_labels[agent_id] = label
            graph_layout.addLayout(row)

            # Connector line between layers (not after the last one)
            if idx < len(layer_order) - 1:
                connector = QFrame()
                connector.setObjectName("layer-connector")
                connector.setFrameShape(QFrame.Shape.HLine)
                graph_layout.addWidget(connector)

        graph_layout.addStretch()

        # -- Separator --
        sep = QFrame()
        sep.setObjectName("separator")
        sep.setFrameShape(QFrame.Shape.VLine)

        # -- Right: detail panel --
        detail_panel = QWidget()
        detail_layout = QVBoxLayout(detail_panel)
        detail_layout.setContentsMargins(0, 0, 0, 0)

        self._placeholder = QLabel("Select an atom to view details")
        self._placeholder.setObjectName("placeholder")
        self._placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # US-07: "Open in Editor" button
        self._open_editor_btn = QPushButton("Open in Editor")
        self._open_editor_btn.setObjectName("open-editor-btn")
        self._open_editor_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self._open_editor_btn.setFixedHeight(32)
        self._open_editor_btn.clicked.connect(self._on_open_in_editor)
        self._open_editor_btn.hide()

        self._detail_browser = QTextBrowser()
        self._detail_browser.setOpenExternalLinks(False)
        self._detail_browser.hide()

        detail_layout.addWidget(self._placeholder)
        detail_layout.addWidget(self._open_editor_btn)
        detail_layout.addWidget(self._detail_browser)

        root.addWidget(graph_panel, 1)
        root.addWidget(sep)
        root.addWidget(detail_panel, 1)

    # -- Data loading ---

    def _load_agents(self) -> None:
        agents = parse_all_agents(self._config.agents_dir)
        self._agents = {a.id: a for a in agents}

    # -- Health indicators --

    def _update_health_indicators(self) -> None:
        """Update every atom button label with a health indicator and tooltip."""
        for agent_id, btn in self._atom_buttons.items():
            base = self._base_labels[agent_id]
            cn, en, _, _ = AGENT_REGISTRY[agent_id]
            full_name = f"{agent_id} {cn} ({en})"
            agent = self._agents.get(agent_id)
            if agent is None:
                # Agent file could not be parsed or is missing
                btn.setText(base + " ?")
                btn.setToolTip(f"{full_name}\nAgent file not found or parse error")
            else:
                score = _health_score(agent)
                indicator = _health_indicator(score)
                btn.setText(base + indicator)
                # US-10: Health tooltip
                if score >= _HEALTH_MAX:
                    health_tip = "All sections present \u2714"
                else:
                    missing = _missing_sections(agent)
                    health_tip = "Missing: " + ", ".join(missing)
                btn.setToolTip(f"{full_name}\n{health_tip}")

    # -- Health summary (US-06) --

    def _update_health_summary(self) -> None:
        """Update the aggregate health summary label."""
        healthy = 0
        warnings = 0
        errors = 0
        for agent_id in AGENT_REGISTRY:
            agent = self._agents.get(agent_id)
            if agent is None:
                errors += 1
            else:
                score = _health_score(agent)
                if score >= _HEALTH_MAX:
                    healthy += 1
                elif score >= _HEALTH_MAX - 2:
                    warnings += 1
                else:
                    errors += 1
        text = f"System Health: {healthy}/13 Healthy"
        if warnings:
            text += f", {warnings} Warnings"
        if errors:
            text += f", {errors} Errors"
        self._health_summary.setText(text)

    # -- Refresh --

    def _on_refresh(self) -> None:
        """Re-load agents, update health indicators, and refresh detail."""
        self._load_agents()
        self._update_health_indicators()
        self._update_health_summary()

        # Re-render detail if an agent was selected
        if self._selected_id:
            agent = self._agents.get(self._selected_id)
            if agent:
                self._detail_browser.setHtml(_agent_to_html(agent))

    # -- US-08: File watcher debounce --

    def _on_directory_changed(self, _path: str) -> None:
        """Handle file system change with debounce."""
        if not self._debounce_pending:
            self._debounce_pending = True
            QTimer.singleShot(500, self._on_debounced_refresh)

    def _on_debounced_refresh(self) -> None:
        """Execute debounced refresh after file system change."""
        self._debounce_pending = False
        self._on_refresh()

    # -- US-07: Open in Editor --

    def _on_open_in_editor(self) -> None:
        """Open the currently selected agent file in the system default editor."""
        if self._current_agent_path:
            QDesktopServices.openUrl(QUrl.fromLocalFile(self._current_agent_path))

    # -- Atom click handling --

    def _on_atom_clicked(self, agent_id: str) -> None:
        # Update selection highlight
        if self._selected_id:
            old_btn = self._atom_buttons.get(self._selected_id)
            if old_btn:
                old_btn.setProperty("selected", "false")
                old_btn.style().unpolish(old_btn)
                old_btn.style().polish(old_btn)

        self._selected_id = agent_id
        btn = self._atom_buttons.get(agent_id)
        if btn:
            btn.setProperty("selected", "true")
            btn.style().unpolish(btn)
            btn.style().polish(btn)

        # Show detail
        agent = self._agents.get(agent_id)
        if not agent:
            self._open_editor_btn.hide()
            self._current_agent_path = None
            return
        self._placeholder.hide()

        # US-07: Show editor button and store path
        if agent.source_path:
            self._current_agent_path = str(agent.source_path)
            self._open_editor_btn.show()
        else:
            self._current_agent_path = None
            self._open_editor_btn.hide()

        self._detail_browser.show()
        self._detail_browser.setHtml(_agent_to_html(agent))
