from fastapi import APIRouter, Depends
from database import get_db
from tags.user.schemas import User
from sqlalchemy.orm import Session
from dependencies import get_current_user
from tags.questions.schemas import QuestionInput, QuestionOutput
from tags.questions.helper import get_all_question_by_survey, add_questions_to_survey
from typing import List

question_route = APIRouter(
    prefix="/api/v1/questions",
    tags=["Questions"]
)

@question_route.post("/add", summary="add question to survey")
def add_question(questions: QuestionInput, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    questions = add_questions_to_survey(db, questions)
    return {
        "details" : "success"
    }

@question_route.get("/surveys/{survey_id}", summary="get all questions of a survey", response_model=QuestionOutput)
def get_all_surveys_of_user(survey_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    question_obj_list = get_all_question_by_survey(db,survey_id)
    question_list = []
    for question_obj in question_obj_list:
        question_list.append({
            "id": question_obj.id,
            "description": question_obj.description
        })

    return {
        "descriptions": question_list,
        "survey_id": survey_id
    }
