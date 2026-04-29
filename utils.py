import os
from supabase import create_client, Client
from dotenv import load_dotenv
from pathlib import Path
import shutil
from fastapi import UploadFile, File, HTTPException

load_dotenv()


IMG_DIR = Path("files/img")
SUPABASE_BUCKET = os.getenv("SUPABASE_BUCKET")

def save_img_local(file: UploadFile):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type")

    IMG_DIR.mkdir(parents=True, exist_ok=True)
    destination = IMG_DIR /file.filename

    with destination.open("wb") as stores:
        shutil.copyfileobj(file.file, stores)

    return destination


##SUPABASE Begins here
def supabase_client():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        raise RuntimeError("No credentials provided")
    return create_client(url, key)



def save_img_remote(file: UploadFile):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Invalid file type")

    contents = file.file.read()
    path = file.filename

    client = supabase_client()

    response = client.storage.from_(SUPABASE_BUCKET).upload(
        path=path,
        file=contents,
        file_options={"content-type":file.content_type},
    )
    public_url_bucket = client.storage.from_(SUPABASE_BUCKET).get_public_url(path)
    return public_url_bucket



