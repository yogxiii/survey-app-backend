from sqlalchemy.orm import Session
from tags.answers.schemas import AnswerInput
from tags.user.schemas import User
from models.all import Questions, Surveys, Answers
from fastapi.exceptions import HTTPException
from sqlalchemy import exc, text

def check_question(db: Session, question_id: int):
    return db.query(Questions).filter(Questions.id == question_id).first()

def add_questions_to_survey(db: Session, answer_data: AnswerInput):
    answer_obj = []
    answer_data = answer_data.answers
    for answer in answer_data:
        if not check_question(db, answer.question_id):
            raise HTTPException(status_code=404, detail="question not exist")
        answer_obj.append(
            Answers(
                question_id=answer.question_id,
                answer=answer.answer,
                user_id=answer.user_id
            )
        )

    try:
        db.add_all(answer_obj)
        db.commit()
    except exc.SQLAlchemyError:
        raise ValueError("Encountered general SQLAlchemyError")
    return answer_obj

def get_survey_with_answer(db: Session, survey_id: int):
    stmt = text(
        """
        SELECT s.id as survey_id, q.id as question_id, q.description as description, 
        a.answer as answer, a.user_id as user_id from surveys as s
        JOIN questions as q on s.id = q.survey_id
        JOIN answers as a on q.id = a.question_id
        WHERE s.id = :survey_id
        """
    )
    try:
        obj = db.execute(stmt, {"survey_id":survey_id})
    except exc.SQLAlchemyError:
        raise ValueError("Encountered general SQLAlchemyError")
    return obj



