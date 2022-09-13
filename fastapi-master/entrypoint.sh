#!/bin/sh
#set -e

#. /venv/bin/activate
#http://0.0.0.0:8001/docs#/

#gunicorn app.main:app -b localhost:8001 -k uvicorn.workers.UvicornWorker --workers 4
uvicorn app.main:app --host=0.0.0.0 --port 8001
