#!/bin/sh
if command -v python -3 &>/dev/null; then
    echo Installing Dependencies
    pip3 install -r requirements/dev.txt
    echo Running Tests
    python3 -m pytest tests/
    echo Running App
    python3 main.py
else
    echo Python 3 is not installed
fi
read -p "Press enter to continue..."