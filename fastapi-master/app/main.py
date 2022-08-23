import imp
import json
from typing import Optional, Set, Dict
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Json


# External Packages
from app.models.email import Email
from app.utils.utils import to_json
from app.utils.word_analysis import *

model = joblib.load("../fastapi-master/app/ML model/trainedForest.joblib")

app = FastAPI()


@app.get("/health/")
async def get_health_status():
    return to_json("Healthy")


@app.post("/email/")
async def post_email(email: Email):
    content = email.email
    res = email_analysis(content, model)
    return to_json(res)
