import imp
from typing import Optional, Set, Dict
from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Json


# External Packages
from app.models.email import Email
from app.utils.utils import to_json
from app.utils.word_analysis import *

app = FastAPI()



@app.get("/health/")
async def get_health_status():
    return to_json("Healthy")



@app.post("/email/")
async def post_email_(email: Email):
    content = email.email
    email_analysis(content)
    return to_json("Email")