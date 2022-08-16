#!/bin/sh
set -e

#. /venv/bin/activate

gunicorn app.main:app -b localhost:8001 -k uvicorn.workers.UvicornWorker --workers 4
