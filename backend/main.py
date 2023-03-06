# std
import time

# 3rd
import uvicorn
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Request, UploadFile

# local
import services
from utils import Response

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/upload_files", response_class=HTMLResponse)
def get_upload_form(request: Request):
    """
    HTML page for file uploading
    """
    return templates.TemplateResponse("upload_form.html", {"request": request})


@app.post("/upload_files")
async def upload(files: list[UploadFile]):
    """
    Method for uploading files to S3 Bucket
    """

    if services.validate_files(files):
        services.upload_files(files)
    return Response(detail="Files uploaded successfully!")


if __name__ == "__main__":
    uvicorn.run(app="main:app", port=8081, reload=True)
