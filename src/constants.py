# -*- coding: utf-8 -*-
"""Application-wide constants, paths and defaults.

This module is intentionally free of any Qt import so that it can be used from
build scripts and tests without a display server.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Metadata
# ---------------------------------------------------------------------------
APP_NAME = "AFCOM Client"
APP_TITLE = f"{APP_NAME} - Serial Communication GUI"
APP_AUTHOR = "Mehmet Cagri Aksoy"
APP_REPO = "mcagriaksoy/Serial-Communication-GUI-Program"
APP_URL = f"https://github.com/{APP_REPO}"
APP_RELEASES_URL = f"{APP_URL}/releases"
APP_TAGS_API = f"https://api.github.com/repos/{APP_REPO}/tags"
APP_DONATE_URL = "https://buymeacoffee.com/mcagriaksoy"

APP_VERSION = "1.9.0"
# Kept for backwards compatibility with code importing ``__version__``.
__version__ = APP_VERSION

__author__ = f"{APP_AUTHOR} - github.com/mcagriaksoy"
__license__ = "GPLv3"
__status__ = "Production"

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
UI_DIR = PROJECT_ROOT / "ui"
ASSETS_DIR = UI_DIR
ICON_PATH = UI_DIR / "icon.ico"
THEME_DIR = UI_DIR / "themes"

# User-writable settings live next to the source in development, but a proper
# per-user location is used when the app runs from a bundled (installed) build,
# because the PyInstaller extraction directory is temporary and read-only.
# User-writable settings live next to the source in development, but a proper
# per-user location is used when the app runs from a bundled (installed) build
# or from a pip-installed wheel, because those directories are temporary or
# read-only.
def _per_user_settings_path() -> Path:
    if sys.platform.startswith("win"):
        base = os.environ.get("APPDATA") or os.path.expanduser("~")
        return Path(base) / "AFCOM" / "settings.json"
    if sys.platform == "darwin":
        return Path.home() / "Library" / "Application Support" / "AFCOM" / "settings.json"
    base = os.environ.get("XDG_CONFIG_HOME") or os.path.join(os.path.expanduser("~"), ".config")
    return Path(base) / "afcom" / "settings.json"


def _settings_path() -> Path:
    frozen = getattr(sys, "frozen", False)
    # A source checkout keeps a ``.git`` directory; an installed wheel does not.
    is_checkout = (PROJECT_ROOT / ".git").exists()
    if frozen or not is_checkout:
        return _per_user_settings_path()
    return PROJECT_ROOT / "src" / "settings.json"


SETTINGS_FILE = _settings_path()

# ---------------------------------------------------------------------------
# Serial defaults / dictionaries
# ---------------------------------------------------------------------------
BAUDRATE_LIST = [
    "110", "300", "600", "1200", "2400", "4800", "9600", "14400",
    "19200", "28800", "38400", "57600", "115200", "230400", "460800",
    "921600",
]
DATA_BITS_LIST = ["8", "7", "6", "5"]
PARITY_LIST = ["None", "Even", "Odd", "Mark", "Space"]
STOP_BITS_LIST = ["1", "1.5", "2"]
TIMEOUT_LIST = ["0.1", "0.5", "1", "2", "3", "5"]
FLOW_CONTROL_LIST = ["None", "Xon/Xoff", "RTS/CTS", "DSR/DTR"]
LINE_ENDING_LIST = ["None", "LF", "CR", "CRLF"]

DEFAULT_FONT_FAMILY = "Monospace"
DEFAULT_FONT_SIZE = 11
DEFAULT_THEME = "system"

DEFAULT_SETTINGS = {
    "theme": DEFAULT_THEME,
    "font_family": DEFAULT_FONT_FAMILY,
    "font_size": DEFAULT_FONT_SIZE,
    "language": "en",
    "timestamps": False,
}
