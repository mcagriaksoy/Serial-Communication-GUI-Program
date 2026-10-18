# -*- coding: utf-8 -*-
"""Backwards-compatibility shim.

Historically the whole application lived in this module.  It has since been
split into focused modules under ``src/``.  This file re-exports the public
names so that older imports (and scripts) keep working.
"""

from __future__ import annotations

from .app import run
from .constants import APP_VERSION as __version__
from .main_window import MainWindow
from .serial_ports import port_names


def get_serial_port():
    """Return the list of available serial port names (legacy helper)."""
    return port_names()


def start_ui_design() -> int:
    """Start the application (legacy entry point used by ``main.py``)."""
    return run()


__all__ = ["MainWindow", "get_serial_port", "start_ui_design", "__version__"]
