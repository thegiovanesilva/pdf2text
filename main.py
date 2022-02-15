from fastapi import FastAPI, File, UploadFile
from os import remove
from pdfminer.high_level import extract_text 
from shutil import copyfileobj
from uuid import uuid4

app = FastAPI()

@app.post('/extract/')
def extract(file: UploadFile = File(...)):
    filename = str(uuid4())
    with open(filename,'wb') as buffer:
        copyfileobj (file.file, buffer)
    text = extract_text(filename)
    remove(filename)
    return { 'text': text }
