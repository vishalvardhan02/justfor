from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
from pydantic import BaseModel
import gunicorn
import requests
import base64
import github
import base64

app = FastAPI()


@app.get('/')
def home():
    return "hello"

@app.get('/append_to_file/{text}')
def append_to_file(text):
    # g = github.Github("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")

    # repo = g.get_user().get_repo("justfor")
    # file = repo.get_contents("myfile.txt")

    # current_content = file.content
    # current_content_decoded = base64.b64decode(current_content).decode()
    # new_content = ''
    # print(current_content_decoded)
    # if current_content_decoded == '\n':
    #     new_content = text
    # else:
    #     new_content = current_content_decoded + '\n' + '\n' + text 
    
    # repo.update_file("myfile.txt", "Update myfile.txt", new_content, file.sha)

    return "hello"
    

