#!/usr/bin/fish
python3.12 -m venv .venv
.venv/bin/pip install --upgrade pip
.venv/bin/pip install -r requirements.txt
.venv/bin/pip uninstall nmrespy
.venv/bin/pip install -e ../../NMR-EsPy
