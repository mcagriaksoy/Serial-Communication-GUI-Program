@echo off
REM AFCOM launcher for Windows - no manual virtualenv activation required.
REM Just double-click or run:  run.bat
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo ==^> First run: creating virtual environment in .venv ...
    python -m venv .venv
    .venv\Scripts\python.exe -m pip install --upgrade pip
    echo ==^> Installing dependencies ...
    .venv\Scripts\python.exe -m pip install -r requirements.txt
)

.venv\Scripts\python.exe main.py %*
