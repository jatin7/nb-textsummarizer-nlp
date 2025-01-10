from fastapi import FastAPI, File, UploadFile, Form
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from textSummarizer.pipeline.prediction import PredictionPipeline
import fitz
app = FastAPI()
text: str = "What is text Summarizer and how does it work?"
@app.get("/")
async def index():
    return RedirectResponse(url='/docs')
@app.get("/train")
async def train():
    try:
        os.system("python main.py")
        return Response('Training completed successfully.')
    except Exception as e:
        return Response(f'Error occurred during training: {str(e)}')
@app.post("/predict")
async def predict_route(
    text: str = Form(None),
    file: UploadFile = None
):
    try:
        if file:
            pdf_text = extract_text_from_pdf(file)
            input_text = pdf_text
        elif text:
            input_text = text
        else:
            return Response("Please provide either text input or a PDF file.", status_code=400)
        obj = PredictionPipeline()
        result = obj.predict(input_text)
        return {"summary": result}

    except Exception as e:
        return {"error": str(e)}
def extract_text_from_pdf(uploaded_file):
    pdf_text = ""
    with fitz.open(stream=uploaded_file.file.read(), filetype="pdf") as doc:
        for page in doc:
            pdf_text += page.get_text()
    return pdf_text

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)