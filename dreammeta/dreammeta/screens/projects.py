"""Projects page — manage Meta-Department projects."""

from __future__ import annotations

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFileDialog,
    QFrame,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QTextBrowser,
    QVBoxLayout,
    QWidget,
)

from dreammeta.config import DreamMetaConfig
from dreammeta.data.models import ProjectInfo
from dreammeta.data.project_scanner import init_project, scan_project


def _project_to_html(proj: ProjectInfo) -> str:
    """Convert a ProjectInfo model to styled HTML."""
    health_class = "layer-3" if proj.agent_count == 13 else "layer-2"
    health_text = "Complete" if proj.agent_count == 13 else "Incomplete"

    parts = [
        f"<h1>{proj.name}</h1>",
        f"<p><b>Root</b>: {proj.root_path}</p>",
        f"<p><b>Health</b>: <span class='{health_class}'>{health_text}</span></p>",
        f"<p><b>Agents</b>: {proj.agent_count}/13</p>",
    ]
    if proj.missing_agents:
        parts.append(f"<p><b>Missing</b>: {', '.join(proj.missing_agents)}</p>")
    parts.append(f"<p><b>Memory Topics</b>: {proj.topic_count}</p>")
    parts.append(
        f"<p><b>CLAUDE.md</b>: {'Yes' if proj.has_claude_md else 'No'}</p>"
    )
    if proj.last_modified:
        parts.append(
            f"<p class='muted'>Last modified: {proj.last_modified:%Y-%m-%d %H:%M}</p>"
        )
    return "\n".join(parts)


class _ProjectCard(QFrame):
    """A clickable card displaying project summary info."""

    def __init__(
        self, project: ProjectInfo, on_click, parent: QWidget | None = None
    ) -> None:
        super().__init__(parent)
        self.project = project
        self._on_click = on_click
        self.setObjectName("project-card")
        self.setCursor(Qt.CursorShape.PointingHandCursor)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(14, 12, 14, 12)
        layout.setSpacing(6)

        # Project name — styled via QSS objectName
        name_label = QLabel(project.name)
        name_label.setObjectName("card-name")
        layout.addWidget(name_label)

        # Info line — styled via QSS objectName
        info_text = (
            f"Agents: {project.agent_count}/13  \u2502  "
            f"Topics: {project.topic_count}  \u2502  "
            f"{'CLAUDE.md' if project.has_claude_md else 'No CLAUDE.md'}"
        )
        info_label = QLabel(info_text)
        info_label.setObjectName("card-info")
        layout.addWidget(info_label)

        # Health indicator — styled via QSS objectName
        health = "Complete" if project.agent_count == 13 else "Incomplete"
        health_id = "health-good" if project.agent_count == 13 else "health-warn"
        health_label = QLabel(health)
        health_label.setObjectName(health_id)
        layout.addWidget(health_label)

    def mousePressEvent(self, event):
        self._on_click(self.project)
        super().mousePressEvent(event)


class ProjectsPage(QWidget):
    """Manage multiple projects using Meta-Department architecture."""

    def __init__(self, config: DreamMetaConfig, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._config = config
        self._build_ui()
        self._load_projects()

    def set_detail_style(self, css: str) -> None:
        """Update the HTML style used by the detail browser."""
        self._detail_browser.document().setDefaultStyleSheet(css)

    def _build_ui(self) -> None:
        root = QHBoxLayout(self)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # ── Left: project list ──────────────────────────────────
        list_panel = QWidget()
        list_layout = QVBoxLayout(list_panel)
        list_layout.setContentsMargins(24, 24, 24, 24)
        list_layout.setSpacing(12)

        title = QLabel("Projects")
        title.setObjectName("section-title")
        list_layout.addWidget(title)

        new_btn = QPushButton("+ Initialize New Project")
        new_btn.setObjectName("primary-btn")
        new_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        new_btn.clicked.connect(self._on_new_project)
        list_layout.addWidget(new_btn)

        # Scrollable cards area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        self._cards_container = QWidget()
        self._cards_layout = QVBoxLayout(self._cards_container)
        self._cards_layout.setContentsMargins(0, 8, 0, 0)
        self._cards_layout.setSpacing(8)
        self._cards_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll.setWidget(self._cards_container)
        list_layout.addWidget(scroll, 1)

        # ── Separator ───────────────────────────────────────────
        sep = QFrame()
        sep.setObjectName("separator")
        sep.setFrameShape(QFrame.Shape.VLine)

        # ── Right: detail panel ─────────────────────────────────
        detail_panel = QWidget()
        detail_layout = QVBoxLayout(detail_panel)
        detail_layout.setContentsMargins(0, 0, 0, 0)

        self._detail_placeholder = QLabel("Select a project to view details")
        self._detail_placeholder.setObjectName("placeholder")
        self._detail_placeholder.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self._detail_browser = QTextBrowser()
        self._detail_browser.hide()

        detail_layout.addWidget(self._detail_placeholder)
        detail_layout.addWidget(self._detail_browser)

        root.addWidget(list_panel, 1)
        root.addWidget(sep)
        root.addWidget(detail_panel, 1)

    def _load_projects(self) -> None:
        # Current Meta_Creates project
        project = scan_project(self._config.meta_creates_root)
        self._add_card(project)

        # Registered projects
        for proj_path in self._config.get_registered_projects():
            if proj_path.exists() and proj_path != self._config.meta_creates_root:
                proj = scan_project(proj_path)
                self._add_card(proj)

    def _add_card(self, project: ProjectInfo) -> None:
        card = _ProjectCard(project, self._on_card_clicked)
        self._cards_layout.addWidget(card)

    def _on_card_clicked(self, project: ProjectInfo) -> None:
        self._detail_placeholder.hide()
        self._detail_browser.show()
        self._detail_browser.setHtml(_project_to_html(project))

    def _on_new_project(self) -> None:
        dir_path = QFileDialog.getExistingDirectory(
            self, "Select project root directory"
        )
        if not dir_path:
            return
        from pathlib import Path

        target = Path(dir_path)
        project = init_project(self._config.agents_dir, target)
        self._config.register_project(target)
        self._add_card(project)
        self._on_card_clicked(project)
