"""Settings page — theme configuration."""

from __future__ import annotations

from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QColorDialog,
    QComboBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
)

from dreammeta.config import DreamMetaConfig
from dreammeta.theme import PRESET_THEMES, ThemeManager


class SettingsPage(QWidget):
    """Settings for theme configuration."""

    theme_changed = Signal()

    def __init__(
        self,
        config: DreamMetaConfig,
        theme_manager: ThemeManager,
        parent: QWidget | None = None,
    ) -> None:
        super().__init__(parent)
        self._config = config
        self._theme = theme_manager
        self._build_ui()
        self._load_current_values()

    def _build_ui(self) -> None:
        root = QVBoxLayout(self)
        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(16)

        title = QLabel("Settings")
        title.setObjectName("section-title")
        root.addWidget(title)

        # ── Theme section ─────────────────────────────────────────
        theme_group = QGroupBox("Theme 主题")
        theme_layout = QVBoxLayout(theme_group)
        theme_layout.setSpacing(12)

        # Preset selector
        preset_row = QHBoxLayout()
        preset_row.addWidget(QLabel("Preset:"))
        self._preset_combo = QComboBox()
        self._preset_combo.addItems(list(PRESET_THEMES.keys()))
        self._preset_combo.currentTextChanged.connect(self._on_preset_changed)
        preset_row.addWidget(self._preset_combo, 1)
        theme_layout.addLayout(preset_row)

        # Accent color
        accent_row = QHBoxLayout()
        accent_row.addWidget(QLabel("Accent:"))
        self._accent_preview = QLabel("  ")
        self._accent_preview.setFixedSize(28, 28)
        accent_row.addWidget(self._accent_preview)
        self._accent_input = QLineEdit()
        self._accent_input.setPlaceholderText("#7b6cb7")
        self._accent_input.setMaximumWidth(120)
        self._accent_input.editingFinished.connect(self._on_accent_text_changed)
        accent_row.addWidget(self._accent_input)
        accent_pick_btn = QPushButton("Pick")
        accent_pick_btn.setObjectName("action-btn")
        accent_pick_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        accent_pick_btn.clicked.connect(self._on_pick_accent)
        accent_row.addWidget(accent_pick_btn)
        accent_row.addStretch()
        theme_layout.addLayout(accent_row)

        # Font size
        size_row = QHBoxLayout()
        size_row.addWidget(QLabel("Font Size:"))
        self._size_spin = QSpinBox()
        self._size_spin.setRange(10, 24)
        self._size_spin.setSuffix(" px")
        self._size_spin.valueChanged.connect(self._on_size_changed)
        size_row.addWidget(self._size_spin)
        size_row.addStretch()
        theme_layout.addLayout(size_row)

        root.addWidget(theme_group)

        # ── Preview section ───────────────────────────────────────
        preview_group = QGroupBox("Preview 预览")
        preview_layout = QVBoxLayout(preview_group)
        preview_layout.setSpacing(8)

        self._preview_label = QLabel()
        self._preview_label.setWordWrap(True)
        self._preview_label.setTextFormat(Qt.TextFormat.RichText)
        preview_layout.addWidget(self._preview_label)

        root.addWidget(preview_group)
        root.addStretch()

    def _load_current_values(self) -> None:
        self._preset_combo.blockSignals(True)
        self._size_spin.blockSignals(True)

        try:
            idx = self._preset_combo.findText(self._theme.config.name)
            if idx >= 0:
                self._preset_combo.setCurrentIndex(idx)
            self._update_accent_preview(self._theme.colors.accent)
            self._accent_input.setText(self._theme.colors.accent)
            self._size_spin.setValue(self._theme.fonts.size)
        finally:
            self._preset_combo.blockSignals(False)
            self._size_spin.blockSignals(False)

        self._update_preview()

    # ── Theme handlers ────────────────────────────────────────────

    def _on_preset_changed(self, name: str) -> None:
        self._theme.apply_preset(name)
        self._update_accent_preview(self._theme.colors.accent)
        self._accent_input.setText(self._theme.colors.accent)
        self._update_preview()
        self.theme_changed.emit()

    def _on_accent_text_changed(self) -> None:
        color = self._accent_input.text().strip()
        if color.startswith("#") and len(color) in (4, 7):
            self._theme.set_accent(color)
            self._update_accent_preview(color)
            self._update_preview()
            self.theme_changed.emit()

    def _on_pick_accent(self) -> None:
        from PySide6.QtGui import QColor

        current = QColor(self._theme.colors.accent)
        color = QColorDialog.getColor(current, self, "Pick Accent Color")
        if color.isValid():
            hex_color = color.name()
            self._theme.set_accent(hex_color)
            self._accent_input.setText(hex_color)
            self._update_accent_preview(hex_color)
            self._update_preview()
            self.theme_changed.emit()

    def _update_accent_preview(self, color: str) -> None:
        c = self._theme.colors
        self._accent_preview.setStyleSheet(
            f"background-color: {color}; border-radius: 4px; border: 1px solid {c.overlay};"
        )

    def _on_size_changed(self, size: int) -> None:
        self._theme.set_font(size=size)
        self._update_preview()
        self.theme_changed.emit()

    # ── Preview ───────────────────────────────────────────────────

    def _update_preview(self) -> None:
        c = self._theme.colors
        f = self._theme.fonts

        html = f"""
        <div style="font-family: '{f.family}', '{f.fallback}', sans-serif; font-size: {f.size}px;">
          <p style="color: {c.text}; margin-bottom: 8px;">
            <b>Theme:</b> {self._theme.config.name}
          </p>
          <p style="color: {c.text}; margin-bottom: 8px;">
            <span style="color: {c.accent};">\u25CF Accent</span> &nbsp;
            <span style="color: {c.gold};">\u25CF Gold</span> &nbsp;
            <span style="color: {c.green};">\u25CF Green</span>
          </p>
          <table cellpadding="4" cellspacing="0" style="margin: 4px 0;">
            <tr>
              <td style="background-color: {c.layer1_bg}; color: {c.layer1_fg};
                          border: 1px solid {c.layer1_border}; border-radius: 4px;
                          padding: 6px 12px;">L1 Foundation</td>
              <td style="background-color: {c.layer2_bg}; color: {c.layer2_fg};
                          border: 1px solid {c.layer2_border}; border-radius: 4px;
                          padding: 6px 12px;">L2 Orchestration</td>
              <td style="background-color: {c.layer3_bg}; color: {c.layer3_fg};
                          border: 1px solid {c.layer3_border}; border-radius: 4px;
                          padding: 6px 12px;">L3 Execution</td>
            </tr>
          </table>
        </div>
        """
        self._preview_label.setText(html)
