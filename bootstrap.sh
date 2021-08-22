#!/bin/bash

echo "Creating local virtualenv"
python3 -m venv .venv

echo "Entering virtualenv"
source .venv/bin/activate

echo "Installing/Upgrading dependencies"
pip install --upgrade pip
pip install -e ".[test]"

echo "Drop to shell"
eval "$SHELL"
