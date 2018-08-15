# Serial-Communication-GUI-Program
PyQt, Serial Communication between different hardwares
During my test releases I have tried NodeMCU and Arduino cards. Also the program tested on Windows and Ubuntu software.

New Feature:
Python PyQt threading, multitasking feature added.
Thanks to multitasking function, now program do not crashes and uses optimal memory. 
It has different 2 block of code. One of worker runs in one thread also main side of program runs at the same time.
Thread1=listen COM port and calculate .
Thread2=send data to arduino etc. Control the buttons.



PyQt5
The program is used Pyqt5 which is better than 4th version of PyQt.


