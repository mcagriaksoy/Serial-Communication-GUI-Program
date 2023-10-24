# -*- coding: utf-8 -*-
"""
AFCOM - Serial Communication GUI Program
Cannot be used directly, it is a part of main.py
"""

__author__ = 'Mehmet Cagri Aksoy - github.com/mcagriaksoy'
__annotations__ = 'AFCOM - Serial Communication GUI Program'

# IMPORTS
import sys
import glob
import os

# Runtime Type Checking
PROGRAM_TYPE_DEBUG = 1
PROGRAM_TYPE_RELEASE = 0

try:
    import serial
    import serial.tools.list_ports
    from serial import SerialException
    from PyQt6.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
    from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox

    if (PROGRAM_TYPE_DEBUG):
        from PyQt6.uic import loadUi
    else: # PROGRAM_TYPE_RELEASE
        from ui_config import Ui_main_window
except ImportError as e:
    print("Import Error! Please install the required libraries: " + str(e))
    sys.exit(1)

# GLOBAL VARIABLES
SERIAL_INFO = serial.Serial()
PORTS = []

def get_serial_port():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

# MULTI-THREADING
class Worker(QObject):
    """ Worker Thread """
    finished = pyqtSignal()
    serial_data = pyqtSignal(str)

    @pyqtSlot()
    def __init__(self):
        super(Worker, self).__init__()
        self.working = True

    def work(self):
        """ Read data from serial port """
        while self.working:
            try:
                char = SERIAL_INFO.read()
                h = char.hex()
                self.serial_data.emit(h)
            except SerialException:
                # Emit last error message before die!
                self.serial_data.emit("ERROR_SERIAL_EXCEPTION")
                self.working = False
            self.finished.emit()

class MainWindow(QMainWindow):
    """ Main Window """
    def __init__(self):
        """ Initialize Main Window """
        QMainWindow.__init__(self)

        PORTS = get_serial_port()

        self.thread = None
        self.worker = None
        self.start_button.clicked.connect(self.start_loop)
        self.comboBox_3.addItems(PORTS)

    def print_message_on_screen(self, text):
        """ Print the message on the screen """
        msg = QMessageBox()
        msg.setWindowTitle("Warning!")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(text)
        msg.exec()

    def establish_serial_communication(self):
        """ Establish serial communication """
        port = self.comboBox_3.currentText()
        baudrate = self.comboBox_1.currentText()
        timeout = self.comboBox.currentText()
        length = self.comboBox_2.currentText()
        parity = self.comboBox_4.currentText()
        stopbits = self.comboBox_5.currentText()
        SERIAL_INFO = serial.Serial(port=str(port),
                                    baudrate=int(baudrate, base=10),
                                    timeout=float(timeout),
                                    bytesize=int(length, base=10),
                                    parity = parity[0], #get first character
                                    stopbits = float(stopbits)
                                    )

    def start_loop(self):
        """ Start the loop """
        try:
            self.establish_serial_communication()
        except SerialException:
            self.print_message_on_screen(
                "Exception occured while trying establish serial communication!")

        try:
            self.worker = Worker()   # a new worker to perform those tasks
            self.thread = QThread()  # a new thread to run our background tasks in
            # move the worker into the thread, do this first before connecting the signals
            self.worker.moveToThread(self.thread)
            # begin our worker object's loop when the thread starts running
            self.thread.started.connect(self.worker.work)
            self.worker.serial_data.connect(self.read_data_from_thread)
            # stop the loop on the stop button click
            self.end_button.clicked.connect(self.stop_loop)
            # tell the thread it's time to stop running
            self.worker.finished.connect(self.thread.quit)
            # have worker mark itself for deletion
            self.worker.finished.connect(self.worker.deleteLater)
            # have thread mark itself for deletion
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.start()
        except RuntimeError:
            self.print_message_on_screen("Exception in Worker Thread!")

    def stop_loop(self):
        """ Stop the loop """
        self.worker.working = False
        self.textEdit.setText('Stopped!')

    def read_data_from_thread(self, serial_data):
        """ Write the result to the text edit box"""
        # self.textEdit_3.append("{}".format(i))
        if "ERROR_SERIAL_EXCEPTION" in serial_data:
            self.print_message_on_screen("Serial Exception! Please check the serial port")
            self.label_5.setText("NOT CONNECTED!")
            self.label_5.setStyleSheet('color: red')
        else:
            self.comboBox.setEnabled(False)
            self.comboBox_1.setEnabled(False)
            self.comboBox_2.setEnabled(False)
            self.comboBox_3.setEnabled(False)
            self.comboBox_4.setEnabled(False)
            self.comboBox_5.setEnabled(False)
            self.save_button.setEnabled(False)
            self.start_button.setEnabled(False)

            self.textEdit.setText('Data Gathering...')
            self.label_5.setText("CONNECTED!")
            self.label_5.setStyleSheet('color: green')
            self.textEdit_3.insertPlainText("{}".format(serial_data))

    # Save the settings
    def on_save_button_clicked(self):
        """ Save the settings """
        if self.x != 0:
            self.textEdit.setText('Settings Saved!')
        else:
            self.textEdit.setText('Please enter port and speed!')

    def on_save_txt_button_clicked(self):
        """ Save the values to the TXT file"""
        with open('Output.txt', 'w', encoding='utf-8') as f:
            my_text = self.textEdit_3.toPlainText()
            f.write(my_text)
            f.close()

    def on_end_button_clicked(self):
        """ Stop the process """
        self.textEdit.setText('Stopped!')
        self.comboBox.setEnabled(True)
        self.comboBox_1.setEnabled(True)
        self.comboBox_2.setEnabled(True)
        self.comboBox_3.setEnabled(True)
        self.comboBox_4.setEnabled(True)
        self.comboBox_5.setEnabled(True)
        self.save_button.setEnabled(True)
        self.start_button.setEnabled(True)

    def on_send_data_button_clicked(self):
        """ Send data to serial port """
        mytext = self.textEdit_2.toPlainText()
        print(mytext.encode())
        SERIAL_INFO.write(mytext.encode())

def start_ui_design():
    """ Start the UI Design """
    app = QApplication(sys.argv)
    window_object = QMainWindow()

    if PROGRAM_TYPE_RELEASE:
        ui = Ui_main_window()
        ui.setupUi(window_object)
    elif PROGRAM_TYPE_DEBUG:
        file_path = os.path.join("../ui/main_window.ui")
        if not os.path.exists(file_path):
            print("UI File Not Found!")
            sys.exit(1)
        loadUi(file_path, window_object)

    window_object.show()
    sys.exit(app.exec())