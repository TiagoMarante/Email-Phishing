#!/bin/sh
set -e

#. /venv/bin/activate
uvicorn app.main:app --reload --host=0.0.0.0 --proxy-headers
