from sqlalchemy.orm import Session
from tags.surveys.schema import SurveyInput, SurveyOutput
from tags.user.schemas import User
from models.all import Surveys
from fastapi.exceptions import HTTPException
from sqlalchemy import exc

def get_survey(db: Session, title: str):
    return db.query(Surveys).filter(Surveys.title == title).first()

def create_survey(db: Session, survey_data: SurveyInput, user: User):
    if get_survey(db, survey_data.title):
        raise HTTPException(status_code=403, detail="Survey already exist with same title")
    survey_obj = Surveys(
        title=survey_data.title,
        description=survey_data.description,
        user_id=user.id
    )

    try:
        db.add(survey_obj)
        db.commit()
        db.refresh(survey_obj)
    except exc.SQLAlchemyError:
        raise ValueError("Encountered general SQLAlchemyError")
    return survey_obj

def get_all_survey(db: Session):
    return db.query(Surveys).all()

def get_survey_by_user(db: Session, user_id: int):
    return db.query(Surveys).filter(Surveys.user_id == user_id).all()


