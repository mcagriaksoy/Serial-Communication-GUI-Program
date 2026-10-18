@echo off
REM Regenerate the Python modules from the Qt Designer .ui files.
python "%~dp0build_ui.py"
pause
