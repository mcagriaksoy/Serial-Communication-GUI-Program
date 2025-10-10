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
    from PySide6.QtWidgets import QWidget
except ImportError:
        print("PySide6 is not installed. Please install it to use this module.")

import json
from os import path
SETTINGS_FILE = path.join(path.dirname(__file__), 'settings.json')
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
    
    # Hide donate button in basic view
    if hasattr(ui, 'donateButton'):
        try:
            ui.donateButton.setVisible(False)
        except Exception:
            pass

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
    
    # Show donate button in advanced view
    if hasattr(ui, 'donateButton'):
        try:
            ui.donateButton.setVisible(True)
        except Exception:
            pass

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

def load_settings():
    """Load settings from settings.json if available."""
    try:
        if path.exists(SETTINGS_FILE):
            with open(SETTINGS_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception:
        pass
    # defaults
    return {'font_family': 'Segoe UI', 'font_size': 10}

def save_settings(settings):
    """Save settings dict to settings.json (best-effort)."""
    try:
        with open(SETTINGS_FILE, 'w', encoding='utf-8') as f:
            json.dump(settings, f, ensure_ascii=False, indent=2)
    except Exception:
        pass

def show_settings_dialog(ui=None):
    """ Show the settings dialog (debug/release). Persist chosen font settings on close.
        `ui` parameter is optional (kept for compatibility)."""
    widget_container = None
    settings_ui_obj = None
    try:
        if PROGRAM_TYPE_DEBUG:
            file_path = "ui/settings.ui"
            ui_file = QFile(file_path)
            if not ui_file.exists():
                QMessageBox.critical(None, "Error", f"Settings UI file not found: {file_path}")
                return
            ui_file.open(QFile.ReadOnly)
            loader = QUiLoader()
            settings_dialog = loader.load(ui_file)
            ui_file.close()
            if not settings_dialog:
                QMessageBox.critical(None, "Error", "Failed to load the settings UI.")
                return
            
            # Load existing settings and populate the UI
            settings = load_settings()
            font_w = settings_dialog.findChild(QWidget, 'fontComboBox')
            size_w = settings_dialog.findChild(QWidget, 'fontSize_spinBox')
            
            if font_w is not None and settings.get('font_family'):
                try:
                    from PySide6.QtGui import QFont as _QF
                    if hasattr(font_w, 'setCurrentFont'):
                        font_w.setCurrentFont(_QF(settings['font_family']))
                    else:
                        font_w.setCurrentText(settings['font_family'])
                except Exception:
                    pass
            
            if size_w is not None and settings.get('font_size'):
                try:
                    size_w.setValue(int(settings['font_size']))
                except Exception:
                    pass
            
            settings_dialog.setWindowTitle("Settings")
            settings_dialog.setModal(True)
            settings_dialog.exec()
            widget_container = settings_dialog
        else:
            dialog = QDialog()
            settings_ui = Ui_Dialog()
            settings_ui.setupUi(dialog)
            settings_ui_obj = settings_ui
            
            # Load existing settings and populate the UI
            settings = load_settings()
            if hasattr(settings_ui, 'fontComboBox') and settings.get('font_family'):
                try:
                    from PySide6.QtGui import QFont as _QF
                    if hasattr(settings_ui.fontComboBox, 'setCurrentFont'):
                        settings_ui.fontComboBox.setCurrentFont(_QF(settings['font_family']))
                    else:
                        settings_ui.fontComboBox.setCurrentText(settings['font_family'])
                except Exception:
                    pass
            
            if hasattr(settings_ui, 'fontSize_spinBox') and settings.get('font_size'):
                try:
                    settings_ui.fontSize_spinBox.setValue(int(settings['font_size']))
                except Exception:
                    pass
            
            dialog.setWindowTitle("Settings")
            dialog.exec()
            widget_container = dialog
    except Exception as e:
        print(f"Error showing settings dialog: {e}")
        return

    # After dialog closes, try to read font selection widgets and persist them.
    try:
        if widget_container is None:
            return
        # find font family widget (fontComboBox) and font size widget (fontSize_spinBox)
        font_w = None
        size_w = None
        
        try:
            font_w = widget_container.findChild(QWidget, 'fontComboBox')
            size_w = widget_container.findChild(QWidget, 'fontSize_spinBox')
        except Exception:
            # Release mode fallback
            if settings_ui_obj is not None:
                if hasattr(settings_ui_obj, 'fontComboBox'):
                    font_w = settings_ui_obj.fontComboBox
                if hasattr(settings_ui_obj, 'fontSize_spinBox'):
                    size_w = settings_ui_obj.fontSize_spinBox
        
        font_family = None
        font_size = None
        
        if font_w is not None:
            try:
                if hasattr(font_w, 'currentFont'):
                    font_family = font_w.currentFont().family()
                else:
                    font_family = font_w.currentText()
            except Exception:
                try:
                    font_family = font_w.currentText()
                except Exception:
                    font_family = None
        
        if size_w is not None:
            try:
                font_size = size_w.value()
            except Exception:
                font_size = None

        # load existing settings then update and save
        settings = load_settings()
        if font_family:
            settings['font_family'] = font_family
        if font_size:
            settings['font_size'] = font_size
        save_settings(settings)
    except Exception as e:
        print(f"Error saving settings: {e}")

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



