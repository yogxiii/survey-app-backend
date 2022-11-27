from pydantic import BaseModel

class SurveyInput(BaseModel):
    title: str
    description: str

class SurveyOutput(SurveyInput):
    id: int
    user_id: int


