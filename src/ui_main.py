# -*- coding: utf-8 -*-
"""
AFCOM - Serial Communication GUI Program
Cannot be used directly, it is a part of main.py
"""

__author__ = 'Mehmet Cagri Aksoy - github.com/mcagriaksoy'
__annotations__ = 'AFCOM - Serial Communication GUI Program'
__version__ = '1.7.0'
__license__ = 'JGPLv3'
__status__ = 'Development'

# IMPORTS
from os import path, system
from sys import platform, exit, argv
from glob import glob
from src import action_ui
import re
# Runtime Type Checking
PROGRAM_TYPE_DEBUG = True
PROGRAM_TYPE_RELEASE = False

try:
    import serial.tools.list_ports
    from serial import SerialException, Serial
except ImportError as e:
    print("Import Error! I am installing the PySerial library.")
    #system("python -m pip install pyserial")

try:
    from PySide6.QtCore import QObject, QThread, Signal, QFile, Qt, QEvent, QTimer
    from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QInputDialog
    from ui.main_window import Ui_main_window
    if (PROGRAM_TYPE_DEBUG):
        from PySide6.QtUiTools import QUiLoader

except ImportError as e:
    print("Import Error! I am installing the required libraries: " + str(e))
    #system("pip install {0}".format(str(e).split(" ")[-1]))

# GLOBAL VARIABLES
SERIAL_DEVICE = Serial()
PORTS = []
is_serial_port_established = False

from winreg import OpenKey, HKEY_CURRENT_USER, QueryValueEx, ConnectRegistry, KEY_READ, KEY_WOW64_64KEY

def is_windows_dark_mode(self):
    try:
        registry = ConnectRegistry(None, HKEY_CURRENT_USER)
        registry_key = OpenKey(registry, r'Software\Microsoft\Windows\CurrentVersion\Themes\Personalize')
        value, _ = QueryValueEx(registry_key, 'AppsUseLightTheme')
        return value == 0  # 0 means dark mode is enabled
    except WindowsError:
        return False

# simpleViewEnabled = False


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
        except (OSError, SerialException):
            pass
    return result

def strip_ansi_codes(text):
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

def ansi_to_html(text):
    # Improved ANSI to HTML conversion with support for bold and combined codes
    ansi_color_map = {
        '30': 'black', '31': 'red', '32': 'green', '33': 'yellow',
        '34': 'blue', '35': 'magenta', '36': 'cyan', '37': 'white',
        '90': 'gray', '91': 'lightcoral', '92': 'lightgreen', '93': 'lightyellow',
        '94': 'lightblue', '95': 'violet', '96': 'lightcyan', '97': 'white'
    }
    def ansi_repl(match):
        codes = match.group(1).split(';')
        styles = []
        for code in codes:
            if code == '1':
                styles.append('font-weight:bold;')
            elif code in ansi_color_map:
                styles.append(f'color:{ansi_color_map[code]};')
        if styles:
            return f'<span style="{''.join(styles)}">'
        elif '0' in codes:
            return '</span>'
        return ''
    # Open/close spans for each ANSI code
    text = re.sub(r'\x1b\[([0-9;]+)m', ansi_repl, text)
    # Remove any remaining ANSI codes
    text = re.sub(r'\x1b\[[0-9;]*[A-Za-z]', '', text)
    return text

# MULTI-THREADING
class Worker(QObject):
    """ Worker Thread """
    finished = Signal()
    serial_data = Signal(str)

    def __init__(self):
        super(Worker, self).__init__()
        self.working = True

    def work(self):
        """ Read data from serial port, emit full lines """
        buffer = ''
        while self.working:
            try:
                char = SERIAL_DEVICE.read().decode('utf-8', errors='replace')
                buffer += char
                if '\n' in buffer:
                    lines = buffer.split('\n')
                    for line in lines[:-1]:
                        self.serial_data.emit(line + '\n')
                    buffer = lines[-1]
            except SerialException as e:
                print(e)
                self.serial_data.emit("ERROR_SERIAL_EXCEPTION")
                self.working = False
        self.finished.emit()

class MainWindow(QMainWindow):
    """ Main Window """

    def __init__(self):
        """ Initialize Main Window """
        super(MainWindow, self).__init__()

        if PROGRAM_TYPE_DEBUG:
            
            file_path = path.join("ui/main_window.ui")
            if not path.exists(file_path):
                print("UI File Not Found!")
                exit(1)
            ui_file = QFile(file_path)
            ui_file.open(QFile.ReadOnly)
            loader = QUiLoader()
            self.ui = loader.load(ui_file)
            self.ui.show()
            # Try to make the menu bar more compact (smaller height and padding).
            # Some platforms/skins make the menubar very tall; force a tighter style.
            try:
                m = getattr(self.ui, 'menuBar', None)
                if callable(m):
                    mb = m()
                else:
                    mb = m
                if mb is not None:
                    # Avoid forcing a fixed height (which can trigger the overflow '>>').
                    # Reduce font size and item padding so the menu is visually smaller
                    # but items remain visible.
                    mb.setStyleSheet(
                        "QMenuBar { font-size: 8pt; }")
                    mb.setStyleSheet(mb.styleSheet() +
                                    "QMenuBar::item { padding: 2px 8px; margin: 0px; }")
                    mb.updateGeometry()
            except Exception:
                pass
        else:  # PROGRAM_TYPE_RELEASE
            print("UI File Found!")
            self.ui = Ui_main_window()
            self.ui.setupUi(self)
            # Apply the same compact menubar style in release mode (setupUi created the menubar
            # on the QMainWindow instance `self`). Use safe checks so this doesn't fail.
            try:
                m = getattr(self, 'menuBar', None)
                if callable(m):
                    mb = m()
                else:
                    mb = m
                if mb is not None:
                    # Avoid fixed height to prevent the menu overflow chevron (>>).
                    mb.setStyleSheet(
                        "QMenuBar { font-size: 9pt; }")
                    mb.setStyleSheet(mb.styleSheet() +
                                    "QMenuBar::item { padding: 2px 8px; margin: 0px; }")
                    mb.updateGeometry()
            except Exception:
                pass
        
        if (is_windows_dark_mode(self)):
            print("Windows Dark Mode is enabled!")
            # todo add dark mode support for the UI

        PORTS = get_serial_port()

        self.thread = None
        self.worker = None

        self.ui.start_button.clicked.connect(self.on_start_button_clicked)
        self.ui.refresh_button.clicked.connect(self.refresh_port)
        '''
        self.ui.command_edit_1.clicked.connect(self.command1)
        self.ui.command_edit_2.clicked.connect(self.command2)
        self.ui.command_edit_3.clicked.connect(self.command3)
        self.ui.command_edit_4.clicked.connect(self.command4)

        self.ui.saved_command_1.clicked.connect(self.move_command1_to_text)
        self.ui.saved_command_2.clicked.connect(self.move_command2_to_text)
        self.ui.saved_command_3.clicked.connect(self.move_command3_to_text)
        self.ui.saved_command_4.clicked.connect(self.move_command4_to_text)
        '''

        self.ui.actionCopy.triggered.connect(lambda: self.ui.data_textEdit.copy())
        self.ui.actionSelect_All.triggered.connect(lambda: self.ui.data_textEdit.selectAll())
        self.ui.actionClear_Screen.triggered.connect(lambda: self.ui.data_textEdit.clear())

        self.ui.actionClear_Cache.triggered.connect(action_ui.clear_buffer)

        self.ui.actionBasic_View.triggered.connect(lambda: action_ui.basic_view_enabled(self.ui))
        self.ui.actionAdvanced_View.triggered.connect(lambda: action_ui.advanced_view_enabled(self.ui))

        self.ui.actionSave.triggered.connect(action_ui.action_save)
        self.ui.actionSave_As.triggered.connect(action_ui.action_save_as)

        self.ui.port_comboBox.addItems(PORTS)
        self.ui.send_button.clicked.connect(self.on_send_data_button_clicked)

        # when Enter is pressed in send_data_text
        self.ui.send_data_text.installEventFilter(self)

        self.ui.actionExit.triggered.connect(lambda: exit(0))
        self.ui.actionAbout.triggered.connect(action_ui.show_about_dialog)
        self.ui.actionCheck_for_updates.triggered.connect(action_ui.check_for_updates)
        self.ui.actionHelp_2.triggered.connect(action_ui.show_help_dialog)
        self.ui.actionPreferences.triggered.connect(action_ui.show_settings_dialog)

        # Dark mode button event
        self.night_mode_enabled = False
        if hasattr(self.ui, 'nightMode_Button'):
            self.ui.nightMode_Button.clicked.connect(self.enable_night_mode)

    '''
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
                self.ui.saved_command_1.setText(str(text))
            elif button_number == 2:
                self.ui.saved_command_2.setText(str(text))
            elif button_number == 3:
                self.ui.saved_command_3.setText(str(text))
            elif button_number == 4:
                self.ui.saved_command_4.setText(str(text))

    def move_command1_to_text(self):
        """ Move the saved command to the text box """
        self.ui.send_data_text.setText(self.ui.saved_command_1.text())
        self.on_send_data_button_clicked()

    def move_command2_to_text(self):
        """ Move the saved command to the text box """
        self.ui.send_data_text.setText(self.ui.saved_command_2.text())
        self.on_send_data_button_clicked()

    def move_command3_to_text(self):
        """ Move the saved command to the text box """
        self.ui.send_data_text.setText(self.ui.saved_command_3.text())
        self.on_send_data_button_clicked()

    def move_command4_to_text(self):
        """ Move the saved command to the text box """
        self.ui.send_data_text.setText(self.ui.saved_command_4.text())
        self.on_send_data_button_clicked()
    '''
    def eventFilter(self, obj, event):
        # Check if the event is for send_data_text and Enter is pressed
        if obj == self.ui.send_data_text and event.type() == QEvent.KeyPress:
            if event.key() in (Qt.Key_Return, Qt.Key_Enter):
                self.on_send_data_button_clicked()
                return True  # Prevents QTextEdit from adding a new line
        return super().eventFilter(obj, event)

    def refresh_port(self):
        """ Refresh the serial port list """
        PORTS = get_serial_port()
        self.ui.port_comboBox.clear()
        self.ui.port_comboBox.addItems(PORTS)

    def print_message_on_screen(self, text):
        """ Print the message on the screen """
        msg = QMessageBox()
        msg.setWindowTitle("Warning!")
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(text)
        msg.exec()

    def establish_serial_communication(self):
        """ Establish serial communication """
        port = self.ui.port_comboBox.currentText()
        baudrate = self.ui.baudrate_comboBox.currentText()
        timeout = self.ui.timeout_comboBox.currentText()
        length = self.ui.len_comboBox.currentText()
        parity = self.ui.parity_comboBox.currentText()
        stopbits = self.ui.bit_comboBox.currentText()
        flowControl = self.ui.flow_comboBox.currentText()

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
        
        global SERIAL_DEVICE
        SERIAL_DEVICE = serial.Serial(port=str(port),
                                    baudrate=int(baudrate, base=10),
                                    timeout=float(timeout),
                                    bytesize=int(length, base=10),
                                    parity=_parity,
                                    stopbits=float(stopbits),
                                    xonxoff = _xonxoff,
                                    rtscts = _rtscts,
                                    dsrdtr = _dsrdtr,
                                    )
        if SERIAL_DEVICE.isOpen() == False:
            SERIAL_DEVICE.open()

    def on_start_button_clicked(self):
        """ Start the loop """
        # Check if the port_comboBox style is red, if so, set it to system default
        if self.ui.port_comboBox.styleSheet() == 'background-color: red':
            self.ui.port_comboBox.setStyleSheet('')

        global is_serial_port_established

        if is_serial_port_established:
            is_serial_port_established = False
            self.ui.start_button.setText("START")
            self.ui.start_button.setStyleSheet('color: green;')
            self.on_stop_button_clicked()
            return

        # If the serial port is not selected, print a message
        if self.ui.port_comboBox.currentText() == "":
            self.print_message_on_screen("Please select a serial port first!")
            # Set port_comboBox background color to red
            self.ui.port_comboBox.setStyleSheet('background-color: red')
            return

        try:
            self.establish_serial_communication()
        except SerialException:
            self.print_message_on_screen(
                "Exception occured while trying establish serial communication!")
            return
        is_serial_port_established = True
        # change start_button to stop button
        # Get more info about the selected port
        port_info = None
        selected_port = self.ui.port_comboBox.currentText()
        for p in serial.tools.list_ports.comports():
            if p.device == selected_port:
                port_info = p
                break
        if port_info:
            info_text = f"RX/TX Connected to: {port_info.device}\nDescription: {port_info.description}\nManufacturer: {getattr(port_info, 'manufacturer', 'N/A')}\nHWID: {port_info.hwid}"
        else:
            info_text = f"RX/TX Connected to: {selected_port}"
        self.ui.options_textEdit.setText(info_text)
        self.ui.start_button.setText("STOP")
        self.ui.start_button.setStyleSheet('color: red;')

        try:
            self.worker = Worker()   # a new worker to perform those tasks
            self.thread = QThread()   # a new thread to run our background tasks in
            # move the worker into the thread, do this first before connecting the signals
            self.worker.moveToThread(self.thread)
            # begin our worker object's loop when the thread starts running
            self.thread.started.connect(self.worker.work)
            self.worker.serial_data.connect(self.read_data_from_thread)
            # tell the thread it's time to stop running
            self.worker.finished.connect(self.thread.quit)
            # have worker mark itself for deletion
            self.worker.finished.connect(self.worker.deleteLater)
            # have thread mark itself for deletion
            self.thread.finished.connect(self.thread.deleteLater)
            
            self.enable_configuration(False)
            self.ui.options_textEdit.setText('RX/TX Connected to the: ' + str(SERIAL_DEVICE.portstr))
            self.ui.status_label.setText("CONNECTED!")
            self.ui.status_label.setStyleSheet('color: green')
            # start the thread
            self.thread.start()
        except RuntimeError:
            self.print_message_on_screen("Exception in Worker Thread!")

    def on_stop_button_clicked(self):
        """ Stop the loop """
        self.ui.options_textEdit.setText('Stopped!')
        self.ui.status_label.setText("DISCONNECTED!")
        self.ui.status_label.setStyleSheet('color: red')
        self.enable_configuration(True)
        self.stop_worker_thread()
        # Safely close the serial device
        global SERIAL_DEVICE
        try:
            if SERIAL_DEVICE.is_open:
                SERIAL_DEVICE.close()
        except Exception as e:
            print(f"Error closing serial port: {e}")
    
    def stop_worker_thread(self):
        # Safely stop the worker thread and wait for it to finish
        if hasattr(self, 'worker') and self.worker is not None:
            self.worker.working = False
        if hasattr(self, 'thread') and self.thread is not None:
            if self.thread.isRunning():
                self.thread.quit()
                self.thread.wait(2000)  # wait up to 2 seconds

    def enable_configuration(self, state):
        """ enable/disable the configuration """
        self.ui.timeout_comboBox.setEnabled(state)
        self.ui.baudrate_comboBox.setEnabled(state)
        self.ui.len_comboBox.setEnabled(state)
        self.ui.port_comboBox.setEnabled(state)
        self.ui.parity_comboBox.setEnabled(state)
        self.ui.bit_comboBox.setEnabled(state)
        self.ui.flow_comboBox.setEnabled(state)
        self.ui.lineEnd_comboBox.setEnabled(state)

    def read_data_from_thread(self, serial_data):
        """ Write the result to the text edit box"""
        if "ERROR_SERIAL_EXCEPTION" in serial_data:
            self.print_message_on_screen(
                "Serial Port Exception! Please check the serial port"
                " Possibly it is not connected or the port is not available!")
            self.on_stop_button_clicked()
        else:
            html_data = ansi_to_html(serial_data.replace('\r\n', '<br>').replace('\n', '<br>'))
            # Adjust text color for day/Dark mode
            if hasattr(self, 'night_mode_enabled') and self.night_mode_enabled:
                # Night mode: convert black text to white
                html_data = html_data.replace('color:black;', 'color:white;')
            else:
                # Day mode: convert white text to black
                html_data = html_data.replace('color:white;', 'color:black;')
            self.ui.data_textEdit.insertHtml(html_data)
            self.ui.data_textEdit.verticalScrollBar().setValue(
                self.ui.data_textEdit.verticalScrollBar().maximum())

    def on_send_data_button_clicked(self):
        """ Send data to serial port """
        if is_serial_port_established:
            self.ui.indicate_button.setChecked(True)
            # Clear end of line, spaces, and tabs from end of the text
            mytext = self.ui.send_data_text.toPlainText().strip().encode('utf-8')
            # Get line ending from combo box
            line_end = self.ui.lineEnd_comboBox.currentText()
            if line_end == "CR":
                line_ending = b'\r'
            elif line_end == "LF":
                line_ending = b'\n'
            elif line_end == "CRLF":
                line_ending = b'\r\n'
            else:
                line_ending = b''
            SERIAL_DEVICE.flushOutput()  # Flush output buffer
            SERIAL_DEVICE.write(mytext + line_ending)

            # Uncheck after 5 seconds without blocking the UI
            QTimer.singleShot(500, lambda: self.ui.indicate_button.setChecked(False))
        else:
            self.print_message_on_screen(
                "Serial Port is not established yet! Please establish the serial port first!")

    def enable_night_mode(self):
        """Toggle night/day mode for data_textEdit"""
        if not hasattr(self, 'night_mode_enabled'):
            self.night_mode_enabled = False
        if not self.night_mode_enabled:
            self.ui.data_textEdit.setStyleSheet("background-color: black;")
            if hasattr(self.ui.nightMode_Button, 'setText'):
                self.ui.nightMode_Button.setText("Day Mode")
            self.night_mode_enabled = True
        else:
            self.ui.data_textEdit.setStyleSheet("")
            if hasattr(self.ui.nightMode_Button, 'setText'):
                self.ui.nightMode_Button.setText("Dark Mode")
            self.night_mode_enabled = False

    def closeEvent(self, event):
        # Properly stop the worker and thread before closing
        self.stop_worker_thread()
        if hasattr(self, 'thread') and self.thread is not None:
            if self.thread.isRunning():
                self.thread.quit()
                self.thread.wait(2000)  # Wait up to 2 seconds for thread to finish
        event.accept()

def start_ui_design():
    """ Start the UI Design """
    app = QApplication(argv)  # Create an instance
    window_object = MainWindow()  # Create an instance of our class
    if PROGRAM_TYPE_RELEASE:
        window_object.show()
    exit(app.exec())