#!/usr/bin/env python3
"""Build the AFCOM Client Windows portable executable with PyInstaller.

This is the CI/release entry point.  It produces a single-file windowed
executable named ``AFCOM_v<version>_portable_win64.exe`` in ``dist`` (or the
directory passed with ``--dist-dir``).

The resulting executable is what the Inno Setup script
(``installer/afcom.iss``) packages into the Windows installer.  Run it locally
on any platform to validate the PyInstaller configuration.

    python scripts/build_windows.py [--version 1.9.0] [--dist-dir dist]
"""
from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SPEC_FILE = REPO_ROOT / "main.spec"
CONSTANTS_FILE = REPO_ROOT / "src" / "constants.py"


def get_version() -> str:
    """Read ``APP_VERSION`` from ``src/constants.py``."""
    content = CONSTANTS_FILE.read_text(encoding="utf-8")
    match = re.search(r'APP_VERSION\s*=\s*["\']([^"\']+)["\']', content)
    if not match:
        raise SystemExit("Could not determine version from src/constants.py")
    return match.group(1)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", help="Override version (default: src/constants.py).")
    parser.add_argument(
        "--dist-dir",
        default=str(REPO_ROOT / "dist"),
        help="Directory for the built executable (default: dist/).",
    )
    parser.add_argument(
        "--name",
        help="Output base name (default: AFCOM_v<version>_portable_win64).",
    )
    args = parser.parse_args(argv)

    version = args.version or get_version()
    name = args.name or f"AFCOM_v{version}_portable_win64"
    dist_dir = Path(args.dist_dir).resolve()
    build_dir = REPO_ROOT / "build"

    for folder in (dist_dir, build_dir):
        shutil.rmtree(folder, ignore_errors=True)
    dist_dir.mkdir(parents=True, exist_ok=True)

    env = dict(os.environ)
    env["AFCOM_VERSION"] = version
    env["AFCOM_EXE_NAME"] = name

    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--clean",
        "--distpath",
        str(dist_dir),
        "--workpath",
        str(build_dir),
        str(SPEC_FILE),
    ]
    print("Running:", " ".join(cmd), flush=True)
    subprocess.run(cmd, cwd=str(REPO_ROOT), check=True, env=env)

    exe = dist_dir / f"{name}.exe"
    if not exe.exists():
        fallback = dist_dir / name  # non-Windows builds have no .exe suffix
        exe = fallback if fallback.exists() else exe
    print(f"Built: {exe}")

    github_output = os.environ.get("GITHUB_OUTPUT")
    if github_output:
        with open(github_output, "a", encoding="utf-8") as handle:
            handle.write(f"exe={exe}\n")
            handle.write(f"name={exe.name}\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
