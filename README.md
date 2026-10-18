```

 .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |      __      | || |  _________   | || |     ______   | || |     ____     | || | ____    ____ | |
| |     /  \     | || | |_   ___  |  | || |   .' ___  |  | || |   .'    `.   | || ||_   \  /   _|| |
| |    / /\ \    | || |   | |_  \_|  | || |  / .'   \_|  | || |  /  .--.  \  | || |  |   \/   |  | |
| |   / ____ \   | || |   |  _|      | || |  | |         | || |  | |    | |  | || |  | |\  /| |  | |
| | _/ /    \ \_ | || |  _| |_       | || |  \ `.___.'\  | || |  \  `--'  /  | || | _| |_\/_| |_ | |
| ||____|  |____|| || | |_____|      | || |   `._____.'  | || |   `.____.'   | || ||_____||_____|| |
| |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
```

The AFCOM (aka Serial communication GUI program) tool is a software application that allows users to send and receive data via the serial port (COM port) of their computer.
The tool can be used for various purposes, such as testing, debugging, or communicating with other devices that use the serial protocol.

<a href="https://github.com/mcagriaksoy/Serial-Communication-GUI-Program" title="Go to GitHub repo"><img src="https://img.shields.io/static/v1?label=mcagriaksoy&message=Serial-Communication-GUI-Program&color=blue&logo=github" alt="mcagriaksoy - Serial-Communication-GUI-Program"></a>
<a href="https://github.com/mcagriaksoy/Serial-Communication-GUI-Program/releases/"><img src="https://img.shields.io/github/tag/mcagriaksoy/Serial-Communication-GUI-Program?include_prereleases=&sort=semver&color=blue" alt="GitHub tag"></a>
<a href="#license"><img src="https://img.shields.io/badge/License-GPL_V3-red" alt="License"></a>
<a href="https://github.com/mcagriaksoy/Serial-Communication-GUI-Program/issues"><img src="https://img.shields.io/github/issues/mcagriaksoy/Serial-Communication-GUI-Program" alt="issues - Serial-Communication-GUI-Program"></a>

[![Hosted with GH Pages](https://img.shields.io/badge/Hosted_with-GitHub_Pages-blue?logo=github&logoColor=white)](https://pages.github.com/ "Go to GitHub Pages homepage")

## Features

The AFCOM client has the following features:

- Automatically detects the available serial ports (Linux, Windows, macOS).
- Configures every common serial parameter: baud rate, data bits, parity,
  stop bits, flow control, timeout and line ending.
- Displays received data in a scrollable terminal with ANSI colour support and
  optional per-line timestamps.
- Sends data with a configurable CR / LF / CRLF line ending (press Enter to
  send).
- Shows live RX / TX byte counters and the connected device's details.
- Saves the terminal output to a text file.
- Ships with **dark and light themes** and an **English / Turkish** interface.
- Lets you choose the terminal font and size.

## Usage

The COM port tool is compatible with:
[![OS - Linux](https://img.shields.io/badge/OS-Linux-blue?logo=linux&logoColor=white)](https://www.linux.org/ "Go to Linux homepage")
[![OS - Windows](https://img.shields.io/badge/OS-Windows-blue?logo=windows&logoColor=white)](https://www.microsoft.com/ "Go to Microsoft homepage")

1. Run the program.
2. Press **Scan ports** and select a serial port.
3. Match the parameters (baud rate, data bits, parity, stop bits, flow control)
   to your device.
4. Press **CONNECT** to start communication.
5. Send data from the input box (press **Enter** or click **Send**).
6. Save received data or clear the buffers using the menus or the **Clear**
   button.

### Main UI
![Project SS](https://github.com/mcagriaksoy/Serial-Communication-GUI-Program/blob/master/img/ui.jpg)

### UI - Settings
![Project SS](https://github.com/mcagriaksoy/Serial-Communication-GUI-Program/blob/master/img/ui_settings.jpg)

### UI - Simple view
![Project SS](https://github.com/mcagriaksoy/Serial-Communication-GUI-Program/blob/master/img/ui_simple.jpg)

If you encounter any problems while using the COM port tool, try these solutions:

Make sure that the COM port is not used by another application or device.
Make sure that the parameters of the serial communication match with those of the device you are communicating with.
Make sure that you have sufficient permissions to access the COM port.
If you have any questions or feedback, please contact me.

## Dependencies

[![Python](https://img.shields.io/badge/Python-3.10%2B-2ea44f)](https://www.python.org/)
[![PySide6](https://img.shields.io/badge/PySide6-%3E%3D6.6-2ea44f)](https://pypi.org/project/PySide6/)
[![pyserial](https://img.shields.io/badge/pyserial-%3E%3D3.5-2ea44f)](https://pypi.org/project/pyserial/)

```bash
pip install -r requirements.txt
```

<h2>Documentation</h2>
<div align="center">
<a href="/docs/" title="Go to project documentation"><img src="https://img.shields.io/badge/view-Documentation-blue?style=for-the-badge" alt="view - Documentation"></a>

</div>

## Installation

Install the released package from PyPI:

```bash
pip install AFCOM
afcom
```

## Running from source

```bash
python main.py
```

## Project structure

```
main.py                 # entry point
src/
  app.py                # QApplication bootstrap
  main_window.py        # main window controller
  serial_worker.py      # background serial reader (QThread)
  serial_ports.py       # cross-platform port discovery
  settings_store.py     # JSON preferences
  settings_dialog.py    # Preferences dialog
  theme.py              # dark / light palettes
  translations.py       # English / Turkish strings
  actions.py            # menu actions (save, about, help, updates)
  ansi.py               # ANSI colour -> HTML
  ui_loader.py          # loads / regenerates the Qt Designer UI
  constants.py          # metadata, paths, defaults
ui/
  *.ui                  # Qt Designer layouts (source of truth)
  theme.qss             # central stylesheet template
  build_ui.py           # regenerate the .py modules from the .ui files
test/                   # pytest unit tests
```

The `ui/*.ui` files are the single source of truth. Edit them in Qt Designer
(or manually) and regenerate the Python modules with:

```bash
python ui/build_ui.py
```

At startup the application also regenerates any `.ui` file that is newer than
its generated `.py` equivalent, so you normally do not need to run this by hand.

## Tests

```bash
pytest test/
```

<h2>Executable Command</h2>
The following command builds a standalone executable:

```
pyinstaller main.spec
```

For the CI/release build (versioned name) use:

```bash
python scripts/build_windows.py
```

## Releasing

Pushing a version tag publishes everything automatically. The tag must match
`APP_VERSION` in `src/constants.py`. The workflows must be present in the
repository (committed to `master`) before the tag is pushed:

```bash
# bump APP_VERSION first, commit and push the branch:
git add -A
git commit -m "Release v1.9.0"
git push origin master

# then tag the same commit and push the tag:
git tag v1.9.0
git push origin v1.9.0
```

Two GitHub Actions workflows run on the tag:

- `.github/workflows/release.yml` — builds the Windows portable executable and
  the Inno Setup installer, then attaches them to the GitHub Release.
- `.github/workflows/publish-pypi.yml` — builds the sdist/wheel and publishes
  `AFCOM` to PyPI (via Trusted Publishing / OIDC, no token needed).

<h2>License</h2>
Released under <a href="/LICENSE">GNU General Public License v3.0</a> by <a href="https://github.com/mcagriaksoy">@mcagriaksoy</a>.

![AFCOM Icon](https://github.com/mcagriaksoy/Serial-Communication-GUI-Program/blob/master/img/icon.png)
