"""梦元 DreamMeta — Meta-Department TUI Dashboard."""

try:
    from importlib.metadata import version
    __version__ = version("dreammeta")
except Exception:
    __version__ = "0.4.0"
