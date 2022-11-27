from fastapi import APIRouter, Depends, Request
from database import get_db
from tags.user.schemas import User
from sqlalchemy.orm import Session
from dependencies import get_current_user
from tags.surveys.schema import SurveyInput, SurveyOutput
from tags.surveys.helper import create_survey, get_all_survey, get_survey_by_user
from typing import List

survey_route = APIRouter(
    prefix="/api/v1/survey",
    tags=["Surveys"]
)

@survey_route.post("/create", summary="create survey", response_model=SurveyOutput)
def create_surveys(survey: SurveyInput, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    new_survey = create_survey(db, survey, user)
    return {
        "title": new_survey.title,
        "description": new_survey.description,
        "id": new_survey.id,
        "user_id": new_survey.user_id
    }

@survey_route.get("/all", summary="get all surveys", response_model=List[SurveyOutput])
def get_all_surveys(db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    survey_list = get_all_survey(db)
    response = []
    for survey_obj in survey_list:
        response.append({
            "title": survey_obj.title,
            "description": survey_obj.description,
            "id": survey_obj.id,
            "user_id": survey_obj.user_id
        })

    return response

@survey_route.get("/{user_id}", summary="get all surveys of a user", response_model=List[SurveyOutput])
def get_all_surveys_of_user(user_id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    survey_list = get_survey_by_user(db,user_id)
    response = []
    for survey_obj in survey_list:
        response.append({
            "title": survey_obj.title,
            "description": survey_obj.description,
            "id": survey_obj.id,
            "user_id": survey_obj.user_id
        })

    return response
