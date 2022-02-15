import PyPDF2
from fastapi import FastAPI, File, UploadFile

app = FastAPI()

@app.post('/extract/')
def extract(file: UploadFile = File(...)):
    pdfFileObj = open(file.filename,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pagehandle = pdfReader.getPage(0)
    text = pagehandle.extractText()
    return {'text': text}
