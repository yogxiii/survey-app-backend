from fastapi import APIRouter, Depends
from database import get_db
from tags.user.schemas import User
from sqlalchemy.orm import Session
from dependencies import get_current_user
from tags.answers.schemas import AnswerInput, AnswerOutput
from tags.answers.helper import add_questions_to_survey, get_survey_with_answer
from typing import List

answer_route = APIRouter(
    prefix="/api/v1/answers",
    tags=["Answers"]
)

@answer_route.post("/add", summary="add answer to questions")
def add_question(answer: AnswerInput, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    answers = add_questions_to_survey(db, answer)
    return {
        "details" : "success"
    }

@answer_route.get("/survey-answers/{survey_id}", summary="survey with answer")
def get_survey_answer(survey_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    obj_list = get_survey_with_answer(db, survey_id)
    response = []
    for obj in obj_list:
        response.append({
            "survey_id": obj.survey_id,
            "question_id": obj.question_id,
            "question": obj.description,
            "answer": obj.answer,
            "user_id": obj.user_id
        })

    return response





