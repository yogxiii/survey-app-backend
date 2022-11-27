from PIL import Image
import urllib.request
from tags.create_thumbnail.schemas import ThumbnailInput
from uuid import uuid4
from fastapi.exceptions import HTTPException
import base64

def create_thumbnail_from_image(data: ThumbnailInput):
    file_name = uuid4()
    try:
        urllib.request.urlretrieve(data.url, f"thumbnails/{file_name}.jpg")
    except:
        raise HTTPException(status_code=400, detail="Unable to pasre URL, please check image URL")
    image = Image.open(f"thumbnails/{file_name}.jpg")
    MAX_SIZE = (50, 50)
    image.thumbnail(MAX_SIZE)
    image.save(f"thumbnails/{file_name}.jpg")

    with open(f"thumbnails/{file_name}.jpg", "rb") as img_file:
        result_thumbnail = base64.b64encode(img_file.read())
    return result_thumbnail
