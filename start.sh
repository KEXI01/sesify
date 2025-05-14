#!/bin/bash

set -e
export FLASK_APP=app:create_app
gunicorn -w 4 -b 0.0.0.0:${PORT:-8080} app:create_app &
python3 bot.py
