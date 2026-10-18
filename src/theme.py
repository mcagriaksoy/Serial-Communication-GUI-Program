# -*- coding: utf-8 -*-
"""Theming: GNOME / Adwaita inspired palettes and stylesheet application.

The Qt Style Sheet lives in ``ui/theme.qss`` and contains ``@token``
placeholders.  This module substitutes the placeholders using an Adwaita colour
palette (light / dark), following the GNOME Human Interface Guidelines: a single
blue accent colour, neutral surfaces and restrained borders.

``system`` mode follows the operating system colour scheme through
``QStyleHints.colorScheme()`` when available, with graceful fallbacks.
"""

from __future__ import annotations

import re
import sys

from .constants import DEFAULT_FONT_FAMILY, DEFAULT_FONT_SIZE, UI_DIR

_THEME_FILE = UI_DIR / "theme.qss"

# ---------------------------------------------------------------------------
# Adwaita palettes (colours taken from libadwaita's default style)
# ---------------------------------------------------------------------------
LIGHT_PALETTE = {
    "window_bg": "#fafafa",
    "headerbar_bg": "#f5f4f3",
    "card_bg": "#ffffff",
    "view_bg": "#ffffff",
    "field_bg": "#ffffff",
    "border": "rgba(0, 0, 0, 0.12)",
    "border_strong": "rgba(0, 0, 0, 0.22)",
    "fg": "#1d1d1d",
    "dim": "#6e6e6e",
    "dim_disabled": "#b0b0b0",
    "accent": "#3584e4",
    "accent_hover": "#4a90e2",
    "accent_active": "#1c71d8",
    "accent_fg": "#ffffff",
    "btn_bg": "#f6f5f4",
    "btn_hover": "#efeeec",
    "btn_active": "#e6e4e2",
    "btn_border": "rgba(0, 0, 0, 0.12)",
    "btn_disabled": "rgba(0, 0, 0, 0.05)",
    "hover": "rgba(0, 0, 0, 0.06)",
    "terminal_bg": "#1e1e1e",
    "terminal_fg": "#ffffff",
    "scroll": "rgba(0, 0, 0, 0.25)",
    "scroll_hover": "rgba(0, 0, 0, 0.45)",
    "success": "#2ec27e",
    "danger": "#e01b24",
    "danger_hover": "#c01c28",
    "warning": "#f5c211",
}

DARK_PALETTE = {
    "window_bg": "#242424",
    "headerbar_bg": "#2e2e2e",
    "card_bg": "#303030",
    "view_bg": "#1e1e1e",
    "field_bg": "#1e1e1e",
    "border": "rgba(255, 255, 255, 0.12)",
    "border_strong": "rgba(255, 255, 255, 0.22)",
    "fg": "#ffffff",
    "dim": "#9a9a9a",
    "dim_disabled": "#5f5f5f",
    "accent": "#78aeed",
    "accent_hover": "#8bbbf0",
    "accent_active": "#69a1e6",
    "accent_fg": "#0b0b0b",
    "btn_bg": "#3a3a3a",
    "btn_hover": "#454545",
    "btn_active": "#2e2e2e",
    "btn_border": "rgba(255, 255, 255, 0.10)",
    "btn_disabled": "rgba(255, 255, 255, 0.05)",
    "hover": "rgba(255, 255, 255, 0.08)",
    "terminal_bg": "#1e1e1e",
    "terminal_fg": "#ffffff",
    "scroll": "rgba(255, 255, 255, 0.25)",
    "scroll_hover": "rgba(255, 255, 255, 0.45)",
    "success": "#33d17a",
    "danger": "#ff7b63",
    "danger_hover": "#ff9384",
    "warning": "#f5c211",
}

_PALETTES = {"dark": DARK_PALETTE, "light": LIGHT_PALETTE}
_TOKEN_RE = re.compile(r"@([a-z_]+)")

_UI_FONT_CANDIDATES = (
    "Cantarell",
    "Adwaita Sans",
    "Inter",
    "Noto Sans",
    "DejaVu Sans",
    "Segoe UI",
    "Helvetica Neue",
    "Sans Serif",
)


def detect_ui_font() -> str:
    """Return the most Adwaita-like font installed on the system."""
    try:
        from PySide6.QtGui import QFontDatabase
        from PySide6.QtWidgets import QApplication

        # The font database needs a live application; fall back otherwise.
        if QApplication.instance() is None:
            return "Sans Serif"
        families = set(QFontDatabase.families())
        for name in _UI_FONT_CANDIDATES:
            if name in families:
                return name
    except Exception:
        pass
    return "Sans Serif"


def system_prefers_dark() -> bool:
    """Best-effort detection of the OS colour scheme."""
    # Preferred: Qt's own colour-scheme notification (Qt >= 6.5).
    try:
        from PySide6.QtCore import Qt
        from PySide6.QtWidgets import QApplication

        app = QApplication.instance()
        if app is not None:
            scheme = app.styleHints().colorScheme()
            if scheme == Qt.ColorScheme.Dark:
                return True
            if scheme == Qt.ColorScheme.Light:
                return False
    except Exception:
        pass

    if sys.platform.startswith("win"):
        try:
            from winreg import (  # type: ignore[import-not-found]
                HKEY_CURRENT_USER,
                KEY_READ,
                OpenKey,
                QueryValueEx,
            )

            with OpenKey(
                HKEY_CURRENT_USER,
                r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize",
                0,
                KEY_READ,
            ) as key:
                value, _ = QueryValueEx(key, "AppsUseLightTheme")
                return value == 0
        except Exception:
            return False

    if sys.platform == "darwin":
        try:
            from subprocess import DEVNULL, check_output

            result = check_output(
                ["defaults", "read", "-g", "AppleInterfaceStyle"],
                text=True,
                stderr=DEVNULL,
            )
            return "dark" in result.lower()
        except Exception:
            return False

    # Linux / GNOME: ask gsettings for the desktop colour scheme.
    try:
        from subprocess import DEVNULL, check_output

        result = check_output(
            ["gsettings", "get", "org.gnome.desktop.interface", "color-scheme"],
            text=True,
            stderr=DEVNULL,
        ).strip()
        if "dark" in result:
            return True
        if "default" in result or "light" in result:
            return False
    except Exception:
        pass

    # Fall back to dark for a developer tool.
    return True


def resolve_theme(theme: str) -> str:
    """Return the concrete palette name for a settings value."""
    if theme == "system":
        return "dark" if system_prefers_dark() else "light"
    return theme if theme in _PALETTES else "light"


def load_stylesheet(
    theme: str = "light",
    font_family: str | None = None,
    font_size: float = 10.5,
    terminal_font: str | None = None,
    terminal_size: int | None = None,
) -> str:
    """Build the QSS string for *theme* with the given font tokens filled in."""
    template = _THEME_FILE.read_text(encoding="utf-8")
    palette = dict(_PALETTES[resolve_theme(theme)])
    ui_font = font_family or detect_ui_font()
    terminal_family = terminal_font or DEFAULT_FONT_FAMILY
    palette["font_family"] = f'"{ui_font}"'
    palette["font_size"] = f"{font_size}pt"
    palette["terminal_font"] = f'"{terminal_family}"'
    palette["terminal_size"] = f"{terminal_size if terminal_size is not None else DEFAULT_FONT_SIZE}pt"

    def replace(match: "re.Match[str]") -> str:
        return palette.get(match.group(1), match.group(0))

    return _TOKEN_RE.sub(replace, template)
