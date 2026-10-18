# -*- coding: utf-8 -*-
"""Unit tests for the AFCOM Client core modules.

These tests deliberately avoid creating a ``QApplication`` or opening real
serial ports so they can run in any headless CI environment.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.ansi import ansi_to_html, strip_ansi_codes
from src.constants import DEFAULT_SETTINGS
from src.serial_ports import display_name, port_names
from src.settings_store import SettingsStore
from src.theme import load_stylesheet, resolve_theme
from src.translations import Translator


# --------------------------------------------------------------------------
# ansi
# --------------------------------------------------------------------------
def test_strip_ansi_codes_removes_sequences():
    assert strip_ansi_codes("\x1b[31mred\x1b[0m") == "red"


def test_ansi_to_html_escapes_markup():
    html = ansi_to_html("a < b & c > d")
    assert "&lt;" in html and "&amp;" in html and "&gt;" in html


def test_ansi_to_html_adds_colour_span():
    html = ansi_to_html("\x1b[32mok\x1b[0m")
    assert "color:" in html
    assert "ok" in html


def test_ansi_to_html_converts_newlines():
    assert "<br>" in ansi_to_html("line1\nline2")


# --------------------------------------------------------------------------
# settings store
# --------------------------------------------------------------------------
def test_settings_defaults_when_file_missing(tmp_path):
    store = SettingsStore(tmp_path / "missing.json")
    assert store.get("theme") == DEFAULT_SETTINGS["theme"]


def test_settings_roundtrip(tmp_path):
    path = tmp_path / "settings.json"
    store = SettingsStore(path)
    store.set("font_size", 17)
    store.save()

    reloaded = SettingsStore(path)
    assert reloaded.get("font_size") == 17


def test_settings_ignores_corrupt_file(tmp_path):
    path = tmp_path / "settings.json"
    path.write_text("{ not valid json", encoding="utf-8")
    store = SettingsStore(path)
    assert store.get("theme") == DEFAULT_SETTINGS["theme"]


# --------------------------------------------------------------------------
# translations
# --------------------------------------------------------------------------
def test_translator_falls_back_to_english():
    translator = Translator("fr")  # unsupported -> english
    assert translator.tr("menu.file") == "File"


def test_translator_switches_language():
    translator = Translator("en")
    translator.set_language("tr")
    assert translator.tr("menu.file") == "Dosya"


# --------------------------------------------------------------------------
# theme
# --------------------------------------------------------------------------
def test_resolve_theme_system_returns_known_palette():
    assert resolve_theme("system") in {"dark", "light"}


@pytest.mark.parametrize("theme", ["dark", "light"])
def test_stylesheet_has_no_unresolved_tokens(theme):
    import re

    qss = load_stylesheet(theme=theme)
    # Only real @token placeholders matter; the header comment may mention "@".
    assert not re.search(r"@[a-z_]+", qss)


# --------------------------------------------------------------------------
# serial ports
# --------------------------------------------------------------------------
def test_port_names_returns_list():
    names = port_names()
    assert isinstance(names, list)


def test_display_name_hides_dev_prefix():
    assert display_name("/dev/ttyUSB0") == "ttyUSB0"
    assert display_name("/dev/ttyS0") == "ttyS0"
    # Windows ports and unrelated strings are left untouched.
    assert display_name("COM3") == "COM3"
    assert display_name("tty") == "tty"
