# -*- coding: utf-8 -*-
"""Background reader that pumps data from a serial port into Qt signals.

The worker runs inside a :class:`QThread` and never touches widgets directly;
it only emits signals.  Reads are performed in chunks using ``in_waiting`` so a
fast device does not turn into thousands of tiny 1-byte reads.
"""

from __future__ import annotations

import re
import threading

from PySide6.QtCore import QObject, Signal

try:  # pragma: no cover - import guard mirrors the rest of the app
    from serial import Serial, SerialException
except ImportError:  # pragma: no cover
    Serial = object  # type: ignore[assignment]
    SerialException = Exception  # type: ignore[assignment]

# A trailing, possibly incomplete ANSI escape sequence is withheld until the
# next read so that colour codes are not split across two emissions.
_PARTIAL_ESCAPE_RE = re.compile(r"\x1b\[[0-9;]*$")


class SerialReader(QObject):
    """Read from a serial device in the background and emit received text."""

    data_received = Signal(str)
    error_occurred = Signal(str)
    finished = Signal()

    def __init__(self, serial_port: "Serial", encoding: str = "utf-8") -> None:
        super().__init__()
        self._serial = serial_port
        self._encoding = encoding
        self._stop = threading.Event()
        self._pending = ""

    # -- control -----------------------------------------------------------
    def stop(self) -> None:
        """Ask the worker loop to exit at the next opportunity."""
        self._stop.set()

    @property
    def running(self) -> bool:
        return not self._stop.is_set()

    # -- main loop ---------------------------------------------------------
    def run(self) -> None:
        """Read until :meth:`stop` is called or the port errors out."""
        try:
            while not self._stop.is_set():
                try:
                    waiting = getattr(self._serial, "in_waiting", 0) or 0
                    chunk = self._serial.read(max(1, waiting))
                except SerialException as exc:
                    self.error_occurred.emit(str(exc))
                    break
                except Exception as exc:  # pragma: no cover - defensive
                    self.error_occurred.emit(str(exc))
                    break

                if not chunk:
                    continue

                text = self._pending + chunk.decode(self._encoding, errors="replace")
                partial = _PARTIAL_ESCAPE_RE.search(text)
                if partial:
                    self._pending = text[partial.start():]
                    text = text[:partial.start()]
                else:
                    self._pending = ""

                if text:
                    self.data_received.emit(text)
        finally:
            if self._pending:
                self.data_received.emit(self._pending)
                self._pending = ""
            self.finished.emit()
