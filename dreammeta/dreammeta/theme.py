"""Dynamic theme system for DreamMeta — default dark, customizable."""

from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path


@dataclass
class ThemeColors:
    """Color palette for a theme."""

    # ── Background gradient (dark → light) ──────────────────────
    base: str = "#0a0a0c"           # Deepest background
    mantle: str = "#101014"         # Sidebar / status bar
    crust: str = "#08080a"          # Below-base (brand area)
    surface0: str = "#18181c"       # Cards, input fields
    surface1: str = "#222228"       # Hover backgrounds
    surface2: str = "#2c2c34"       # Active backgrounds
    overlay: str = "#3a3a44"        # Borders, dividers
    overlay_light: str = "#48485a"  # Secondary borders

    # ── Text ────────────────────────────────────────────────────
    text: str = "#e2e2e8"           # Primary text
    text_muted: str = "#6e6e82"     # Muted / placeholder
    text_subtle: str = "#52526a"    # Very subtle hints

    # ── Accents ─────────────────────────────────────────────────
    accent: str = "#7b6cb7"         # Cool purple (primary)
    accent_light: str = "#a99cd6"   # Light purple
    accent_dim: str = "#4a3f78"     # Dimmed accent for backgrounds
    gold: str = "#c9a84c"           # Gold point-color for highlights

    # ── Semantic ────────────────────────────────────────────────
    green: str = "#5eb87a"          # Success
    amber: str = "#d4a44c"         # Warning
    red: str = "#c95454"            # Error

    # ── Layer colors (more saturated, more distinct) ────────────
    layer1_bg: str = "#0c1a2e"      # Foundation — deep navy
    layer1_fg: str = "#5a9ec8"      # Foundation — steel blue
    layer1_border: str = "#1a2e48"  # Foundation — subtle border
    layer2_bg: str = "#2a1a0a"      # Orchestration — deep amber
    layer2_fg: str = "#c8985a"      # Orchestration — warm amber
    layer2_border: str = "#3e2a14"  # Orchestration — subtle border
    layer3_bg: str = "#0a2a1a"      # Execution — deep emerald
    layer3_fg: str = "#5ac87a"      # Execution — vivid green
    layer3_border: str = "#143e28"  # Execution — subtle border


@dataclass
class ThemeFonts:
    """Font settings."""

    family: str = "Segoe UI"
    fallback: str = "Microsoft YaHei"
    mono: str = "Consolas"
    size: int = 13
    size_small: int = 12
    size_large: int = 14
    size_h1: int = 18
    size_h2: int = 15
    size_h3: int = 13


@dataclass
class ThemeConfig:
    """Complete theme configuration."""

    name: str = "Obsidian"
    colors: ThemeColors = field(default_factory=ThemeColors)
    fonts: ThemeFonts = field(default_factory=ThemeFonts)


# ── Preset themes ────────────────────────────────────────────────

PRESET_THEMES: dict[str, ThemeColors] = {
    "Obsidian": ThemeColors(),  # Default

    "Catppuccin Mocha": ThemeColors(
        base="#1e1e2e", mantle="#181825", crust="#11111b",
        surface0="#313244", surface1="#45475a", surface2="#585b70",
        overlay="#6c7086", overlay_light="#7f849c",
        text="#cdd6f4", text_muted="#6c7086", text_subtle="#585b70",
        accent="#c9a0dc", accent_light="#f5c2e7", accent_dim="#7a5a8c",
        gold="#f9e2af",
        green="#a6e3a1", amber="#f9e2af", red="#f38ba8",
        layer1_bg="#1a3a5c", layer1_fg="#7eb8da", layer1_border="#2a4a6c",
        layer2_bg="#5c3a1a", layer2_fg="#dab87e", layer2_border="#6c4a2a",
        layer3_bg="#1a5c3a", layer3_fg="#7eda8b", layer3_border="#2a6c4a",
    ),

    "Nord": ThemeColors(
        base="#2e3440", mantle="#272c36", crust="#222730",
        surface0="#3b4252", surface1="#434c5e", surface2="#4c566a",
        overlay="#616e88", overlay_light="#6d7a96",
        text="#eceff4", text_muted="#7b88a1", text_subtle="#616e88",
        accent="#88c0d0", accent_light="#8fbcbb", accent_dim="#4a6a7a",
        gold="#ebcb8b",
        green="#a3be8c", amber="#ebcb8b", red="#bf616a",
        layer1_bg="#2e3440", layer1_fg="#81a1c1", layer1_border="#3e4450",
        layer2_bg="#3b3226", layer2_fg="#d08770", layer2_border="#4b4236",
        layer3_bg="#2a3a2e", layer3_fg="#a3be8c", layer3_border="#3a4a3e",
    ),

    "Dracula": ThemeColors(
        base="#282a36", mantle="#21222c", crust="#1a1b26",
        surface0="#343746", surface1="#44475a", surface2="#565970",
        overlay="#6272a4", overlay_light="#7282b4",
        text="#f8f8f2", text_muted="#6272a4", text_subtle="#565970",
        accent="#bd93f9", accent_light="#ff79c6", accent_dim="#6a4ca0",
        gold="#f1fa8c",
        green="#50fa7b", amber="#f1fa8c", red="#ff5555",
        layer1_bg="#1a2a44", layer1_fg="#8be9fd", layer1_border="#2a3a54",
        layer2_bg="#44341a", layer2_fg="#ffb86c", layer2_border="#54442a",
        layer3_bg="#1a4428", layer3_fg="#50fa7b", layer3_border="#2a5438",
    ),
}


class ThemeManager:
    """Manages theme state and generates QSS."""

    def __init__(self, settings_path: Path) -> None:
        self._settings_path = settings_path
        self._config = ThemeConfig()
        self._load()

    @property
    def config(self) -> ThemeConfig:
        return self._config

    @property
    def colors(self) -> ThemeColors:
        return self._config.colors

    @property
    def fonts(self) -> ThemeFonts:
        return self._config.fonts

    def apply_preset(self, name: str) -> None:
        if name in PRESET_THEMES:
            self._config.colors = ThemeColors(**asdict(PRESET_THEMES[name]))
            self._config.name = name
            self._save()

    def set_accent(self, color: str) -> None:
        self._config.colors.accent = color
        self._save()

    def set_font(self, family: str | None = None, size: int | None = None) -> None:
        if family is not None:
            self._config.fonts.family = family
        if size is not None:
            self._config.fonts.size = size
            self._config.fonts.size_small = max(10, size - 1)
            self._config.fonts.size_large = size + 1
        self._save()

    def set_mono_font(self, family: str) -> None:
        self._config.fonts.mono = family
        self._save()

    def generate_stylesheet(self) -> str:
        c = self._config.colors
        f = self._config.fonts
        font_stack = f'"{f.family}", "{f.fallback}", sans-serif'
        mono_stack = f'"{f.mono}", monospace'

        return f"""
/* ========================================================================
   DreamMeta QSS — Generated by ThemeManager
   ======================================================================== */

/* ===== Global Reset ===== */
QMainWindow, QWidget {{
    background-color: {c.base};
    color: {c.text};
    font-family: {font_stack};
    font-size: {f.size}px;
}}

/* ===== Sidebar ===== */
QWidget#sidebar {{
    background-color: {c.mantle};
    min-width: 200px;
    max-width: 200px;
    border-right: 1px solid {c.surface0};
}}

/* -- Brand area at top -- */
QLabel#brand-title {{
    color: {c.text};
    font-size: {f.size_h1}px;
    font-weight: bold;
    padding: 0;
    background: transparent;
    letter-spacing: 2px;
}}
QLabel#brand-subtitle {{
    color: {c.text_subtle};
    font-size: {f.size_small}px;
    padding: 0;
    background: transparent;
}}
QWidget#brand-area {{
    background-color: {c.crust};
    border-bottom: 1px solid {c.surface0};
}}

/* -- Nav separator -- */
QFrame#nav-separator {{
    background-color: {c.surface0};
    max-height: 1px;
    min-height: 1px;
    margin: 4px 16px;
}}

/* -- Nav buttons -- */
QWidget#sidebar QPushButton {{
    background-color: transparent;
    color: {c.text_muted};
    border: none;
    border-left: 3px solid transparent;
    text-align: left;
    padding: 10px 16px 10px 14px;
    font-size: {f.size}px;
    border-radius: 0;
}}
QWidget#sidebar QPushButton:hover {{
    background-color: {c.surface0};
    color: {c.text};
    border-left: 3px solid {c.overlay};
}}
QWidget#sidebar QPushButton[active="true"] {{
    background-color: {c.surface1};
    color: {c.text};
    font-weight: bold;
    border-left: 3px solid {c.accent};
}}

/* ===== Layer atom buttons ===== */
QPushButton[layer="1"] {{
    background-color: {c.layer1_bg};
    color: {c.layer1_fg};
    border: 1px solid {c.layer1_border};
    border-bottom: 2px solid {c.layer1_border};
    border-radius: 8px;
    min-width: 100px;
    min-height: 56px;
    margin: 4px;
    padding: 6px 8px;
    font-size: {f.size_small}px;
}}
QPushButton[layer="1"]:hover {{
    border: 1px solid {c.layer1_fg};
    border-bottom: 2px solid {c.layer1_fg};
    background-color: {c.layer1_border};
}}
QPushButton[layer="1"][selected="true"] {{
    border: 2px solid {c.accent};
    border-bottom: 3px solid {c.accent};
    background-color: {c.layer1_border};
    font-weight: bold;
}}

QPushButton[layer="2"] {{
    background-color: {c.layer2_bg};
    color: {c.layer2_fg};
    border: 1px solid {c.layer2_border};
    border-bottom: 2px solid {c.layer2_border};
    border-radius: 8px;
    min-width: 100px;
    min-height: 56px;
    margin: 4px;
    padding: 6px 8px;
    font-size: {f.size_small}px;
}}
QPushButton[layer="2"]:hover {{
    border: 1px solid {c.layer2_fg};
    border-bottom: 2px solid {c.layer2_fg};
    background-color: {c.layer2_border};
}}
QPushButton[layer="2"][selected="true"] {{
    border: 2px solid {c.accent};
    border-bottom: 3px solid {c.accent};
    background-color: {c.layer2_border};
    font-weight: bold;
}}

QPushButton[layer="3"] {{
    background-color: {c.layer3_bg};
    color: {c.layer3_fg};
    border: 1px solid {c.layer3_border};
    border-bottom: 2px solid {c.layer3_border};
    border-radius: 8px;
    min-width: 100px;
    min-height: 56px;
    margin: 4px;
    padding: 6px 8px;
    font-size: {f.size_small}px;
}}
QPushButton[layer="3"]:hover {{
    border: 1px solid {c.layer3_fg};
    border-bottom: 2px solid {c.layer3_fg};
    background-color: {c.layer3_border};
}}
QPushButton[layer="3"][selected="true"] {{
    border: 2px solid {c.accent};
    border-bottom: 3px solid {c.accent};
    background-color: {c.layer3_border};
    font-weight: bold;
}}

/* ===== Separator ===== */
QFrame#separator {{
    background-color: {c.surface0};
    max-width: 1px;
    min-width: 1px;
}}

/* ===== Layer labels ===== */
QLabel#layer-label {{
    color: {c.text_muted};
    font-size: {f.size_small}px;
    font-weight: bold;
    letter-spacing: 1px;
    padding: 8px 12px 4px 12px;
    background-color: {c.surface0};
    border-radius: 4px;
    margin: 8px 24px 2px 24px;
}}
QLabel#layer-label[layer="1"] {{ color: {c.layer1_fg}; background-color: {c.layer1_bg}; }}
QLabel#layer-label[layer="2"] {{ color: {c.layer2_fg}; background-color: {c.layer2_bg}; }}
QLabel#layer-label[layer="3"] {{ color: {c.layer3_fg}; background-color: {c.layer3_bg}; }}

/* ===== Health summary ===== */
QLabel#health-summary {{
    color: {c.text_muted};
    font-size: {f.size_small}px;
    padding: 4px 8px;
}}

/* ===== Refresh button ===== */
QPushButton#refresh-btn {{
    background-color: {c.surface0};
    color: {c.text_muted};
    border: 1px solid {c.overlay};
    border-radius: 4px;
    padding: 4px 12px;
    font-size: {f.size_small}px;
}}
QPushButton#refresh-btn:hover {{
    background-color: {c.surface1};
    color: {c.text};
}}

/* ===== Open in Editor button ===== */
QPushButton#open-editor-btn {{
    background-color: {c.surface0};
    color: {c.accent_light};
    border: 1px solid {c.overlay};
    border-radius: 4px;
    padding: 6px 16px;
    font-size: {f.size_small}px;
}}
QPushButton#open-editor-btn:hover {{
    background-color: {c.accent_dim};
    color: {c.text};
}}

/* ===== Layer connector lines ===== */
QFrame#layer-connector {{
    background-color: {c.overlay};
    min-height: 1px;
    max-height: 1px;
    margin: 0 48px;
}}

/* ===== Section titles ===== */
QLabel#section-title {{
    color: {c.accent};
    font-weight: bold;
    font-size: {f.size_large}px;
    padding: 4px 0 8px 0;
    border-bottom: 2px solid {c.accent_dim};
    margin-bottom: 8px;
}}

/* ===== Placeholder text ===== */
QLabel#placeholder {{
    color: {c.text_subtle};
    font-style: italic;
    padding: 24px;
}}

/* ===== Detail panels ===== */
QTextBrowser {{
    background-color: {c.base};
    color: {c.text};
    border: none;
    padding: 16px 20px;
    selection-background-color: {c.surface1};
}}

/* ===== Search input ===== */
QLineEdit {{
    background-color: {c.surface0};
    color: {c.text};
    border: 1px solid {c.overlay};
    border-radius: 4px;
    padding: 10px 12px;
    font-size: {f.size}px;
}}
QLineEdit:focus {{
    border: 1px solid {c.accent};
    background-color: {c.surface1};
}}
QLineEdit::placeholder {{
    color: {c.text_subtle};
}}

/* ===== Combo box ===== */
QComboBox {{
    background-color: {c.surface0};
    color: {c.text};
    border: 1px solid {c.overlay};
    border-radius: 4px;
    padding: 8px 12px;
    font-size: {f.size}px;
    min-height: 20px;
}}
QComboBox:focus {{
    border: 1px solid {c.accent};
}}
QComboBox::drop-down {{
    border: none;
    width: 24px;
}}
QComboBox QAbstractItemView {{
    background-color: {c.surface0};
    color: {c.text};
    border: 1px solid {c.overlay};
    selection-background-color: {c.surface2};
    selection-color: {c.text};
    outline: none;
    padding: 4px;
}}
QComboBox QAbstractItemView::item {{
    padding: 6px 8px;
    min-height: 24px;
}}
QComboBox QAbstractItemView::item:hover {{
    background-color: {c.surface1};
}}

/* ===== Spin box ===== */
QSpinBox {{
    background-color: {c.surface0};
    color: {c.text};
    border: 1px solid {c.overlay};
    border-radius: 4px;
    padding: 8px 12px;
    font-size: {f.size}px;
}}
QSpinBox:focus {{
    border: 1px solid {c.accent};
}}

/* ===== List widgets ===== */
QListWidget {{
    background-color: {c.base};
    color: {c.text};
    border: 1px solid {c.surface0};
    border-radius: 4px;
    outline: none;
    font-size: {f.size}px;
}}
QListWidget::item {{
    padding: 10px 12px;
    border-bottom: 1px solid {c.surface0};
    border-radius: 0;
}}
QListWidget::item:selected {{
    background-color: {c.surface1};
    border-left: 3px solid {c.accent};
}}
QListWidget::item:hover:!selected {{
    background-color: {c.surface0};
}}

/* ===== Project cards ===== */
QFrame#project-card {{
    background-color: {c.surface0};
    border: 1px solid {c.overlay};
    border-bottom: 2px solid {c.overlay};
    border-radius: 8px;
    padding: 14px 18px;
}}
QFrame#project-card:hover {{
    border: 1px solid {c.accent_dim};
    border-bottom: 2px solid {c.accent_dim};
    background-color: {c.surface1};
}}

/* -- Project card labels -- */
QLabel#card-name {{
    font-weight: bold;
    font-size: {f.size_large}px;
    color: {c.text};
    padding: 0;
    background: transparent;
}}
QLabel#card-info {{
    color: {c.text_muted};
    font-size: {f.size_small}px;
    padding: 0;
    background: transparent;
}}

QLabel#health-good {{ color: {c.green}; font-weight: bold; font-size: {f.size_small}px; }}
QLabel#health-warn {{ color: {c.amber}; font-weight: bold; font-size: {f.size_small}px; }}
QLabel#health-bad  {{ color: {c.red}; font-weight: bold; font-size: {f.size_small}px; }}

/* ===== Action buttons ===== */
QPushButton#action-btn {{
    background-color: {c.surface1};
    color: {c.text};
    border: 1px solid {c.overlay};
    border-bottom: 2px solid {c.overlay};
    border-radius: 4px;
    padding: 8px 16px;
    font-size: {f.size}px;
}}
QPushButton#action-btn:hover {{
    background-color: {c.surface2};
    border: 1px solid {c.overlay_light};
    border-bottom: 2px solid {c.overlay_light};
}}
QPushButton#action-btn:pressed {{
    background-color: {c.surface1};
    border-bottom: 1px solid {c.overlay};
    padding-top: 9px;
}}

QPushButton#primary-btn {{
    background-color: {c.accent_dim};
    color: {c.accent_light};
    border: 1px solid {c.accent};
    border-bottom: 2px solid {c.accent};
    border-radius: 4px;
    padding: 8px 16px;
    font-weight: bold;
    font-size: {f.size}px;
}}
QPushButton#primary-btn:hover {{
    background-color: {c.accent};
    color: {c.text};
}}
QPushButton#primary-btn:pressed {{
    background-color: {c.accent_dim};
    border-bottom: 1px solid {c.accent};
    padding-top: 9px;
}}

/* ===== Scroll areas ===== */
QScrollArea {{
    border: none;
    background-color: transparent;
}}
QScrollBar:vertical {{
    background-color: {c.mantle};
    width: 8px;
    border-radius: 4px;
}}
QScrollBar::handle:vertical {{
    background-color: {c.surface2};
    border-radius: 4px;
    min-height: 24px;
}}
QScrollBar::handle:vertical:hover {{
    background-color: {c.overlay};
}}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0;
}}
QScrollBar:horizontal {{
    background-color: {c.mantle};
    height: 8px;
    border-radius: 4px;
}}
QScrollBar::handle:horizontal {{
    background-color: {c.surface2};
    border-radius: 4px;
    min-width: 24px;
}}
QScrollBar::handle:horizontal:hover {{
    background-color: {c.overlay};
}}
QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
    width: 0;
}}

/* ===== Status bar ===== */
QStatusBar {{
    background-color: {c.crust};
    color: {c.text_subtle};
    border-top: 1px solid {c.surface0};
    font-size: {f.size_small}px;
    padding: 2px 12px;
}}

/* ===== Group box (settings) ===== */
QGroupBox {{
    background-color: {c.surface0};
    border: 1px solid {c.overlay};
    border-radius: 8px;
    margin-top: 16px;
    padding: 20px 16px 16px 16px;
    font-weight: bold;
    color: {c.accent};
}}
QGroupBox::title {{
    subcontrol-origin: margin;
    left: 16px;
    padding: 0 8px;
    color: {c.accent_light};
    font-size: {f.size_large}px;
}}

"""

    def generate_detail_html_style(self) -> str:
        c = self._config.colors
        f = self._config.fonts
        font_stack = f'"{f.family}", "{f.fallback}", sans-serif'
        mono_stack = f'"{f.mono}", monospace'

        return f"""
    body {{
        color: {c.text};
        font-family: {font_stack};
        font-size: {f.size}px;
        line-height: 1.6;
    }}
    h1 {{
        color: {c.text};
        font-size: {f.size_h1}px;
        margin-bottom: 10px;
        padding-bottom: 8px;
        border-bottom: 2px solid {c.accent_dim};
    }}
    h2 {{
        color: {c.accent};
        font-size: {f.size_h2}px;
        margin-top: 20px;
        margin-bottom: 8px;
        padding-bottom: 4px;
        border-bottom: 1px solid {c.surface1};
    }}
    h3 {{
        color: {c.accent_light};
        font-size: {f.size_h3}px;
        margin-top: 14px;
    }}
    pre {{
        background-color: {c.surface0};
        color: {c.green};
        padding: 12px 14px;
        border: 1px solid {c.overlay};
        border-left: 3px solid {c.accent_dim};
        border-radius: 4px;
        font-family: {mono_stack};
        font-size: {f.size_small}px;
        line-height: 1.5;
        margin: 8px 0;
    }}
    code {{
        background-color: {c.surface0};
        color: {c.green};
        padding: 2px 6px;
        border-radius: 3px;
        font-family: {mono_stack};
    }}
    b, strong {{
        color: {c.accent_light};
    }}
    ul {{
        margin-left: 16px;
        padding-left: 8px;
    }}
    li {{
        margin-bottom: 6px;
        line-height: 1.5;
    }}
    p {{
        margin: 6px 0;
        line-height: 1.6;
    }}
    .muted {{ color: {c.text_muted}; }}
    .layer-1 {{ color: {c.layer1_fg}; font-weight: bold; }}
    .layer-2 {{ color: {c.layer2_fg}; font-weight: bold; }}
    .layer-3 {{ color: {c.layer3_fg}; font-weight: bold; }}
"""

    # ── Persistence ──────────────────────────────────────────────

    def _load(self) -> None:
        if not self._settings_path.exists():
            return
        try:
            data = json.loads(self._settings_path.read_text(encoding="utf-8"))
            theme_data = data.get("theme", {})
            if "name" in theme_data:
                self._config.name = theme_data["name"]
            if "colors" in theme_data:
                self._config.colors = ThemeColors(**theme_data["colors"])
            if "fonts" in theme_data:
                self._config.fonts = ThemeFonts(**theme_data["fonts"])
        except (json.JSONDecodeError, TypeError, KeyError):
            pass

    def _save(self) -> None:
        data: dict = {}
        if self._settings_path.exists():
            try:
                data = json.loads(self._settings_path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, TypeError):
                pass
        data["theme"] = {
            "name": self._config.name,
            "colors": asdict(self._config.colors),
            "fonts": asdict(self._config.fonts),
        }
        self._settings_path.write_text(
            json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8"
        )
