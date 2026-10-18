# -*- coding: utf-8 -*-
"""Very small runtime translation table (English / Turkish).

Only the user interface strings that matter are translated.  Missing keys fall
back to English, so adding a new language (or a new string) never breaks the
application.
"""

from __future__ import annotations

LANGUAGES = {"en": "English", "tr": "Türkçe"}

_EN = {
    "menu.file": "File",
    "menu.edit": "Edit",
    "menu.settings": "Settings",
    "menu.connection": "Connection",
    "menu.view": "View",
    "menu.help": "Help",
    "action.new": "New",
    "action.save": "Save",
    "action.save_as": "Save As…",
    "action.exit": "Exit",
    "action.copy": "Copy",
    "action.select_all": "Select All",
    "action.clear_screen": "Clear Screen",
    "action.clear_buffer": "Clear Buffers",
    "action.reset_terminal": "Reset Terminal",
    "action.preferences": "Preferences…",
    "action.basic_view": "Basic View",
    "action.advanced_view": "Advanced View",
    "action.help": "Help",
    "action.about": "About",
    "action.check_updates": "Check for Updates",
    "group.connection": "Connection",
    "group.device": "Device",
    "label.port": "Port",
    "label.baud": "Baud",
    "label.databits": "Data",
    "label.timeout": "Timeout",
    "label.parity": "Parity",
    "label.stopbits": "Stop",
    "label.flow": "Flow",
    "label.lineending": "Line end",
    "label.status": "Status",
    "label.terminal": "Terminal",
    "label.send": "Send",
    "button.connect": "CONNECT",
    "button.disconnect": "DISCONNECT",
    "button.send": "Send",
    "button.scan": "Scan ports",
    "status.connected": "Connected",
    "status.disconnected": "Disconnected",
    "status.idle": "Not connected",
    "terminal.placeholder": "Received data will appear here…",
    "send.placeholder": "Type data to send and press Enter…",
}

_TR = {
    "menu.file": "Dosya",
    "menu.edit": "Düzen",
    "menu.settings": "Ayarlar",
    "menu.connection": "Bağlantı",
    "menu.view": "Görünüm",
    "menu.help": "Yardım",
    "action.new": "Yeni",
    "action.save": "Kaydet",
    "action.save_as": "Farklı Kaydet…",
    "action.exit": "Çıkış",
    "action.copy": "Kopyala",
    "action.select_all": "Tümünü Seç",
    "action.clear_screen": "Ekranı Temizle",
    "action.clear_buffer": "Tamponları Temizle",
    "action.reset_terminal": "Terminali Sıfırla",
    "action.preferences": "Tercihler…",
    "action.basic_view": "Basit Görünüm",
    "action.advanced_view": "Gelişmiş Görünüm",
    "action.help": "Yardım",
    "action.about": "Hakkında",
    "action.check_updates": "Güncellemeleri Denetle",
    "group.connection": "Bağlantı",
    "group.device": "Cihaz",
    "label.port": "Port",
    "label.baud": "Baud",
    "label.databits": "Veri",
    "label.timeout": "Süre",
    "label.parity": "Parite",
    "label.stopbits": "Dur",
    "label.flow": "Akış",
    "label.lineending": "Satır sonu",
    "label.status": "Durum",
    "label.terminal": "Terminal",
    "label.send": "Gönder",
    "button.connect": "BAĞLAN",
    "button.disconnect": "BAĞLANTIYI KES",
    "button.send": "Gönder",
    "button.scan": "Portları tara",
    "status.connected": "Bağlı",
    "status.disconnected": "Bağlı değil",
    "status.idle": "Bağlı değil",
    "terminal.placeholder": "Alınan veriler burada görünecek…",
    "send.placeholder": "Gönderilecek veriyi yazıp Enter'a basın…",
}

_TABLES = {"en": _EN, "tr": _TR}


class Translator:
    """Resolve translation keys for the active language."""

    def __init__(self, language: str = "en") -> None:
        self._language = language if language in _TABLES else "en"

    @property
    def language(self) -> str:
        return self._language

    def set_language(self, language: str) -> None:
        if language in _TABLES:
            self._language = language

    def tr(self, key: str, default: str | None = None) -> str:
        table = _TABLES.get(self._language, _EN)
        if key in table:
            return table[key]
        if key in _EN:
            return _EN[key]
        return default if default is not None else key
