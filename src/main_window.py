# -*- coding: utf-8 -*-
"""The main window controller.

This module wires the generated ``main_window`` UI to the serial worker,
settings store and menu actions.  It contains no UI layout code (that lives in
``ui/main_window.ui``) and no algorithm code (that lives in the helper
modules).
"""

from __future__ import annotations

import webbrowser

from PySide6.QtCore import QEvent, Qt, QThread, QTimer
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox

from . import actions
from .ansi import ansi_to_html
from .constants import (
    APP_DONATE_URL,
    BAUDRATE_LIST,
    DATA_BITS_LIST,
    DEFAULT_FONT_FAMILY,
    DEFAULT_FONT_SIZE,
    DEFAULT_THEME,
    FLOW_CONTROL_LIST,
    LINE_ENDING_LIST,
    PARITY_LIST,
    STOP_BITS_LIST,
    TIMEOUT_LIST,
)
from .serial_ports import available_ports, display_name, port_details_by_device
from .serial_worker import SerialReader
from .settings_dialog import PreferencesDialog
from .settings_store import SettingsStore
from .theme import detect_ui_font, load_stylesheet
from .translations import Translator
from .ui_loader import load_ui_class

try:  # pragma: no cover - import guard
    from serial import PARITY_EVEN, PARITY_MARK, PARITY_NONE, PARITY_ODD, PARITY_SPACE, Serial
    from serial import SerialException
except ImportError:  # pragma: no cover
    Serial = None  # type: ignore[assignment]
    SerialException = Exception  # type: ignore[assignment]
    PARITY_NONE = PARITY_EVEN = PARITY_ODD = PARITY_MARK = PARITY_SPACE = "N"

_PARITY_MAP = {
    "None": PARITY_NONE,
    "Even": PARITY_EVEN,
    "Odd": PARITY_ODD,
    "Mark": PARITY_MARK,
    "Space": PARITY_SPACE,
}

_FLOW_MAP = {
    "None": {"xonxoff": False, "rtscts": False, "dsrdtr": False},
    "Xon/Xoff": {"xonxoff": True, "rtscts": False, "dsrdtr": False},
    "RTS/CTS": {"xonxoff": False, "rtscts": True, "dsrdtr": False},
    "DSR/DTR": {"xonxoff": False, "rtscts": False, "dsrdtr": True},
}

_LINE_ENDINGS = {"None": b"", "LF": b"\n", "CR": b"\r", "CRLF": b"\r\n"}

_NO_PORT_TEXT = "— no ports found —"


class MainWindow(QMainWindow):
    """Application main window."""

    def __init__(self, settings: SettingsStore) -> None:
        super().__init__()
        self.settings = settings
        self.translator = Translator(settings.get("language", "en"))
        self.current_file: str | None = None

        ui_class = load_ui_class("main_window", "Ui_main_window")
        self.ui = ui_class()
        self.ui.setupUi(self)

        self._serial = None
        self._worker: SerialReader | None = None
        self._thread: QThread | None = None
        self._connected = False
        self._rx_bytes = 0
        self._tx_bytes = 0

        self._populate_combos()
        self._wire_signals()
        self.apply_appearance()
        self.apply_language()
        self.refresh_ports()
        self._set_status("idle")

    # ------------------------------------------------------------------
    # Setup helpers
    # ------------------------------------------------------------------
    def _populate_combos(self) -> None:
        ui = self.ui
        ui.baudrate_comboBox.addItems(BAUDRATE_LIST)
        ui.len_comboBox.addItems(DATA_BITS_LIST)
        ui.parity_comboBox.addItems(PARITY_LIST)
        ui.bit_comboBox.addItems(STOP_BITS_LIST)
        ui.timeout_comboBox.addItems(TIMEOUT_LIST)
        ui.flow_comboBox.addItems(FLOW_CONTROL_LIST)
        ui.lineEnd_comboBox.addItems(LINE_ENDING_LIST)

        self._select(ui.baudrate_comboBox, "115200")
        self._select(ui.len_comboBox, "8")
        self._select(ui.parity_comboBox, "None")
        self._select(ui.bit_comboBox, "1")
        self._select(ui.timeout_comboBox, "1")
        self._select(ui.flow_comboBox, "None")
        self._select(ui.lineEnd_comboBox, "LF")

    @staticmethod
    def _select(combo, text: str) -> None:
        index = combo.findText(text)
        if index >= 0:
            combo.setCurrentIndex(index)

    def _wire_signals(self) -> None:
        ui = self.ui
        ui.start_button.clicked.connect(self._on_connect_clicked)
        ui.refresh_button.clicked.connect(self.refresh_ports)
        ui.send_button.clicked.connect(self._send_data)
        ui.clearButton.clicked.connect(self._clear_terminal)
        ui.donateButton.clicked.connect(lambda: webbrowser.open(APP_DONATE_URL))
        ui.send_data_text.installEventFilter(self)

        ui.actionNew.triggered.connect(lambda: actions.new_terminal(self))
        ui.actionSave.triggered.connect(lambda: actions.save_terminal(self))
        ui.actionSave_As.triggered.connect(lambda: actions.save_terminal_as(self))
        ui.actionExit.triggered.connect(self.close)
        ui.actionCopy.triggered.connect(ui.data_textEdit.copy)
        ui.actionSelect_All.triggered.connect(ui.data_textEdit.selectAll)
        ui.actionClear_Screen.triggered.connect(self._clear_terminal)
        ui.actionClear_Cache.triggered.connect(self._clear_buffers)
        ui.actionReset_terminal.triggered.connect(self._reset_terminal)
        ui.actionBasic_View.triggered.connect(lambda: actions.set_advanced_view(self, False))
        ui.actionAdvanced_View.triggered.connect(lambda: actions.set_advanced_view(self, True))
        ui.actionPreferences.triggered.connect(self._open_preferences)
        ui.actionHelp_2.triggered.connect(lambda: actions.show_help(self))
        ui.actionAbout.triggered.connect(lambda: actions.show_about(self))
        ui.actionCheck_for_updates.triggered.connect(lambda: actions.check_for_updates(self))

    # ------------------------------------------------------------------
    # Appearance / language
    # ------------------------------------------------------------------
    def apply_appearance(self) -> None:
        """(Re)apply the Adwaita theme and the terminal font from settings."""
        theme = self.settings.get("theme", DEFAULT_THEME)
        terminal_font = self.settings.get("font_family", DEFAULT_FONT_FAMILY)
        terminal_size = int(self.settings.get("font_size", DEFAULT_FONT_SIZE))

        ui_font = detect_ui_font()
        stylesheet = load_stylesheet(
            theme=theme,
            font_family=ui_font,
            font_size=10.5,
            terminal_font=terminal_font,
            terminal_size=terminal_size,
        )

        app = QApplication.instance()
        if app is not None:
            ui_font_obj = QFont(ui_font)
            ui_font_obj.setPointSizeF(10.5)
            app.setFont(ui_font_obj)
            app.setStyleSheet(stylesheet)

        # Keep the rich-text document consistent with the terminal font.
        document = self.ui.data_textEdit.document()
        document.setDefaultFont(QFont(terminal_font, terminal_size))

    def apply_language(self) -> None:
        """Retranslate all user-visible strings for the active language."""
        tr = self.translator.tr
        ui = self.ui

        ui.menuFile.setTitle(tr("menu.file"))
        ui.menuEdit.setTitle(tr("menu.edit"))
        ui.menuSetup.setTitle(tr("menu.settings"))
        ui.menuControl.setTitle(tr("menu.connection"))
        ui.menuWindow.setTitle(tr("menu.view"))
        ui.menuHelp.setTitle(tr("menu.help"))

        ui.actionNew.setText(tr("action.new"))
        ui.actionSave.setText(tr("action.save"))
        ui.actionSave_As.setText(tr("action.save_as"))
        ui.actionExit.setText(tr("action.exit"))
        ui.actionCopy.setText(tr("action.copy"))
        ui.actionSelect_All.setText(tr("action.select_all"))
        ui.actionClear_Screen.setText(tr("action.clear_screen"))
        ui.actionClear_Cache.setText(tr("action.clear_buffer"))
        ui.actionReset_terminal.setText(tr("action.reset_terminal"))
        ui.actionPreferences.setText(tr("action.preferences"))
        ui.actionBasic_View.setText(tr("action.basic_view"))
        ui.actionAdvanced_View.setText(tr("action.advanced_view"))
        ui.actionHelp_2.setText(tr("action.help"))
        ui.actionAbout.setText(tr("action.about"))
        ui.actionCheck_for_updates.setText(tr("action.check_updates"))

        ui.connectionGroup.setTitle(tr("group.connection"))
        ui.infoGroup.setTitle(tr("group.device"))
        ui.refresh_button.setText("⟳  " + tr("button.scan"))
        ui.label_22.setText(tr("label.port"))
        ui.label_25.setText(tr("label.baud"))
        ui.label_26.setText(tr("label.databits"))
        ui.label_28.setText(tr("label.parity"))
        ui.label_29.setText(tr("label.stopbits"))
        ui.label_30.setText(tr("label.flow"))
        ui.label_27.setText(tr("label.timeout"))
        ui.label.setText(tr("label.lineending"))
        ui.terminalTitleLabel.setText(tr("label.terminal"))
        ui.send_button.setText(tr("button.send"))
        ui.start_button.setText(
            tr("button.disconnect") if self._connected else tr("button.connect")
        )
        ui.data_textEdit.setPlaceholderText(tr("terminal.placeholder"))
        ui.send_data_text.setPlaceholderText(tr("send.placeholder"))

        self._set_status("connected" if self._connected else "idle")

    # ------------------------------------------------------------------
    # Ports
    # ------------------------------------------------------------------
    def refresh_ports(self) -> None:
        combo = self.ui.port_comboBox
        previous = combo.currentData()
        combo.clear()
        ports = available_ports()
        if ports:
            for info in ports:
                # Show a short label (e.g. "ttyUSB0") but keep the real device
                # path as item data so connecting still uses "/dev/ttyUSB0".
                combo.addItem(display_name(info.device), info.device)
                combo.setItemData(
                    combo.count() - 1, info.detail_text(), Qt.ItemDataRole.ToolTipRole
                )
            if isinstance(previous, str):
                index = combo.findData(previous)
                if index >= 0:
                    combo.setCurrentIndex(index)
        else:
            combo.addItem(_NO_PORT_TEXT, None)

    # ------------------------------------------------------------------
    # Connection lifecycle
    # ------------------------------------------------------------------
    def _on_connect_clicked(self) -> None:
        if self._connected:
            self._disconnect()
            return

        port = self.ui.port_comboBox.currentData() or self.ui.port_comboBox.currentText().strip()
        if not port or port == _NO_PORT_TEXT:
            QMessageBox.warning(self, "No port", "Please select a serial port first.")
            return

        try:
            self._open_serial(port)
        except Exception as exc:
            QMessageBox.critical(
                self, "Connection failed", f"Could not open {port}:\n{exc}"
            )
            return

        self._start_worker(port)

    def _open_serial(self, port: str) -> None:
        ui = self.ui
        details = port_details_by_device(port)
        flow = _FLOW_MAP.get(ui.flow_comboBox.currentText(), _FLOW_MAP["None"])
        self._serial = Serial(
            port=port,
            baudrate=int(ui.baudrate_comboBox.currentText()),
            bytesize=int(ui.len_comboBox.currentText()),
            parity=_PARITY_MAP.get(ui.parity_comboBox.currentText(), PARITY_NONE),
            stopbits=float(ui.bit_comboBox.currentText()),
            timeout=float(ui.timeout_comboBox.currentText()),
            xonxoff=flow["xonxoff"],
            rtscts=flow["rtscts"],
            dsrdtr=flow["dsrdtr"],
        )
        if not self._serial.is_open:
            self._serial.open()

        if details is not None:
            ui.options_textEdit.setPlainText(details.detail_text())
        else:
            ui.options_textEdit.setPlainText(f"Port: {port}")

    def _start_worker(self, port: str) -> None:
        self._thread = QThread(self)
        self._worker = SerialReader(self._serial)
        self._worker.moveToThread(self._thread)
        self._thread.started.connect(self._worker.run)
        self._worker.data_received.connect(self._on_data_received)
        self._worker.error_occurred.connect(self._on_serial_error)
        self._worker.finished.connect(self._thread.quit)
        self._worker.finished.connect(self._worker.deleteLater)
        self._thread.finished.connect(self._thread.deleteLater)
        self._thread.start()

        self._connected = True
        self._set_config_enabled(False)
        self._set_status("connected")
        self.ui.start_button.setText(self.translator.tr("button.disconnect"))

    def _disconnect(self) -> None:
        # Mark as disconnected first so a late read error during shutdown is
        # ignored by the error handler.
        self._connected = False
        worker, thread = self._worker, self._thread
        self._worker = None
        self._thread = None

        if worker is not None:
            worker.stop()

        # Close the port before waiting so a blocked read returns promptly.
        if self._serial is not None:
            try:
                if self._serial.is_open:
                    self._serial.close()
            except Exception:
                pass
        self._serial = None

        if thread is not None:
            thread.quit()
            thread.wait(2000)

        self._set_config_enabled(True)
        self._set_status("disconnected")
        self.ui.start_button.setText(self.translator.tr("button.connect"))
        self.ui.options_textEdit.setPlainText("Disconnected.")

    def _on_serial_error(self, message: str) -> None:
        if not self._connected:
            # Error raised while we were deliberately tearing the port down.
            return
        QMessageBox.warning(
            self,
            "Serial port error",
            "The serial port reported an error and the connection was closed:\n"
            f"{message}",
        )
        self._disconnect()

    def _set_config_enabled(self, enabled: bool) -> None:
        for name in (
            "port_comboBox",
            "baudrate_comboBox",
            "len_comboBox",
            "parity_comboBox",
            "bit_comboBox",
            "flow_comboBox",
            "timeout_comboBox",
            "lineEnd_comboBox",
            "refresh_button",
        ):
            getattr(self.ui, name).setEnabled(enabled)

    # ------------------------------------------------------------------
    # Data
    # ------------------------------------------------------------------
    def _on_data_received(self, text: str) -> None:
        self._rx_bytes += len(text.encode("utf-8", errors="replace"))
        if self.settings.get("timestamps", False):
            text = self._prefix_timestamps(text)

        edit = self.ui.data_textEdit
        cursor = edit.textCursor()
        cursor.movePosition(cursor.MoveOperation.End)
        edit.setTextCursor(cursor)
        edit.insertHtml(ansi_to_html(text))
        edit.verticalScrollBar().setValue(edit.verticalScrollBar().maximum())
        self._update_counters()

    @staticmethod
    def _prefix_timestamps(text: str) -> str:
        from datetime import datetime

        stamp = datetime.now().strftime("%H:%M:%S.%f")[:-3]
        lines = text.split("\n")
        prefixed = [lines[0]] + [f"[{stamp}] {line}" for line in lines[1:]]
        return "\n".join(prefixed)

    def _send_data(self) -> None:
        if not self._connected or self._serial is None:
            QMessageBox.information(
                self, "Not connected", "Connect to a serial port before sending data."
            )
            return

        text = self.ui.send_data_text.toPlainText()
        if not text:
            return
        ending = _LINE_ENDINGS.get(self.ui.lineEnd_comboBox.currentText(), b"")
        payload = text.encode("utf-8") + ending
        try:
            self._serial.write(payload)
            self._serial.flush()
        except Exception as exc:
            QMessageBox.warning(self, "Send failed", f"Could not send data:\n{exc}")
            return

        self._tx_bytes += len(payload)
        self._update_counters()
        self._blink_indicator()

    def _blink_indicator(self) -> None:
        self.ui.indicate_button.setChecked(True)
        QTimer.singleShot(250, lambda: self.ui.indicate_button.setChecked(False))

    def _update_counters(self) -> None:
        self.ui.rxCountLabel.setText(f"RX {self._human_bytes(self._rx_bytes)}")
        self.ui.txCountLabel.setText(f"TX {self._human_bytes(self._tx_bytes)}")

    @staticmethod
    def _human_bytes(count: int) -> str:
        if count < 1024:
            return f"{count} B"
        if count < 1024 * 1024:
            return f"{count / 1024:.1f} KB"
        return f"{count / (1024 * 1024):.1f} MB"

    # ------------------------------------------------------------------
    # Terminal actions
    # ------------------------------------------------------------------
    def _clear_terminal(self) -> None:
        self.ui.data_textEdit.clear()

    def _clear_buffers(self) -> None:
        self.ui.data_textEdit.clear()
        self.ui.send_data_text.clear()

    def _reset_terminal(self) -> None:
        self.ui.data_textEdit.clear()
        self.ui.send_data_text.clear()
        self.reset_counters()

    def reset_counters(self) -> None:
        self._rx_bytes = 0
        self._tx_bytes = 0
        self._update_counters()

    # ------------------------------------------------------------------
    # Preferences
    # ------------------------------------------------------------------
    def _open_preferences(self) -> None:
        dialog = PreferencesDialog(self.settings, self)
        if dialog.exec() == dialog.DialogCode.Accepted:
            self.translator.set_language(self.settings.get("language", "en"))
            self.apply_appearance()
            self.apply_language()

    # ------------------------------------------------------------------
    # Status
    # ------------------------------------------------------------------
    def _set_status(self, state: str) -> None:
        labels = {
            "connected": self.translator.tr("status.connected"),
            "disconnected": self.translator.tr("status.disconnected"),
            "idle": self.translator.tr("status.idle"),
        }
        self.ui.status_label.setText(labels.get(state, labels["idle"]))
        self._set_dynamic_property(self.ui.status_label, "state", state)
        self._set_dynamic_property(self.ui.statusDot, "state", state)
        self._set_dynamic_property(
            self.ui.start_button, "state", "connected" if self._connected else "idle"
        )

    @staticmethod
    def _set_dynamic_property(widget, name: str, value: str) -> None:
        widget.setProperty(name, value)
        style = widget.style()
        style.unpolish(widget)
        style.polish(widget)
        widget.update()

    # ------------------------------------------------------------------
    # Qt overrides
    # ------------------------------------------------------------------
    def eventFilter(self, obj, event) -> bool:  # noqa: N802 (Qt naming)
        if obj is self.ui.send_data_text and event.type() == QEvent.Type.KeyPress:
            if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
                self._send_data()
                return True
        return super().eventFilter(obj, event)

    def closeEvent(self, event) -> None:  # noqa: N802 (Qt naming)
        if self._connected:
            self._disconnect()
        super().closeEvent(event)
