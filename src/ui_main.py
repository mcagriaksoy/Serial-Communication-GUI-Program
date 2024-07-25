# -*- coding: utf-8 -*-
"""
AFCOM - Serial Communication GUI Program
Cannot be used directly, it is a part of main.py
"""

__author__ = 'Mehmet Cagri Aksoy - github.com/mcagriaksoy'
__annotations__ = 'AFCOM - Serial Communication GUI Program'
__version__ = '2024.05'
__license__ = 'MIT'
__status__ = 'Research'

# IMPORTS
from os import path, system
from sys import platform, exit, argv
from glob import glob

# Runtime Type Checking
PROGRAM_TYPE_DEBUG = 1
PROGRAM_TYPE_RELEASE = 0

try:
    import serial.tools.list_ports
    from serial import SerialException, Serial
except ImportError as e:
    print("Import Error! I am installing the PySerial library.")
    system("python -m pip install pyserial")

try:
    from PyQt6.QtCore import QObject, QThread, pyqtSignal
    from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog

    if (PROGRAM_TYPE_DEBUG):
        from PyQt6.uic import loadUi
    else:  # PROGRAM_TYPE_RELEASE
        from ui_config import Ui_main_window
except ImportError as e:
    print("Import Error! I am installing the required libraries: " + str(e))
    system("pip install {0}".format(str(e).split(" ")[-1]))

# GLOBAL VARIABLES
SERIAL_INFO = Serial()
PORTS = []
is_serial_port_established = False

def get_serial_port():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif platform.startswith('linux') or platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob('/dev/tty[A-Za-z]*')
    elif platform.startswith('darwin'):
        ports = glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = Serial(port)
            s.close()
            result.append(port)
        except SerialException:
            pass
    return result

# MULTI-THREADING
class Worker(QObject):
    """ Worker Thread """
    finished = pyqtSignal()
    serial_data = pyqtSignal(str)

    def __init__(self):
        super(Worker, self).__init__()
        self.working = True

    def work(self):
        """ Read data from serial port """
        while self.working:
            try:
                char = SERIAL_INFO.read()
                h = char.decode('utf-8')
                self.serial_data.emit(h)
            except SerialException as e:
                print(e)
                # Emit last error message before die!
                self.serial_data.emit("ERROR_SERIAL_EXCEPTION")
                self.working = False
            self.finished.emit()

class MainWindow(QMainWindow):
    """ Main Window """

    def __init__(self):
        """ Initialize Main Window """
        super(MainWindow, self).__init__()
        if PROGRAM_TYPE_DEBUG:
            file_path = path.join("../ui/main_window.ui")
            if not path.exists(file_path):
                print("UI File Not Found!")
                exit(1)
            loadUi(file_path, self)  # Load the .ui file
            self.show()  # Show the GUI

        PORTS = get_serial_port()

        self.thread = None
        self.worker = None

        self.start_button.clicked.connect(self.start_loop)
        self.refresh_button.clicked.connect(self.refresh_port)

        self.command_edit_1.clicked.connect(self.command1)
        self.command_edit_2.clicked.connect(self.command2)
        self.command_edit_3.clicked.connect(self.command3)
        self.command_edit_4.clicked.connect(self.command4)

        self.saved_command_1.clicked.connect(self.move_command1_to_text)
        self.saved_command_2.clicked.connect(self.move_command2_to_text)
        self.saved_command_3.clicked.connect(self.move_command3_to_text)
        self.saved_command_4.clicked.connect(self.move_command4_to_text)

        self.clear_buffer_button.clicked.connect(self.clear_buffer)

        self.port_comboBox.addItems(PORTS)

        self.send_data_button.clicked.connect(
            self.on_send_data_button_clicked)

        self.end_button.clicked.connect(self.on_end_button_clicked)

    def command1(self):
        """ Open the text input popup to save command for button 1 """
        self.command_edit(1)

    def command2(self):
        """ Open the text input popup to save command for button 2 """
        self.command_edit(2)

    def command3(self):
        """ Open the text input popup to save command for button 3 """
        self.command_edit(3)

    def command4(self):
        """ Open the text input popup to save command for button 4 """
        self.command_edit(4)

    def command_edit(self, button_number):
        """ Open the text input popup to save command """
        # Create a text input popup
        text, ok = QInputDialog.getText(
            self, 'Set your command', 'Please enter the command that you want to save:')
        if ok:
            if button_number == 1:
                self.saved_command_1.setText(str(text))
            elif button_number == 2:
                self.saved_command_2.setText(str(text))
            elif button_number == 3:
                self.saved_command_3.setText(str(text))
            elif button_number == 4:
                self.saved_command_4.setText(str(text))

    def move_command1_to_text(self):
        """ Move the saved command to the text box """
        self.textEdit_5.setText(self.saved_command_1.text())
        self.on_send_data_button_clicked()

    def move_command2_to_text(self):
        """ Move the saved command to the text box """
        self.textEdit_5.setText(self.saved_command_2.text())
        self.on_send_data_button_clicked()

    def move_command3_to_text(self):
        """ Move the saved command to the text box """
        self.textEdit_5.setText(self.saved_command_3.text())
        self.on_send_data_button_clicked()

    def move_command4_to_text(self):
        """ Move the saved command to the text box """
        self.textEdit_5.setText(self.saved_command_4.text())
        self.on_send_data_button_clicked()

    def refresh_port(self):
        """ Refresh the serial port list """
        PORTS = get_serial_port()
        self.port_comboBox.clear()
        self.port_comboBox.addItems(PORTS)

    def print_message_on_screen(self, text):
        """ Print the message on the screen """
        msg = QMessageBox()
        msg.setWindowTitle("Warning!")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(text)
        msg.exec()

    def establish_serial_communication(self):
        """ Establish serial communication """
        port = self.port_comboBox.currentText()
        baudrate = self.baudrate_comboBox.currentText()
        timeout = self.timeout_comboBox.currentText()
        length = self.len_comboBox.currentText()
        parity = self.parity_comboBox.currentText()
        stopbits = self.bit_comboBox.currentText()
        flowControl = self.flow_comboBox.currentText()

        if parity == "None":
            _parity = serial.PARITY_NONE
        elif parity == "Even":
            _parity = serial.PARITY_EVEN
        elif parity == "Odd":
            _parity = serial.PARITY_ODD
        elif parity == "Mark":
            _parity = serial.PARITY_MARK
        elif parity == "Space":
            _parity = serial.PARITY_SPACE
        else:
            self.print_message_on_screen("Parity Error!")

        if flowControl == "None":
            _xonxoff = False
            _rtscts = False
            _dsrdtr = False
        elif flowControl == "Xon/Xoff":
            _xonxoff = True
            _rtscts = False
            _dsrdtr = False
        elif flowControl == "RTS/CTS":
            _xonxoff = False
            _rtscts = True
            _dsrdtr = False
        elif flowControl == "DSR/DTR":
            _xonxoff = False
            _rtscts = False
            _dsrdtr = True
        else:
            self.print_message_on_screen("Flow Control Error!")
        
        global SERIAL_INFO
        SERIAL_INFO = serial.Serial(port=str(port),
                                    baudrate=int(baudrate, base=10),
                                    timeout=float(timeout),
                                    bytesize=int(length, base=10),
                                    parity=_parity,
                                    stopbits=float(stopbits),
                                    xonxoff = _xonxoff,
                                    rtscts = _rtscts,
                                    dsrdtr = _dsrdtr,
                                    )
        if SERIAL_INFO.isOpen() == False:
            SERIAL_INFO.open()

    def start_loop(self):
        """ Start the loop """
        self.port_comboBox.setStyleSheet('background-color: white')

        # If the serial port is not selected, print a message
        if self.port_comboBox.currentText() == "":
            self.print_message_on_screen("Please select a serial port first!")
            # Set port_comboBox background color to red
            self.port_comboBox.setStyleSheet('background-color: red')
            return

        try:
            self.establish_serial_communication()
        except SerialException:
            self.print_message_on_screen(
                "Exception occured while trying establish serial communication!")
            return

        is_serial_port_established = True
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
            # start the thread
            self.thread.start()
        except RuntimeError:
            self.print_message_on_screen("Exception in Worker Thread!")

    def stop_loop(self):
        """ Stop the loop """
        self.worker.working = False
        self.options_textEdit.setText('Stopped!')
    
    def clear_buffer(self):
        """ Clear the buffer """
        self.data_textEdit.clear()
        self.send_data_text.clear()

    def read_data_from_thread(self, serial_data):
        """ Write the result to the text edit box"""
        # self.data_textEdit.append("{}".format(i))
        if "ERROR_SERIAL_EXCEPTION" in serial_data:
            self.print_message_on_screen(
                "Serial Port Exception! Please check the serial port"
                " Possibly it is not connected or the port is not available!")
            self.status_label.setText("NOT CONNECTED!")
            self.status_label.setStyleSheet('color: red')
        else:
            self.timeout_comboBox.setEnabled(False)
            self.baudrate_comboBox.setEnabled(False)
            self.len_comboBox.setEnabled(False)
            self.port_comboBox.setEnabled(False)
            self.parity_comboBox.setEnabled(False)
            self.bit_comboBox.setEnabled(False)
            self.flow_comboBox.setEnabled(False)
            self.start_button.setEnabled(False)

            self.options_textEdit.setText('Data Gathering...')
            self.status_label.setText("CONNECTED!")
            self.status_label.setStyleSheet('color: green')
            serial_data = serial_data.replace('\n', '')
            self.data_textEdit.insertPlainText("{}".format(serial_data))

    def on_save_txt_button_clicked(self):
        """ Save the values to the TXT file"""
        with open('Output.txt', 'w', encoding='utf-8') as f:
            my_text = self.data_textEdit.toPlainText()
            f.write(my_text)
            f.close()

    def on_end_button_clicked(self):
        """ Stop the process """
        is_serial_port_established = False
        self.options_textEdit.setText('Stopped!')
        self.status_label.setText("DISCONNECTED!")
        self.status_label.setStyleSheet('color: red')
        self.timeout_comboBox.setEnabled(True)
        self.baudrate_comboBox.setEnabled(True)
        self.len_comboBox.setEnabled(True)
        self.port_comboBox.setEnabled(True)
        self.parity_comboBox.setEnabled(True)
        self.bit_comboBox.setEnabled(True)
        self.flow_comboBox.setEnabled(True)
        self.start_button.setEnabled(True)

    def on_send_data_button_clicked(self):
        """ Send data to serial port """
        if (is_serial_port_established):
            mytext = self.send_data_text.toPlainText()
            #print(mytext.encode())
            SERIAL_INFO.write(mytext.encode())
        else:
            self.print_message_on_screen(
                "Serial Port is not established yet! Please establish the serial port first!")

def start_ui_design():
    """ Start the UI Design """
    app = QApplication(argv)  # Create an instance
    window_object = MainWindow()  # Create an instance of our class

    if PROGRAM_TYPE_RELEASE:
        ui = Ui_main_window()
        ui.setupUi(window_object)

    app.exec()  # Start the application
