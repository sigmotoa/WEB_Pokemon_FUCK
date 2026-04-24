import os
from pathlib import Path
import shutil
from fastapi import UploadFile, File, HTTPException

IMG_DIR = Path("files/img")

def save_img(file: UploadFile):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type")

    IMG_DIR.mkdir(parents=True, exist_ok=True)
    destination = IMG_DIR /file.filename

    with destination.open("wb") as stores:
        shutil.copyfileobj(file.file, stores)

    return destination






