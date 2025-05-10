from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from db.crud.user import create_user, get_user_by_username
from api.dependencies.db import get_db
from db.models.user import User as UserModel

from db.schemas.user import UserCreate
from services.auth import authenticate_user, get_password_hash
from services.jwt import create_access_token


router = APIRouter(prefix="/users")


@router.post("/register")
async def register_user(user_in: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_username(db, user_in.username)

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed_password = get_password_hash(user_in.password)
    new_user = UserModel(username=user_in.username, hashed_password=hashed_password)

    return create_user(db, new_user)


@router.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if user is None:
        raise HTTPException(status_code=401, detail="Incorrect username or password")

    token = create_access_token(data={"sub": user.username})

    return {"access_token": token, "token_type": "bearer"}


# @router.get("/test")
# async def test(db: Session = Depends(get_db)):
#     user = db.query(UserModel).filter(UserModel.id == 3).first()
#     return {"user": user, "cards": user.cards}
