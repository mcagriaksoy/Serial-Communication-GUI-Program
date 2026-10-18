# -*- coding: utf-8 -*-
"""Menu and toolbar actions for the main window.

Each function receives the :class:`~src.main_window.MainWindow` instance, which
gives it access to the generated UI, the settings store and the serial worker.
Keeping the logic here keeps the window controller focused on wiring.
"""

from __future__ import annotations

import json
import urllib.request

from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox

from .constants import (
    APP_AUTHOR,
    APP_NAME,
    APP_RELEASES_URL,
    APP_TAGS_API,
    APP_URL,
    APP_VERSION,
)
from .ui_loader import load_ui_class


# ---------------------------------------------------------------------------
# Save / open
# ---------------------------------------------------------------------------
def save_terminal_as(window) -> None:
    """Prompt for a destination and write the terminal contents to it."""
    file_name, _ = QFileDialog.getSaveFileName(
        window, "Save terminal output", "", "Text files (*.txt);;All files (*)"
    )
    if not file_name:
        return
    try:
        with open(file_name, "w", encoding="utf-8") as handle:
            handle.write(window.ui.data_textEdit.toPlainText())
    except OSError as exc:
        QMessageBox.warning(window, "Save failed", f"Could not save the file:\n{exc}")
        return
    window.current_file = file_name


def save_terminal(window) -> None:
    """Save to the current file, or fall back to *Save As*."""
    current = getattr(window, "current_file", None)
    if not current:
        save_terminal_as(window)
        return
    try:
        with open(current, "w", encoding="utf-8") as handle:
            handle.write(window.ui.data_textEdit.toPlainText())
    except OSError as exc:
        QMessageBox.warning(window, "Save failed", f"Could not save the file:\n{exc}")


def new_terminal(window) -> None:
    """Start a fresh session: clear the terminal and forget the current file."""
    window.ui.data_textEdit.clear()
    window.current_file = None
    window.reset_counters()


# ---------------------------------------------------------------------------
# View
# ---------------------------------------------------------------------------
def set_advanced_view(window, enabled: bool) -> None:
    """Toggle the configuration side panel and the donate button."""
    window.ui.configPanel.setVisible(enabled)
    donate = getattr(window.ui, "donateButton", None)
    if donate is not None:
        donate.setVisible(enabled)


# ---------------------------------------------------------------------------
# Dialogs
# ---------------------------------------------------------------------------
def show_about(window) -> None:
    text = (
        f"<h3>{APP_NAME}</h3>"
        f"<p>Version {APP_VERSION}</p>"
        f"<p>A free, cross-platform serial (COM) port client for sending and "
        f"receiving data.</p>"
        f"<p>Author: {APP_AUTHOR}<br>"
        f'<a href="{APP_URL}">{APP_URL}</a></p>'
        f"<p>Released under the GNU General Public License v3.</p>"
    )
    box = QMessageBox(window)
    box.setWindowTitle("About")
    box.setIcon(QMessageBox.Icon.Information)
    box.setTextFormat(Qt.TextFormat.RichText)
    box.setText(text)
    open_link = box.addButton("Open project page", QMessageBox.ButtonRole.ActionRole)
    box.addButton(QMessageBox.StandardButton.Close)
    box.exec()
    if box.clickedButton() is open_link:
        QDesktopServices.openUrl(QUrl(APP_URL))


_HELP_HTML = f"""
<h2>{APP_NAME} — Help</h2>
<p>AFCOM is a serial (COM port) communication client. Use it to talk to
microcontrollers, sensors, modems and any other device that exposes a serial
interface.</p>
<h3>Getting started</h3>
<ol>
  <li>Connect your device and press <b>Scan ports</b> to refresh the list.</li>
  <li>Select the <b>Port</b> and configure baud rate, data bits, parity, stop
      bits and flow control to match your device.</li>
  <li>Press <b>CONNECT</b>. Received data appears in the terminal.</li>
  <li>Type into the send box and press <b>Enter</b> (or click <b>Send</b>).</li>
</ol>
<h3>Tips</h3>
<ul>
  <li><b>Save / Save As</b> write the terminal contents to a text file.</li>
  <li><b>Clear Buffers</b> empties the terminal and the send box.</li>
  <li><b>Basic View</b> hides the configuration panel for a distraction-free
      terminal.</li>
  <li>Preferences let you switch theme, language and terminal font.</li>
</ul>
<h3>Legal</h3>
<p>This application uses Qt for Python (PySide6), licensed under LGPLv3.
AFCOM itself is released under the GNU General Public License v3.</p>
"""


def show_help(window) -> None:
    dialog = QDialog(window)
    ui_class = load_ui_class("help", "Ui_HelpDialog")
    ui = ui_class()
    ui.setupUi(dialog)
    ui.helpTitleLabel.setText(APP_NAME)
    ui.helpTextEdit.setHtml(_HELP_HTML)
    dialog.exec()


# ---------------------------------------------------------------------------
# Updates
# ---------------------------------------------------------------------------
def check_for_updates(window) -> None:
    """Compare the newest GitHub tag with the running version."""
    try:
        request = urllib.request.Request(APP_TAGS_API, headers={"User-Agent": APP_NAME})
        with urllib.request.urlopen(request, timeout=6) as response:
            tags = json.load(response)
    except Exception as exc:  # network, JSON, etc.
        QMessageBox.warning(
            window, "Check for Updates", f"Could not check for updates:\n{exc}"
        )
        return

    if not isinstance(tags, list) or not tags:
        QMessageBox.information(window, "Check for Updates", "No releases were found.")
        return

    latest = str(tags[0].get("name", "")).lstrip("v")
    if latest == APP_VERSION:
        QMessageBox.information(
            window, "Check for Updates", f"You are running the latest version ({APP_VERSION})."
        )
        return

    box = QMessageBox(window)
    box.setWindowTitle("Update available")
    box.setIcon(QMessageBox.Icon.Information)
    box.setText(
        f"A newer version is available: <b>{latest}</b><br>"
        f"You are running <b>{APP_VERSION}</b>."
    )
    download = box.addButton("Open download page", QMessageBox.ButtonRole.AcceptRole)
    box.addButton(QMessageBox.StandardButton.Close)
    box.exec()
    if box.clickedButton() is download:
        QDesktopServices.openUrl(QUrl(APP_RELEASES_URL))
