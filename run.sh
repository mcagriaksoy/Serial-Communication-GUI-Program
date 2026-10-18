#!/usr/bin/env bash
#
# AFCOM launcher - no manual virtualenv activation required.
#
#   ./run.sh                 run the app
#   ./run.sh <args>          extra arguments are forwarded to main.py
#
# The virtual environment lives in .venv/ at the project root and is reused
# every time, so you never have to run "source .venv/bin/activate" again.
set -euo pipefail

cd "$(dirname "$0")"
VENV=".venv"
PY="$VENV/bin/python"

# --- system dependency check (Linux only) ---------------------------------
if [ "$(uname)" = "Linux" ]; then
    QXCB="$(find "$VENV" -name libqxcb.so 2>/dev/null | head -1 || true)"
    if [ -n "${QXCB}" ] && ldd "$QXCB" 2>/dev/null | grep -q "not found"; then
        echo "!! Qt is missing system libraries. Install them with:"
        echo
        echo "   sudo apt update && sudo apt install -y \\"
        echo "       libxcb-cursor0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 \\"
        echo "       libxcb-randr0 libxcb-render-util0 libxcb-shape0 \\"
        echo "       libxcb-xinerama0 libxkbcommon-x11-0 libgl1"
        echo
    fi
fi

# --- virtual environment --------------------------------------------------
if [ ! -x "$PY" ]; then
    echo "==> First run: creating virtual environment in $VENV ..."
    python3 -m venv "$VENV"
    "$PY" -m pip install --upgrade pip >/dev/null
    echo "==> Installing dependencies ..."
    "$PY" -m pip install -r requirements.txt
fi

exec "$PY" main.py "$@"
