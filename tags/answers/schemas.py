from pydantic import BaseModel
from typing import List

class Answers(BaseModel):
    question_id: int
    answer: bool
    user_id: int

class AnswerOutputBase(Answers):
    id: int

class AnswerInput(Answers):
    answers: List[Answers]

class AnswerOutput(BaseModel):
    answers: List[AnswerOutputBase]