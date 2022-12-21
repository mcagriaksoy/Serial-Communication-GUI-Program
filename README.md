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

