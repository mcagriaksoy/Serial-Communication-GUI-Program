# -*- coding: utf-8 -*-
"""Persistence for user preferences.

The store is a very small wrapper around a JSON file.  It never raises on load
or save: a corrupt or missing file simply falls back to defaults, which keeps
the application usable no matter what.
"""

from __future__ import annotations

import json
from typing import Any, Dict

from .constants import DEFAULT_SETTINGS, SETTINGS_FILE


class SettingsStore:
    """Load and persist a dictionary of user preferences."""

    def __init__(self, path=SETTINGS_FILE) -> None:
        self._path = path
        self._data: Dict[str, Any] = dict(DEFAULT_SETTINGS)
        self.load()

    # -- public API --------------------------------------------------------
    @property
    def path(self):
        return self._path

    def load(self) -> Dict[str, Any]:
        """Read settings from disk, merging on top of the defaults."""
        data = dict(DEFAULT_SETTINGS)
        try:
            if self._path.exists():
                with open(self._path, "r", encoding="utf-8") as handle:
                    loaded = json.load(handle)
                if isinstance(loaded, dict):
                    data.update(loaded)
        except (OSError, ValueError):
            # Corrupt or unreadable file: keep defaults rather than crashing.
            pass
        self._data = data
        return self._data

    def save(self) -> None:
        """Write the current settings to disk (best effort)."""
        try:
            self._path.parent.mkdir(parents=True, exist_ok=True)
            with open(self._path, "w", encoding="utf-8") as handle:
                json.dump(self._data, handle, ensure_ascii=False, indent=2)
        except OSError:
            pass

    def get(self, key: str, default: Any = None) -> Any:
        return self._data.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self._data[key] = value

    def update(self, values: Dict[str, Any]) -> None:
        self._data.update(values)

    def as_dict(self) -> Dict[str, Any]:
        return dict(self._data)
