#!/bin/bash

# Démarrer les serveurs FastAPI en tant que processus séparés
uvicorn appi1:app --host 0.0.0.0 --port 8001 &
uvicorn appi2:app --host 0.0.0.0 --port 8002 &

# Démarrer le serveur principal FastAPI
uvicorn main:app --host 0.0.0.0 --port 8000
