# -*- coding: utf-8 -*-
"""Cross-platform serial port discovery helpers."""

from __future__ import annotations

from dataclasses import dataclass

try:  # pragma: no cover - import guard
    from serial.tools import list_ports
except ImportError:  # pragma: no cover
    list_ports = None  # type: ignore[assignment]


@dataclass(frozen=True)
class PortInfo:
    """A friendly summary of a serial port."""

    device: str
    description: str = ""
    manufacturer: str = ""
    hwid: str = ""

    def label(self) -> str:
        if self.description and self.description != "n/a":
            return f"{self.device} - {self.description}"
        return self.device

    def detail_text(self) -> str:
        lines = [f"Port: {self.device}"]
        if self.description:
            lines.append(f"Description: {self.description}")
        if self.manufacturer:
            lines.append(f"Manufacturer: {self.manufacturer}")
        if self.hwid:
            lines.append(f"HWID: {self.hwid}")
        return "\n".join(lines)


def available_ports() -> list[PortInfo]:
    """Return the serial ports currently present on the system."""
    if list_ports is None:
        return []
    ports: list[PortInfo] = []
    for port in list_ports.comports():
        ports.append(
            PortInfo(
                device=port.device,
                description=port.description or "",
                manufacturer=getattr(port, "manufacturer", "") or "",
                hwid=port.hwid or "",
            )
        )
    ports.sort(key=lambda item: item.device)
    return ports


def port_names() -> list[str]:
    """Return just the device names (used to populate combo boxes)."""
    return [port.device for port in available_ports()]


_DEV_PREFIX = "/dev/"


def display_name(device: str) -> str:
    """Return a short, human friendly label for a device path.

    On POSIX every device shares the ``/dev/`` prefix, so it only adds noise in
    a narrow combo box; it is stripped for display.  Windows ``COM`` ports and
    anything else are returned unchanged.
    """
    if device.startswith(_DEV_PREFIX):
        return device[len(_DEV_PREFIX):]
    return device


def port_details_by_device(device: str) -> PortInfo | None:
    """Return the :class:`PortInfo` for *device*, or ``None`` if unknown."""
    for port in available_ports():
        if port.device == device:
            return port
    return None
