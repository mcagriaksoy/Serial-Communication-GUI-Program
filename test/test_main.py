import sys
import os
import pytest
from PyQt6.QtWidgets import QApplication
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from ui_main import MainWindow, get_serial_port

# Mock functions to avoid actual serial communication during testing
@pytest.fixture
def mock_serial_communication(mocker):
    mocker.patch('your_app_module.serial.Serial')
    return mocker.patch.object(MainWindow, 'establish_serial_communication')

def test_alp():
    alp = True
    assert alp

# def app_and_window():
#   """Fixture to create a QApplication and MainWindow instance"""
#   app = QApplication([])  # Create a temporary application instance
#   window = MainWindow()
#   yield app, window
#   app.quit()  # Close the application after tests

# def test_get_serial_ports_windows(mocker, app_and_window):
#   """Test get_serial_port function on Windows platform"""
#   mocker.patch('platform.system', return_value='Windows')
#   expected_ports = ['COM1', 'COM2']  # Example ports
#   ports = get_serial_port()
#   assert ports == expected_ports

# def test_get_serial_ports_linux(mocker, app_and_window):
#   """Test get_serial_port function on Linux platform"""
#   mocker.patch('platform.system', return_value='linux')
#   expected_ports = ['/dev/ttyUSB0', '/dev/ttyS0']  # Example ports
#   ports = get_serial_port()
#   assert ports == expected_ports

# def test_get_serial_ports_unsupported_platform(mocker, app_and_window):
#   """Test get_serial_port function on unsupported platform"""
#   mocker.patch('platform.system', return_value='unsupported_os')
#   with pytest.raises(EnvironmentError):
#     get_serial_port()

# def test_refresh_port(qtbot, app_and_window):
#   """Test refresh_port button functionality"""
#   app, window = app_and_window
#   # Mock get_serial_port to return a list of ports
#   window.ports = ["COM1", "COM2"]
#   qtbot.click(window.refresh_button)
#   assert window.port_comboBox.count() == 2  # Check if ports are added

# def test_start_loop_no_port_selected(qtbot, app_and_window, mock_serial_communication):
#   """Test start_loop button with no port selected"""
#   app, window = app_and_window
#   # Mock serial communication to avoid errors
#   mock_serial_communication.return_value = None
#   qtbot.click(window.start_button)
#   assert window.port_comboBox.styleSheet() == 'background-color: red'
#   # Check if error message is displayed (implementation specific)

# def test_start_loop_success(qtbot, app_and_window, mock_serial_communication):
#   """Test start_loop button with successful connection"""
#   app, window = app_and_window
#   # Mock get_serial_port to return a list of ports
#   mock_serial_communication.patch.object(serial.Serial, 'open').return_value = None
#   window.port_comboBox.setCurrentIndex(0)  # Select the first port
#   qtbot.click(window.start_button)
#   assert window.status_label.text() == "CONNECTED!"
#   assert window.status_label.styleSheet() == 'color: green'
#   # Simulate receiving data (implementation specific)

# def test_stop_loop(qtbot, app_and_window):
#   """Test stop_loop button functionality"""
#   app, window = app_and_window
#   # Simulate starting the loop (implementation specific)
#   qtbot.click(window.end_button)
#   assert window.options_textEdit.toPlainText() == ''
#   assert window.status_label.text() == "DISCONNECTED!"
#   assert window.status_label.styleSheet() == 'color: red'
