from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import declarative_mixin
from sqlalchemy.sql import func

@declarative_mixin
class BaseMixin:
    __abstract__=True
    id = Column(Integer, primary_key=True, index=True, unique=True, nullable=False, autoincrement=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())