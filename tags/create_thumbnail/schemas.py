from pydantic import BaseModel, AnyUrl

class ThumbnailInput(BaseModel):
    url: AnyUrl

class ThumbnailOutput(BaseModel):
    base64_encoded_image: str