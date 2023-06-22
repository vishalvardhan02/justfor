from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
from pydantic import BaseModel
import gunicorn
import requests
app = FastAPI()


@app.get('/')
def home():
    return "hello"

@app.get('/append_to_file/{text}')
def append_to_file(text):
    return "hello"
    

