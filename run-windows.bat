@echo off
:: Check for Python Installation
py -3 --version >nul
if errorlevel 1 goto errorNoPython
    py -3 main.py
    pause
goto:eof

:errorNoPython
echo "Error: Python not installed"
pause