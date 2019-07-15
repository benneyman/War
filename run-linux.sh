#!/bin/sh
if command -v python -3 &>/dev/null; then
    py -3 main.py
else
    echo Python 3 is not installed
fi
read -p "Press enter to continue..."