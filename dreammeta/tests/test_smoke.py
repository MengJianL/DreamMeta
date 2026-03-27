"""Smoke tests — verify DreamMeta can start and all pages render."""

from __future__ import annotations

import sys

import pytest
from PySide6.QtWidgets import QApplication

from dreammeta.config import DreamMetaConfig
from dreammeta.theme import ThemeColors, ThemeManager, PRESET_THEMES


@pytest.fixture(scope="session")
def qapp():
    """Provide a QApplication instance for the entire test session."""
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    return app


@pytest.fixture()
def config():
    return DreamMetaConfig()


class TestTheme:
    """Tests for the theme system."""

    def test_all_presets_loadable(self) -> None:
        for name in PRESET_THEMES:
            colors = PRESET_THEMES[name]
            assert colors.base.startswith("#")
            assert colors.text.startswith("#")

    def test_theme_manager_generates_qss(self, tmp_path) -> None:
        settings = tmp_path / "settings.json"
        tm = ThemeManager(settings)
        qss = tm.generate_stylesheet()
        assert len(qss) > 1000
        assert "sidebar" in qss
        assert "layer-label" in qss

    def test_layer_label_per_layer_styling(self, tmp_path) -> None:
        settings = tmp_path / "settings.json"
        tm = ThemeManager(settings)
        qss = tm.generate_stylesheet()
        assert 'layer-label[layer="1"]' in qss
        assert 'layer-label[layer="2"]' in qss
        assert 'layer-label[layer="3"]' in qss

    def test_new_component_styles(self, tmp_path) -> None:
        settings = tmp_path / "settings.json"
        tm = ThemeManager(settings)
        qss = tm.generate_stylesheet()
        assert "health-summary" in qss
        assert "refresh-btn" in qss
        assert "open-editor-btn" in qss

    def test_no_hardcoded_hover_colors(self, tmp_path) -> None:
        settings = tmp_path / "settings.json"
        tm = ThemeManager(settings)
        qss = tm.generate_stylesheet()
        for bad in ["#0e2038", "#102444", "#34220e", "#0e3422"]:
            assert bad not in qss, f"Hardcoded color {bad} still in QSS"

    def test_no_dead_qss_sections(self, tmp_path) -> None:
        settings = tmp_path / "settings.json"
        tm = ThemeManager(settings)
        qss = tm.generate_stylesheet()
        assert "search-toolbar" not in qss
        assert "preview-card" not in qss

    def test_theme_manager_generates_detail_css(self, tmp_path) -> None:
        settings = tmp_path / "settings.json"
        tm = ThemeManager(settings)
        css = tm.generate_detail_html_style()
        assert "layer-1" in css
        assert "layer-2" in css
        assert "layer-3" in css

    def test_preset_switch_persists(self, tmp_path) -> None:
        settings = tmp_path / "settings.json"
        tm = ThemeManager(settings)
        tm.apply_preset("Nord")
        assert tm.config.name == "Nord"
        tm2 = ThemeManager(settings)
        assert tm2.config.name == "Nord"

    def test_theme_colors_field_count(self) -> None:
        tc = ThemeColors()
        assert len(tc.__dataclass_fields__) >= 27


class TestAppStartup:
    """Tests that require a QApplication."""

    def test_window_creation(self, qapp, config) -> None:
        from dreammeta.app import DreamMetaWindow

        window = DreamMetaWindow(config)
        assert window.windowTitle() == "\u68a6\u5143 DreamMeta"
        assert window._stack.count() == 3

    def test_pages_have_detail_style(self, qapp, config) -> None:
        from dreammeta.app import DreamMetaWindow

        window = DreamMetaWindow(config)
        for attr in ["_dashboard", "_projects"]:
            page = getattr(window, attr)
            assert hasattr(page, "set_detail_style"), f"{attr} missing set_detail_style"

    def test_nav_buttons_count(self, qapp, config) -> None:
        from dreammeta.app import DreamMetaWindow

        window = DreamMetaWindow(config)
        assert len(window._nav_buttons) == 3

    def test_theme_apply(self, qapp, config) -> None:
        from dreammeta.app import DreamMetaWindow

        window = DreamMetaWindow(config)
        window._apply_theme()

    def test_dashboard_refresh(self, qapp, config) -> None:
        from dreammeta.app import DreamMetaWindow

        window = DreamMetaWindow(config)
        window._dashboard._on_refresh()

    def test_dashboard_health_summary_exists(self, qapp, config) -> None:
        from dreammeta.app import DreamMetaWindow

        window = DreamMetaWindow(config)
        assert hasattr(window._dashboard, "_health_summary")

    def test_dashboard_file_watcher_exists(self, qapp, config) -> None:
        from dreammeta.app import DreamMetaWindow

        window = DreamMetaWindow(config)
        assert hasattr(window._dashboard, "_file_watcher")

    def test_dashboard_open_editor_btn_exists(self, qapp, config) -> None:
        from dreammeta.app import DreamMetaWindow

        window = DreamMetaWindow(config)
        assert hasattr(window._dashboard, "_open_editor_btn")


class TestProjectScanner:
    """Tests for project scanner safety."""

    def test_init_project_uses_backup(self) -> None:
        import inspect
        from dreammeta.data.project_scanner import init_project

        src = inspect.getsource(init_project)
        assert "backup" in src, "init_project should backup existing agents"


class TestDeadCodeRemoval:
    """Verify dead code was properly cleaned up."""

    def test_no_dead_screen_imports(self) -> None:
        import importlib
        for mod in ["dreammeta.screens.collection", "dreammeta.screens.transform", "dreammeta.screens.absorb"]:
            with pytest.raises(ModuleNotFoundError):
                importlib.import_module(mod)

    def test_no_adapters_package(self) -> None:
        import importlib
        with pytest.raises(ModuleNotFoundError):
            importlib.import_module("dreammeta.adapters")

    def test_no_async_bridge(self) -> None:
        import importlib
        with pytest.raises(ModuleNotFoundError):
            importlib.import_module("dreammeta.async_bridge")

    def test_version_from_metadata(self) -> None:
        from dreammeta import __version__
        assert __version__ == "0.4.0"
