# -*- coding: utf-8 -*-
"""Packaging definition for the ``afcom-client`` distribution.

The application is a PySide6 desktop tool.  It is published to PyPI so users can
install it with::

    pip install afcom-client
    afcom-client

The graphical modules live in the ``src`` and ``ui`` packages and the Qt
Designer ``.ui`` resources are shipped as data files of the ``ui`` package.
"""
from __future__ import annotations

import re
from pathlib import Path

from setuptools import find_packages, setup

ROOT = Path(__file__).resolve().parent


def read_version() -> str:
    """Read ``APP_VERSION`` from ``src/constants.py`` (single source of truth)."""
    content = (ROOT / "src" / "constants.py").read_text(encoding="utf-8")
    match = re.search(r'APP_VERSION\s*=\s*["\']([^"\']+)["\']', content)
    return match.group(1) if match else "0.0.1"


long_description = ""
readme = ROOT / "README.md"
if readme.exists():
    long_description = readme.read_text(encoding="utf-8")

setup(
    name="AFCOM",
    version=read_version(),
    author="Mehmet Cagri Aksoy",
    description="AFCOM - a PySide6 serial communication GUI client.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mcagriaksoy/Serial-Communication-GUI-Program",
    project_urls={
        "Source": "https://github.com/mcagriaksoy/Serial-Communication-GUI-Program",
        "Releases": "https://github.com/mcagriaksoy/Serial-Communication-GUI-Program/releases",
        "Bug Tracker": "https://github.com/mcagriaksoy/Serial-Communication-GUI-Program/issues",
    },
    packages=find_packages(include=["src", "src.*", "ui", "ui.*"]),
    include_package_data=True,
    package_data={
        "ui": ["*.ui", "*.qss", "*.qrc", "*.ico", "*.png", "resource/*.svg"],
    },
    install_requires=["PySide6>=6.6", "pyserial>=3.5"],
    entry_points={
        "console_scripts": [
            "afcom=src.app:run",
        ],
    },
    python_requires=">=3.9",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Terminals :: Serial",
    ],
)
