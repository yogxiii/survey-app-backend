from sqlalchemy.orm import Session
from tags.user import schemas
from models.all import User
from passlib.context import CryptContext
from sqlalchemy import exc
from fastapi.exceptions import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user(db: Session, user_name: str):
    return db.query(User).filter(User.user_name == user_name).first()

def authenticate_user(db: Session, username: str, password: str):
    db_user = get_user(db, username)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    if not verify_password(password, db_user.password):
        raise HTTPException(status_code=401, detail="Wrong password")
    return db_user

def create_user(db: Session, user: schemas.UserCreate):
    if get_user(db, user.user_name):
        raise HTTPException(status_code=403, detail="User already exist, Please signup")

    password = get_password_hash(user.password)
    user_name = user.user_name
    db_user = User(
        user_name=user_name,
        password=password
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except exc.SQLAlchemyError:
        raise ValueError("Encountered general SQLAlchemyError")
    return db_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

