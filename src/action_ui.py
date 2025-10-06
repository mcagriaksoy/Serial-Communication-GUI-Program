# -*- coding: utf-8 -*-
"""
@file action_ui.py
@brief Action UI for the application.
@details This module provides the Action UI for the application, allowing users to interact with the system.
"""
# Runtime Type Checking
PROGRAM_TYPE_DEBUG = True
PROGRAM_TYPE_RELEASE = False
try:
    from PySide6.QtUiTools import QUiLoader
    from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
    from PySide6.QtCore import QFile
    from PySide6.QtGui import QDesktopServices
    from PySide6.QtCore import QUrl
    from ui.settings import Ui_Dialog
    from ui.help import Ui_HelpDialog
except ImportError:
        print("PySide6 is not installed. Please install it to use this module.")

import json
try:
    import requests
except ImportError:
    requests = None

CURRENT_VERSION = "v1.7.0"

def action_save_as(ui):
    """
    Save the current state of the application as a new file.
    """
    # Open the file dialog to select the save location and file name
    file_name, _ = QFileDialog.getSaveFileName(
        None, 'Save File', '', 'Text Files (*.txt)')
    if file_name:
        with open(file_name, 'w') as file:
            text = ui.data_textEdit.toPlainText()  # Access the textEdit element
            file.write(text)

def action_save(ui):
    """
    Save the current state of the application to the existing file.
    """
    # Check if a file is already open
    if hasattr(ui, 'current_file'):
        # Save the current state to the existing file
        with open(ui.current_file, 'w') as file:
            file.write(ui.data_textEdit.toPlainText())
    else:
        # If no file is open, call action_save_as to prompt for a file name
        action_save_as(ui)

def basic_view_enabled(ui):
    """ Hide specific layouts in the UI for basic view and collapse the
    reserved space so the window side doesn't leave an empty gap.

    This saves the layouts' margins/spacing and widgets' maximum heights the
    first time it's called, then sets margins and spacing to zero and forces
    widgets to zero height so the layout collapses. The values are restored
    by `advanced_view_enabled`.
    """
    # Short aliases
    v_layout = ui.verticalLayout_config
    f_layout = ui.formLayout_config

    # Save original layout settings and widget max heights once
    if not hasattr(ui, '_basic_view_saved'):
        ui._basic_view_saved = {
            'v_margins': v_layout.contentsMargins(),
            'v_spacing': v_layout.spacing(),
            'f_margins': f_layout.contentsMargins(),
            'f_spacing': f_layout.spacing(),
            'widgets_maxheight': {}
        }

    # Collapse layout spacing and margins to remove empty space
    try:
        v_layout.setContentsMargins(0, 0, 0, 0)
        v_layout.setSpacing(0)
    except Exception:
        pass
    try:
        f_layout.setContentsMargins(0, 0, 0, 0)
        f_layout.setSpacing(0)
    except Exception:
        pass

    # Hide and shrink widgets inside the layouts
    for i in range(v_layout.count()):
        item = v_layout.itemAt(i)
        widget = item.widget() if item else None
        if widget:
            # store previous maximum height to restore later
            ui._basic_view_saved['widgets_maxheight'][str(id(widget))] = widget.maximumHeight()
            widget.setMaximumHeight(0)
            widget.setVisible(False)

    for i in range(f_layout.count()):
        item = f_layout.itemAt(i)
        widget = item.widget() if item else None
        if widget:
            ui._basic_view_saved['widgets_maxheight'][str(id(widget))] = widget.maximumHeight()
            widget.setMaximumHeight(0)
            widget.setVisible(False)

def advanced_view_enabled(ui):
    """ Show specific layouts in the UI for advanced view and restore the
    layout margins/spacing and widgets' sizes saved by `basic_view_enabled`.
    """
    v_layout = ui.verticalLayout_config
    f_layout = ui.formLayout_config

    # Restore layout margins/spacing if we saved them earlier
    if hasattr(ui, '_basic_view_saved'):
        saved = ui._basic_view_saved
        try:
            m = saved.get('v_margins')
            if m is not None:
                v_layout.setContentsMargins(m.left(), m.top(), m.right(), m.bottom())
            v_layout.setSpacing(saved.get('v_spacing', v_layout.spacing()))
        except Exception:
            pass
        try:
            m = saved.get('f_margins')
            if m is not None:
                f_layout.setContentsMargins(m.left(), m.top(), m.right(), m.bottom())
            f_layout.setSpacing(saved.get('f_spacing', f_layout.spacing()))
        except Exception:
            pass

        # Restore widgets' maximum heights and visibility
        for i in range(v_layout.count()):
            item = v_layout.itemAt(i)
            widget = item.widget() if item else None
            if widget:
                key = str(id(widget))
                prev_h = saved['widgets_maxheight'].get(key)
                if prev_h is not None:
                    widget.setMaximumHeight(prev_h)
                else:
                    widget.setMaximumHeight(16777215)
                widget.setVisible(True)

        for i in range(f_layout.count()):
            item = f_layout.itemAt(i)
            widget = item.widget() if item else None
            if widget:
                key = str(id(widget))
                prev_h = saved['widgets_maxheight'].get(key)
                if prev_h is not None:
                    widget.setMaximumHeight(prev_h)
                else:
                    widget.setMaximumHeight(16777215)
                widget.setVisible(True)
        # clear saved state
        delattr(ui, '_basic_view_saved') if hasattr(ui, '_basic_view_saved') else None
    else:
        # Fallback: simply show widgets
        for i in range(v_layout.count()):
            item = v_layout.itemAt(i)
            widget = item.widget() if item else None
            if widget:
                widget.setVisible(True)
                widget.setMaximumHeight(16777215)

        for i in range(f_layout.count()):
            item = f_layout.itemAt(i)
            widget = item.widget() if item else None
            if widget:
                widget.setVisible(True)
                widget.setMaximumHeight(16777215)

def clear_buffer(ui):
    """ Clear the buffer """
    ui.data_textEdit.clear()
    ui.send_data_text.clear()

def show_about_dialog(ui):
    """ Show the about dialog """
    # Create a message box to display the about information
    msg_box = QMessageBox()
    msg_box.setWindowTitle("About")
    # Use CURRENT_VERSION for the version number
    msg_box.setText(f"AFCOM Client {CURRENT_VERSION} (C) 2020 - 2025 \r\n\r\nAuthor: Mehmet Cagri Aksoy \r\ngithub.com/mcagriaksoy")
    msg_box.setIcon(QMessageBox.Information)
    msg_box.setStandardButtons(QMessageBox.Ok)
    msg_box.setDefaultButton(QMessageBox.Ok)
    msg_box.setModal(True)
    msg_box.exec()  # Show the message box modally

def show_help_dialog(ui):
    """ Show the help dialog """
    if PROGRAM_TYPE_DEBUG:
        file_path = "ui/help.ui"  # Adjust the path if necessary
        ui_file = QFile(file_path)
        if not ui_file.exists():
            QMessageBox.critical(None, "Error", f"Help UI file not found: {file_path}")
            return
        
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        help_dialog = loader.load(ui_file)
        ui_file.close()
        if help_dialog:
            help_dialog.setWindowTitle("Help")
            help_dialog.setModal(True)
            help_dialog.exec()
        else:
            QMessageBox.critical(None, "Error", "Failed to load the help UI.")
    else:
        try:
            dialog = QDialog()  # Create a QDialog instance
            help_dialog = Ui_HelpDialog()  # Initialize the UI class
            help_dialog.setupUi(dialog)  # Set up the UI on the dialog
            dialog.setWindowTitle("Help")  # Set the dialog title
            dialog.exec()  # Show the dialog modally
        except Exception as e:
            print(f"Error in show_help_dialog: {e}")

def show_settings_dialog(ui):
    """ Show the settings dialog """
    if PROGRAM_TYPE_DEBUG:
        file_path = "ui/settings.ui"  # Adjust the path if necessary
        ui_file = QFile(file_path)
        if not ui_file.exists():
            QMessageBox.critical(None, "Error", f"Settings UI file not found: {file_path}")
            return
        
        ui_file.open(QFile.ReadOnly)
        loader = QUiLoader()
        settings_dialog = loader.load(ui_file)
        ui_file.close()
        if settings_dialog:
            settings_dialog.setWindowTitle("Settings")
            settings_dialog.setModal(True)
            settings_dialog.exec()
        else:
            QMessageBox.critical(None, "Error", "Failed to load the settings UI.")
    else:
        try:
            dialog = QDialog()  # Create a QDialog instance
            settings_dialog = Ui_Dialog()  # Initialize the UI class
            settings_dialog.setupUi(dialog)  # Set up the UI on the dialog
            dialog.setWindowTitle("Settings")  # Set the dialog title
            dialog.exec()  # Show the dialog modally
        except Exception as e:
            print(f"Error in show_settings_dialog: {e}")

def check_for_updates(ui):
    """Check for updates by comparing the latest GitHub tag with the current version."""
    if requests is None:
        QMessageBox.warning(None, "Check for Updates", "The 'requests' library is not installed. Please install it to check for updates.")
        return
    try:
        url = "https://api.github.com/repos/mcagriaksoy/Serial-Communication-GUI-Program/tags"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            tags = response.json()
            if tags:
                latest_tag = tags[0]["name"]
                if latest_tag != CURRENT_VERSION:
                    msg_box = QMessageBox()
                    msg_box.setWindowTitle("Update Available")
                    msg_box.setText(f"A new version is available: {latest_tag}\nYou are using: {CURRENT_VERSION}\nWould you like to download the latest version?")
                    download_button = msg_box.addButton("Download", QMessageBox.AcceptRole)
                    msg_box.addButton(QMessageBox.Ok)
                    msg_box.setIcon(QMessageBox.Information)
                    msg_box.setModal(True)
                    msg_box.exec()
                    if msg_box.clickedButton() == download_button:
                        QDesktopServices.openUrl(QUrl(f"https://github.com/mcagriaksoy/Serial-Communication-GUI-Program/releases/tag/{latest_tag}"))
                else:
                    QMessageBox.information(None, "Check for Updates", "You are using the latest version.")
            else:
                QMessageBox.information(None, "Check for Updates", "No version tags found on GitHub.")
        else:
            QMessageBox.warning(None, "Check for Updates", f"Failed to fetch updates. Status code: {response.status_code}")
    except Exception as e:
        QMessageBox.critical(None, "Check for Updates", f"Error checking for updates: {e}")



