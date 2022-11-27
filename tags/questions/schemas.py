from pydantic import BaseModel
from typing import List

class Question(BaseModel):
    description: str

class QuestionOutputBase(Question):
    id: str

class QuestionInput(BaseModel):
    descriptions: List[Question]
    survey_id: int

class QuestionOutput(QuestionInput):
    descriptions: List[QuestionOutputBase]
    survey_id: int