from sqlalchemy.orm import Session

from db.models.user import User as UserModel


def get_user_by_username(db: Session, username: str):
    return db.query(UserModel).filter(UserModel.username == username).first()


def create_user(db: Session, db_user: UserModel) -> UserModel:
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
