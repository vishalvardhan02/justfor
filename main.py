from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
from pydantic import BaseModel
import gunicorn

app = FastAPI()


@app.get('/')
def home():
    return "hello"

@app.get('/append_to_file/{text}')
def append_to_file(text):
    string_to_append = text
    file_path = "C:/Users/vixha/OneDrive/Desktop/myfile.txt"
    with open(file_path, 'w') as file:
        content = text
        file.write(content)
    return FileResponse(file_path, filename="myfile.txt")
    

