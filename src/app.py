# -*- coding: utf-8 -*-
"""Application bootstrap: create the QApplication and show the main window."""

from __future__ import annotations

import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from .constants import APP_NAME, APP_TITLE, APP_VERSION, ICON_PATH, PROJECT_ROOT
from .main_window import MainWindow
from .settings_store import SettingsStore
from .ui_loader import ensure_generated


def _ensure_project_on_path() -> None:
    root = str(PROJECT_ROOT)
    if root not in sys.path:
        sys.path.insert(0, root)


def run(argv: list[str] | None = None) -> int:
    """Start the application and return the Qt exit code."""
    _ensure_project_on_path()
    ensure_generated()

    app = QApplication.instance() or QApplication(argv if argv is not None else sys.argv)
    app.setApplicationName(APP_NAME)
    app.setApplicationDisplayName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setDesktopFileName("afcom-client")

    # Fusion renders our stylesheet consistently across platforms.
    app.setStyle("Fusion")

    if ICON_PATH.exists():
        app.setWindowIcon(QIcon(str(ICON_PATH)))

    settings = SettingsStore()
    window = MainWindow(settings)
    window.setWindowTitle(APP_TITLE)
    window.show()

    return app.exec()
