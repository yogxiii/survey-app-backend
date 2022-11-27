from sqlalchemy.orm import Session
from tags.questions.schemas import QuestionInput
from tags.user.schemas import User
from models.all import Questions, Surveys
from fastapi.exceptions import HTTPException
from sqlalchemy import exc

def check_survey(db: Session, survey_id: int):
    return db.query(Surveys).filter(Surveys.id == survey_id).first()

def add_questions_to_survey(db: Session, question_data: QuestionInput):
    survey_id = question_data.survey_id
    if not check_survey(db, survey_id):
        raise HTTPException(status_code=404, detail="Survey not exist, First create survey")
    question_list = question_data.descriptions

    questions_obj = []
    for question in question_list:
        questions_obj.append(
            Questions(
                description=question.description,
                survey_id=survey_id
            )
        )

    try:
        db.add_all(questions_obj)
        db.commit()
    except exc.SQLAlchemyError:
        raise ValueError("Encountered general SQLAlchemyError")
    return questions_obj

def get_all_question_by_survey(db: Session, survey_id: int):
    question =  db.query(Questions).filter(Questions.survey_id == survey_id).all()
    if not question:
        raise HTTPException(status_code=404, detail="Survey not exist")
    return question



