@echo off
:: Check for Python Installation
py -3 --version >nul
if errorlevel 1 goto errorNoPython
    echo Installing Dependencies
    pip3 install -r requirements/dev.txt
    echo Running Tests
    py -3 -m pytest tests/
    echo Running App
    py -3 main.py
    pause
goto:eof

:errorNoPython
echo "Error: Python not installed"
pause