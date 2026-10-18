#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate the Python modules from the Qt Designer ``.ui`` files.

Run this after editing any ``.ui`` file::

    python ui/build_ui.py

The application also regenerates stale files automatically at startup (see
``src/ui_loader.py``), so this script is mainly useful for packaging.
"""

from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path

UI_DIR = Path(__file__).resolve().parent
FILES = ["main_window", "settings", "help"]
QRC = [("resources.qrc", "resources_rc.py")]


def _uic() -> list[str]:
    exe = shutil.which("pyside6-uic")
    if exe:
        return [exe]
    return [
        sys.executable,
        "-c",
        "from PySide6.scripts.pyside_tool import uic; import sys; sys.exit(uic())",
    ]


def _rcc() -> list[str] | None:
    exe = shutil.which("pyside6-rcc")
    if exe:
        return [exe]
    try:
        import PySide6.scripts.pyside_tool  # noqa: F401
    except Exception:
        return None
    return [
        sys.executable,
        "-c",
        "from PySide6.scripts.pyside_tool import rcc; import sys; sys.exit(rcc())",
    ]


def _normalize(path: Path) -> None:
    source = path.read_text(encoding="utf-8")
    patched = source.replace("import resources_rc", "from . import resources_rc")
    if patched != source:
        path.write_text(patched, encoding="utf-8")


def main() -> int:
    command = _uic()
    for name in FILES:
        ui_path = UI_DIR / f"{name}.ui"
        py_path = UI_DIR / f"{name}.py"
        print(f"uic  {ui_path.name} -> {py_path.name}")
        subprocess.run([*command, str(ui_path), "-o", str(py_path)], check=True)
        _normalize(py_path)

    rcc = _rcc()
    if rcc is not None:
        for qrc, out in QRC:
            print(f"rcc  {qrc} -> {out}")
            subprocess.run([*rcc, str(UI_DIR / qrc), "-o", str(UI_DIR / out)], check=True)

    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
