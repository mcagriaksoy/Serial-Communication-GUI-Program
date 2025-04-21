
call cmd.exe /c "pyside6-uic help.ui -o help.py"
call cmd.exe /c "pyside6-uic settings.ui -o settings.py"
call cmd.exe /c "pyside6-uic main_window.ui -o main_window.py"
call cmd.exe /c "pyside6-rcc resources.qrc -o resources_rc.py"
REM SUCCESS
pause