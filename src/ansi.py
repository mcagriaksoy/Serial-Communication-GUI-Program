# -*- coding: utf-8 -*-
"""Helpers for turning raw serial data into safe, styled HTML.

Serial devices frequently emit ANSI escape sequences for colour.  Qt's rich
text renderer understands a small subset of HTML, so we translate the ANSI
sequences into ``<span>`` elements and HTML-escape everything else.  This keeps
received data from being interpreted as markup.
"""

from __future__ import annotations

import re
from html import escape

ANSI_ESCAPE_RE = re.compile(r"\x1b\[[0-9;]*[A-Za-z]")
ANSI_SGR_RE = re.compile(r"\x1b\[([0-9;]*)m")

_FG_COLORS = {
    "30": "#2e3440",
    "31": "#e06c75",
    "32": "#98c379",
    "33": "#e5c07b",
    "34": "#61afef",
    "35": "#c678dd",
    "36": "#56b6c2",
    "37": "#d7dae0",
    "90": "#7f848e",
    "91": "#ff7b72",
    "92": "#7ee787",
    "93": "#f2cc60",
    "94": "#79c0ff",
    "95": "#d2a8ff",
    "96": "#56d4dd",
    "97": "#ffffff",
}


def strip_ansi_codes(text: str) -> str:
    """Return *text* with every ANSI escape sequence removed."""
    return ANSI_ESCAPE_RE.sub("", text)


def ansi_to_html(text: str) -> str:
    """Convert ANSI coloured text to an HTML fragment.

    The returned fragment is safe to pass to ``QTextEdit.insertHtml``: all
    literal text is HTML-escaped, and spans are balanced.
    """
    output: list[str] = []
    fg: str | None = None
    bold = False
    open_span = False

    def close_span() -> None:
        nonlocal open_span
        if open_span:
            output.append("</span>")
            open_span = False

    def open_style_span() -> None:
        nonlocal open_span
        styles = []
        if fg is not None:
            styles.append(f"color:{fg}")
        if bold:
            styles.append("font-weight:bold")
        if styles:
            output.append(f'<span style="{";".join(styles)}">')
            open_span = True

    index = 0
    for match in ANSI_SGR_RE.finditer(text):
        # Emit the text before this escape sequence.
        plain = text[index:match.start()]
        if plain:
            escaped = escape(plain).replace("\r\n", "<br>").replace("\n", "<br>").replace("\r", "<br>")
            output.append(escaped)
        index = match.end()

        params = [p for p in match.group(1).split(";") if p != ""] or ["0"]
        for param in params:
            if param == "0":
                close_span()
                fg = None
                bold = False
            elif param == "1":
                bold = True
            elif param == "22":
                bold = False
            elif param in _FG_COLORS:
                fg = _FG_COLORS[param]
            elif param == "39":
                fg = None
            # Re-emit a span whenever the visible style changed.
            if open_span:
                close_span()
            open_style_span()

    tail = text[index:]
    if tail:
        escaped = escape(tail).replace("\r\n", "<br>").replace("\n", "<br>").replace("\r", "<br>")
        output.append(escaped)

    close_span()
    return "".join(output)
