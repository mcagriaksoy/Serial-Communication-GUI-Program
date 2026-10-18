# -*- coding: utf-8 -*-
"""Loading of the Qt Designer ``.ui`` files.

The ``.ui`` files in ``ui/`` remain the single source of truth.  At startup we
regenerate the corresponding Python modules with ``pyside6-uic`` whenever the
``.ui`` file is newer than the generated module (development only).  The
generated modules are what the application imports, which keeps bundled builds
simple and reliable.
"""

from __future__ import annotations

import importlib
import shutil
import subprocess
import sys
from pathlib import Path

from .constants import UI_DIR

# (designer file, generated module, generated class)
UI_MODULES = [
    ("main_window.ui", "main_window.py", "Ui_main_window"),
    ("settings.ui", "settings.py", "Ui_Dialog"),
    ("help.ui", "help.py", "Ui_HelpDialog"),
]


def _is_frozen() -> bool:
    return getattr(sys, "frozen", False)


def _uic_command() -> list[str] | None:
    executable = shutil.which("pyside6-uic")
    if executable:
        return [executable]
    try:
        import PySide6.scripts.pyside_tool  # noqa: F401
    except Exception:
        return None
    return [
        sys.executable,
        "-c",
        "from PySide6.scripts.pyside_tool import uic; import sys; sys.exit(uic())",
    ]


def _normalize_generated(path: Path) -> None:
    """Fix the resource import so the module works inside the ``ui`` package."""
    try:
        source = path.read_text(encoding="utf-8")
    except OSError:
        return
    if "from . import resources_rc" in source:
        return
    patched = source.replace("import resources_rc", "from . import resources_rc")
    if patched != source:
        path.write_text(patched, encoding="utf-8")


def ensure_generated(force: bool = False) -> None:
    """Regenerate stale ``.py`` files from their ``.ui`` counterparts.

    Does nothing when running from a frozen bundle (the generated modules are
    bundled at build time) or when ``pyside6-uic`` is unavailable.
    """
    if _is_frozen():
        return
    command = _uic_command()
    if command is None:
        return

    for ui_name, py_name, _class_name in UI_MODULES:
        ui_path = UI_DIR / ui_name
        py_path = UI_DIR / py_name
        if not ui_path.exists():
            continue
        needs_build = force or not py_path.exists() or ui_path.stat().st_mtime > py_path.stat().st_mtime
        if not needs_build:
            continue
        try:
            subprocess.run(
                [*command, str(ui_path), "-o", str(py_path)],
                check=True,
                capture_output=True,
            )
            _normalize_generated(py_path)
        except (OSError, subprocess.CalledProcessError) as exc:  # pragma: no cover
            print(f"[ui] Could not regenerate {py_name}: {exc}", file=sys.stderr)


def load_ui_class(module_name: str, class_name: str):
    """Import a generated UI class from the ``ui`` package."""
    module = importlib.import_module(f"ui.{module_name}")
    return getattr(module, class_name)
