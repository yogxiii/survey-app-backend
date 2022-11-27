from fastapi import APIRouter, Depends, Request
from tags.create_thumbnail.helper import create_thumbnail_from_image
from tags.create_thumbnail.schemas import ThumbnailInput, ThumbnailOutput

image_route = APIRouter(
    prefix="/api/v1",
    tags=["Images"]
)

@image_route.post("/create-thumbnail", summary="create thumbnail", response_model=ThumbnailOutput)
def create_thumbnail(data: ThumbnailInput):
   return {
    "base64_encoded_image": create_thumbnail_from_image(data)
   }


