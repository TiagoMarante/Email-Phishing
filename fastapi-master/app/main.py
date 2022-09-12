import imp
import json
from typing import Optional, Set, Dict
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Json


# External Packages
from app.models.email import Email
from app.models.url import Url
from app.utils.site_analyser import url_analyser
from app.utils.utils import to_json
from app.utils.word_analysis import *

model_email = joblib.load("app/ML model/trainedForest.joblib")
model_url = joblib.load("app/ML model/trained_Forest_tunned.joblib")

app = FastAPI()


@app.get("/health/")
async def get_health_status():
    return to_json("Healthy")


@app.post("/email/")
async def post_email(email: Email):
    content = email.email
    res = email_analysis(content, model_email)
    return to_json(res)


@app.post("/url/")
async def post_url(url: Url):
    content = url.url
    res = url_analyser(content, model_url)
    return to_json(res)
