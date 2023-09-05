###############################################################################################

#COM Port Tool Documentation
Author: Mehmet Cagri Aksoy 2023
##Introduction
The AFCOM port tool is a software application that allows users to send and receive data via the serial port (COM port) of their computer. 

The tool can be used for various purposes, such as testing, debugging, or communicating with other devices that use the serial protocol.

##Features
The COM port tool has the following features:

It supports multiple COM ports and can detect the available ports automatically.
It allows users to configure the parameters of the serial communication, such as baud rate.
It provides a user-friendly interface that shows the transmitted and received data in hexadecimal, decimal, ASCII, or binary formats.
It allows users to save and load the data to and from files.

##Usage
The COM port tool is compatible with Windows/Unix/Linux operating systems. 
To use the tool, follow these steps:

python main.py

![Project](https://github.com/mcagriaksoy/img/blob/master/screenshot.jpg)


If you encounter any problems while using the COM port tool, try these solutions:

Make sure that the COM port is not used by another application or device.
Make sure that the parameters of the serial communication match with those of the device you are communicating with.
Make sure that you have sufficient permissions to access the COM port.
If you have any questions or feedback, please contact me.


Many Thanks to JulianRene also!
###############################################################################################


# 2022 December UPDATE
V1.2 INTRODUCED
CHANGELOG:
- Forked version of JulianRene is merged into master: https://github.com/JulianRene/Serial-GUI-Com
Thank you JulianRene!

- Source code updated
- Bug fixes and performance updates
- GUI updated, now better! faster!

New UI:
![Project](https://github.com/mcagriaksoy/Serial-Communication-GUI-Program/blob/master/1.png)


# 2022 February UPDATE
V1.1 INTRODUCED

CHANGELOG:
- Source code updated
- Bug fixes and performance updates
- GUI updated, now better! faster!
- English language is added.

For serial communication tests, the "serial.ino" file can be investigated!

# 2023 UPDATE Agenda
- Pyuic5 integration
- Putty like UI

--------------------------------------------------

# NOTES FROM 2018
NOTE: Program Language is Turkish, but It can be easily adopted and translated to other languages freely.

# Serial-Communication-GUI-Program
PyQt, Serial Communication between different hardware
During my test releases, I have tried NodeMCU and Arduino cards. Also, the program tested on Windows 10 x64 and Ubuntu 16.04.

# Feature 1
On the right side of the GUI, you can access the port options. After you selected baud rate, port name, etc. you can save your settings via "kaydet" button which means save exactly.

# Feature 2
Python PyQt threading, multitasking feature added. Due to multitasking function, the program does not crash (one of the thread keen on serial port listen, other does rest of tasks) and uses less memory. 
It has different 2 blocks of code. 
One worker runs in one thread also the main side of the program runs at the same time.
```
class Worker(QObject):
    finished = pyqtSignal()
    intReady = pyqtSignal(str)
    @pyqtSlot()
    def __init__(self):
        super(Worker, self).__init__()
        self.working = True
    def work(self):
        while self.working:
            line = ser.readline().decode('utf-8')
            # print(line)
            time.sleep(0.05)
            self.intReady.emit(line)
            # if line != '':
            # self.textEdit_3.append(line)
        self.finished.emit()
 ```       

# Multitasking
Thread1 listen COM port and convert data to UTF-8

Thread2 send data to serially connected hardware (Arduino, esp32, raspberry pi, etc.) also, control the buttons

# PyQt5
The program is using Pyqt5 instead of the 4th version of PyQt.

