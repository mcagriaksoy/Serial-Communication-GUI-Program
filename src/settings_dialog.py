# -*- coding: utf-8 -*-
"""The Preferences dialog: a thin controller over the generated ``settings`` UI."""

from __future__ import annotations

from PySide6.QtWidgets import QDialog

from .settings_store import SettingsStore
from .ui_loader import load_ui_class

_THEME_ORDER = ["system", "dark", "light"]
_LANGUAGE_ORDER = ["en", "tr"]


class PreferencesDialog(QDialog):
    """Edit application preferences and persist them on accept."""

    def __init__(self, settings: SettingsStore, parent=None) -> None:
        super().__init__(parent)
        self._settings = settings

        ui_class = load_ui_class("settings", "Ui_Dialog")
        self.ui = ui_class()
        self.ui.setupUi(self)

        self._populate()
        self.ui.buttonBox.accepted.connect(self._on_accept)

    # -- helpers -----------------------------------------------------------
    def _populate(self) -> None:
        theme = self._settings.get("theme", "dark")
        index = _THEME_ORDER.index(theme) if theme in _THEME_ORDER else 1
        self.ui.themeComboBox.setCurrentIndex(index)

        language = self._settings.get("language", "en")
        self.ui.languageComboBox.setCurrentIndex(
            _LANGUAGE_ORDER.index(language) if language in _LANGUAGE_ORDER else 0
        )

        self.ui.fontComboBox.setCurrentFont(self._settings.get("font_family", "Consolas"))
        self.ui.fontSize_spinBox.setValue(int(self._settings.get("font_size", 11)))
        self.ui.timestampsCheckBox.setChecked(bool(self._settings.get("timestamps", False)))

    def _on_accept(self) -> None:
        self._settings.update(
            {
                "theme": _THEME_ORDER[self.ui.themeComboBox.currentIndex()],
                "language": _LANGUAGE_ORDER[self.ui.languageComboBox.currentIndex()],
                "font_family": self.ui.fontComboBox.currentFont().family(),
                "font_size": self.ui.fontSize_spinBox.value(),
                "timestamps": self.ui.timestampsCheckBox.isChecked(),
            }
        )
        self._settings.save()
        self.accept()
