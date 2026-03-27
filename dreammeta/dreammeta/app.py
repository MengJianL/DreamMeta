"""DreamMeta Desktop Application — Meta-Department operations hub."""

from __future__ import annotations

import sys
from pathlib import Path

from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import (
    QApplication,
    QFrame,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from dreammeta.config import DreamMetaConfig
from dreammeta.screens.dashboard import DashboardPage
from dreammeta.screens.projects import ProjectsPage
from dreammeta.screens.settings import SettingsPage
from dreammeta.theme import ThemeManager


_NAV_ITEMS = [
    ("\u25C8  Atoms", "atoms"),
    ("\u25A3  Projects", "projects"),
    ("\u2699  Settings", "settings"),
]


class DreamMetaWindow(QMainWindow):
    """梦元 — Meta-Department Desktop Dashboard."""

    def __init__(self, config: DreamMetaConfig) -> None:
        super().__init__()
        self.config = config
        self.theme_manager = ThemeManager(config.settings_file)
        self.setWindowTitle("\u68a6\u5143 DreamMeta")
        self.setMinimumSize(1024, 700)

        self._build_ui()
        self._apply_theme()
        self._bind_shortcuts()
        self._goto(0)

    # ── UI construction ─────────────────────────────────────────

    def _build_ui(self) -> None:
        central = QWidget()
        self.setCentralWidget(central)
        root_layout = QHBoxLayout(central)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        # Sidebar
        sidebar = QWidget()
        sidebar.setObjectName("sidebar")
        sidebar_layout = QVBoxLayout(sidebar)
        sidebar_layout.setContentsMargins(0, 0, 0, 8)
        sidebar_layout.setSpacing(0)

        # ── Brand area ──────────────────────────────────────────
        brand_area = QWidget()
        brand_area.setObjectName("brand-area")
        brand_layout = QVBoxLayout(brand_area)
        brand_layout.setContentsMargins(16, 16, 16, 12)
        brand_layout.setSpacing(2)

        brand_title = QLabel("\u68a6\u5143")
        brand_title.setObjectName("brand-title")
        brand_title.setAlignment(Qt.AlignmentFlag.AlignLeft)
        brand_layout.addWidget(brand_title)

        brand_sub = QLabel("DreamMeta v0.4.0")
        brand_sub.setObjectName("brand-subtitle")
        brand_sub.setAlignment(Qt.AlignmentFlag.AlignLeft)
        brand_layout.addWidget(brand_sub)

        sidebar_layout.addWidget(brand_area)

        # ── Nav separator ───────────────────────────────────────
        nav_sep = QFrame()
        nav_sep.setObjectName("nav-separator")
        nav_sep.setFrameShape(QFrame.Shape.HLine)
        sidebar_layout.addWidget(nav_sep)

        # ── Nav buttons ─────────────────────────────────────────
        self._nav_buttons: list[QPushButton] = []
        for label, _name in _NAV_ITEMS:
            btn = QPushButton(label)
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(lambda checked=False, idx=len(self._nav_buttons): self._goto(idx))
            sidebar_layout.addWidget(btn)
            self._nav_buttons.append(btn)
        sidebar_layout.addStretch()

        # Separator
        sep = QFrame()
        sep.setObjectName("separator")
        sep.setFrameShape(QFrame.Shape.VLine)

        # Stacked pages
        self._stack = QStackedWidget()
        self._dashboard = DashboardPage(self.config)
        self._projects = ProjectsPage(self.config)
        self._settings = SettingsPage(self.config, self.theme_manager)
        self._settings.theme_changed.connect(self._apply_theme)

        self._stack.addWidget(self._dashboard)
        self._stack.addWidget(self._projects)
        self._stack.addWidget(self._settings)

        root_layout.addWidget(sidebar)
        root_layout.addWidget(sep)
        root_layout.addWidget(self._stack, 1)

    def _bind_shortcuts(self) -> None:
        for key, idx in [("Ctrl+1", 0), ("Ctrl+2", 1), ("Ctrl+3", 2)]:
            shortcut = QShortcut(QKeySequence(key), self)
            shortcut.activated.connect(lambda i=idx: self._goto(i))

    # ── Theme ──────────────────────────────────────────────────

    def _apply_theme(self) -> None:
        """Regenerate and apply stylesheet from current theme."""
        self.setStyleSheet(self.theme_manager.generate_stylesheet())
        detail_css = self.theme_manager.generate_detail_html_style()
        # Update detail style on pages with QTextBrowser
        self._dashboard.set_detail_style(detail_css)
        self._projects.set_detail_style(detail_css)
        # Re-polish all nav buttons to pick up new styles
        for btn in self._nav_buttons:
            btn.style().unpolish(btn)
            btn.style().polish(btn)

    # ── Navigation ──────────────────────────────────────────────

    def _goto(self, index: int) -> None:
        self._stack.setCurrentIndex(index)
        for i, btn in enumerate(self._nav_buttons):
            btn.setProperty("active", "true" if i == index else "false")
            btn.style().unpolish(btn)
            btn.style().polish(btn)


def main(root: Path | None = None) -> None:
    """Entry point for the DreamMeta desktop application."""
    app = QApplication(sys.argv)
    config = DreamMetaConfig(app_root=root)
    window = DreamMetaWindow(config)
    window.show()
    sys.exit(app.exec())
