from fastapi import APIRouter, Header, status, HTTPException, Depends
from tags.user import schemas
from sqlalchemy.orm import Session
from database import get_db
from tags.user.helper import create_user, authenticate_user
from fastapi.security import OAuth2PasswordRequestForm
from utils import create_access_token, create_refresh_token
from dependencies import get_current_user

user_router = APIRouter(
    prefix="/api",
    tags=["Users"]
)

@user_router.post("/v1/signup", summary="create new user", response_model=schemas.Token)
def user_signup(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Creating new user with user name and password and storing it into db
    """
    new_user = create_user(db=db, user=user_data)
    return {
        "access_token": create_access_token(new_user.user_name), 
        "refresh_token": create_refresh_token(new_user.user_name)
    }

@user_router.post("/v1/login", summary="login by username and password", response_model=schemas.Token)
def user_login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    """
    Creating new user with user name and password and storing it into db
    """
    db_user = authenticate_user(db, form_data.username, form_data.password)
    return {
        "access_token": create_access_token(db_user.user_name),
        "refresh_token": create_refresh_token(db_user.user_name),
    }

@user_router.get("/v1/user/me", summary="Get current user details", response_model=schemas.User)
def get_user(db: Session = Depends(get_db), user: schemas.User = Depends(get_current_user)):
    return user
