#!/bin/bash
sleep 30
export FLASK_APP=/app/api/__init__.py

flask db init
flask db migrate 
flask db upgrade
python /app/run.py
