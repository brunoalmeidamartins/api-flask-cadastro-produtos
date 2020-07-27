#!/bin/bash
sleep 30 #Tempo para subir o banco de dados
export FLASK_APP=/app/api/__init__.py
flask db init
flask db migrate 
flask db upgrade
python /app/run.py #Roda a aplicação
