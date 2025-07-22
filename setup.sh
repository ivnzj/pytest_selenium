#!/bin/bash

set -e
VENV_DIR=".venv"

echo "Checking if python3-venv is installed."
if ! dpkg -s python3-venv >/dev/null 2>&1; then
    echo "Installing python3-venv..."
    sudo apt update
    sudo apt upgrade -y
    sudo apt install -y python3-venv
else
    echo "python3-venv is already installed."
fi

if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment at $VENV_DIR."
    python3 -m venv "$VENV_DIR"
else
    echo "Virtual environment already exists at $VENV_DIR."
fi

echo "Activating virtual environment."
source "$VENV_DIR/bin/activate"

echo "Installing requirements."
pip install --upgrade pip
pip install -r requirements.txt