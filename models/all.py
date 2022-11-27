from sqlalchemy import (
    Column,
    Boolean,
    String,
    Text,
    Integer,
    ForeignKey
)
from database import Base
from models.base import BaseMixin

class User(BaseMixin, Base):
    __tablename__ = "users"
    user_name = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    def __repr__(self) -> str:
        return f"{self.user_name}"

class Surveys(BaseMixin, Base):
    __tablename__ = "surveys"
    title = Column(String(200),unique=True, nullable=False)
    description = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    def __repr__(self) -> str:
        return f"{self.title}"

class Questions(BaseMixin, Base):
    __tablename__ = "questions"
    description = Column(Text, unique=True, nullable=False)
    survey_id = Column(Integer, ForeignKey("surveys.id"), nullable=False)

class Answers(BaseMixin, Base):
    __tablename__ = "answers"
    question_id = Column(Integer, ForeignKey("questions.id"), nullable=False)
    answer = Column(Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
