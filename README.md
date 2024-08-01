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
<a href="#license"><img src="https://img.shields.io/badge/License-MIT-blue" alt="License"></a>
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

To use the tool, follow these steps:
First of all, please ensure that you installed dependencies already.

```
python main.py
```

Then the project can be run with:

```
pip install -r requirements.txt
```

![Project SS](https://github.com/mcagriaksoy/Serial-Communication-GUI-Program/blob/master/img/Screenshot_v2024_07.jpg)

Simple View and Night Mode have been introduced:

![Project SS](https://github.com/mcagriaksoy/Serial-Communication-GUI-Program/blob/master/img/Screenshot_v2024_07_2.jpg)

If you encounter any problems while using the COM port tool, try these solutions:

Make sure that the COM port is not used by another application or device.
Make sure that the parameters of the serial communication match with those of the device you are communicating with.
Make sure that you have sufficient permissions to access the COM port.
If you have any questions or feedback, please contact me.

## Dependencies

[![PyQt - >= 6.0](https://img.shields.io/badge/PyQt->_6.0-2ea44f)](https://wiki.python.org/moin/PyQt)
[![PyQt_sip - >= 13.0](https://img.shields.io/badge/PyQt_sip->_13.0-2ea44f)](https://pypi.org/project/PyQt6-sip/)
[![PySerial - >= 3.0](https://img.shields.io/badge/PyQt->_3.0-2ea44f)](https://pypi.org/project/pyserial/)

<h2>Documentation</h2>
<div align="center">
<a href="/docs/" title="Go to project documentation"><img src="https://img.shields.io/badge/view-Documentation-blue?style=for-the-badge" alt="view - Documentation"></a>

</div>
<h2>Executable Command</h2>
The following command have been used to create AFCOM.exe

```
pyinstaller --noconfirm --onefile --windowed --icon "ui/icon.ico"  "src/main.py"

```

</div>
<h2>License</h2>
Released under <a href="/LICENSE">GNU General Public License v3.0</a> by <a href="https://github.com/mcagriaksoy">@mcagriaksoy</a>.

![AFCOM Icon](https://github.com/mcagriaksoy/Serial-Communication-GUI-Program/blob/master/img/icon.png)
