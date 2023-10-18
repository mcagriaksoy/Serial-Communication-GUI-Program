__author__ = 'Mehmet Cagri Aksoy - github.com/mcagriaksoy'
__annotations__ = 'Serial Communication GUI Program'

# IMPORTS
import sys

try:
    import serial
    import serial.tools.list_ports
    from serial import SerialException
    from PyQt6.QtCore import QObject, QThread, pyqtSignal, pyqtSlot
    from PyQt6.QtWidgets import (QApplication, QMainWindow, QMessageBox)
    from PyQt6.uic import loadUi
except ImportError as e:
    print("Import Error! Please install the required libraries: " + str(e))
    sys.exit(1)
# IMPORTS END
# GLOBAL VARIABLES
SERIAL_INFO = serial.Serial()

#Port Detection START
try:
    PORTS = [
        p.device
        for p in serial.tools.list_ports.comports()
        if 'USB' in p.description
    ]

    if not PORTS:
        print("There is no device exist on serial port!")
        PORTS = "-"
    elif len(PORTS) > 1:
        print("Available serial PORTS are: " + str(PORTS))
        SERIAL_INFO = serial.Serial(PORTS[0], 9600)
except SerialException as e:
    print("Serial Exception! Please check the serial port: " + str(e))
    sys.exit(1)
#Port Detection END

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

        loadUi('..\\ui\\main_window.ui', self)

        self.thread = None
        self.worker = None
        self.start_button.clicked.connect(self.start_loop)
        self.label_11.setText(PORTS[0])

    def print_message_on_screen(self, text):
        """ Print the message on the screen """
        msg = QMessageBox()
        msg.setWindowTitle("Warning!")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(text)
        msg.exec()

    def start_loop(self):
        """ Start the loop """
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
        self.start_button.setEnabled(True)

    def on_send_data_button_clicked(self):
        """ Send data to serial port """
        mytext = self.textEdit_2.toPlainText()
        print(mytext.encode())
        SERIAL_INFO.write(mytext.encode())

def start_ui_design():
    """ Start the UI Design """
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
