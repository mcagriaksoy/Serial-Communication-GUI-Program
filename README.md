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

The COM port tool has the following features:

It supports multiple COM ports and can detect the available ports automatically.
It allows users to configure the parameters of the serial communication, such as baud rate.
It provides a user-friendly interface that shows the transmitted and received data in hexadecimal, decimal, ASCII, or binary formats.
It allows users to save and load the data to and from files.

## Usage

The COM port tool is compatible with:
[![OS - Linux](https://img.shields.io/badge/OS-Linux-blue?logo=linux&logoColor=white)](https://www.linux.org/ "Go to Linux homepage")
[![OS - Windows](https://img.shields.io/badge/OS-Windows-blue?logo=windows&logoColor=white)](https://www.microsoft.com/ "Go to Microsoft homepage")

1. Run the program.
2. Select a serial port and configure parameters.
3. Start communication using the **Start** button.
4. Send or receive data as needed.
5. Save received data or clear buffers using the respective buttons.

![Project SS](https://github.com/mcagriaksoy/Serial-Communication-GUI-Program/blob/master/img/Screenshot_v2025_04.jpg)

If you encounter any problems while using the COM port tool, try these solutions:

Make sure that the COM port is not used by another application or device.
Make sure that the parameters of the serial communication match with those of the device you are communicating with.
Make sure that you have sufficient permissions to access the COM port.
If you have any questions or feedback, please contact me.

## Dependencies

[![PySide - >= 6.0](https://img.shields.io/badge/PySide->_6.0-2ea44f)](https://wiki.python.org/moin/PySide)
[![PySide_sip - >= 13.0](https://img.shields.io/badge/PySide_sip->_13.0-2ea44f)](https://pypi.org/project/PySide6-sip/)
[![PySerial - >= 3.0](https://img.shields.io/badge/PySide->_3.0-2ea44f)](https://pypi.org/project/pyserial/)

<h2>Documentation</h2>
<div align="center">
<a href="/docs/" title="Go to project documentation"><img src="https://img.shields.io/badge/view-Documentation-blue?style=for-the-badge" alt="view - Documentation"></a>

</div>
<h2>Executable Command</h2>
The following command have been used to create AFCOM.exe

```
pyinstaller --noconfirm --onefile --windowed --icon "ui/icon.ico"  "src/main.py"

```

## Changes

### V1.4.0 - 2025 Update

Feature: Added basic_view_enabled and advanced_view_enabled methods to toggle UI layouts visibility.
Implemented start_loop and stop_loop for managing serial communication with threading.
Added on_save_txt_button_clicked to save received data to a .txt file.

Improvement: Enhanced error handling for serial communication and worker threads.
Added visual feedback for serial port selection and connection status.

Bug Fix: Fixed UI responsiveness during active serial communication.

Refactor: Organized serial communication logic into reusable methods.

</div>
<h2>License</h2>
Released under <a href="/LICENSE">GNU General Public License v3.0</a> by <a href="https://github.com/mcagriaksoy">@mcagriaksoy</a>.

![AFCOM Icon](https://github.com/mcagriaksoy/Serial-Communication-GUI-Program/blob/master/img/icon.png)
