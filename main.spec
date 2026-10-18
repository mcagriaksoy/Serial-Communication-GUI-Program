# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller build definition for AFCOM Client.

Build with::

    pyinstaller main.spec

The CI release workflow sets ``AFCOM_EXE_NAME`` so the released binary is
versioned (``AFCOM_v<version>_portable_win64``); local builds fall back to
``AFCOM``.
"""

import os

_exe_name = os.environ.get("AFCOM_EXE_NAME", "AFCOM").strip() or "AFCOM"

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('ui/theme.qss', 'ui'),
        ('ui/icon.ico', 'ui'),
        ('ui/main_window.ui', 'ui'),
        ('ui/settings.ui', 'ui'),
        ('ui/help.ui', 'ui'),
    ],
    hiddenimports=[
        'ui.main_window',
        'ui.settings',
        'ui.help',
        'ui.resources_rc',
        'serial.tools.list_ports',
        'serial.tools.list_ports_common',
        'serial.tools.list_ports_windows',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name=_exe_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='ui/icon.ico',
)
