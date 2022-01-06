from sqlalchemy.orm import Session

from app.database.models.test import UserTest, Item
from app.schemas.test import *


def get_user(db: Session, user_id: int):
    return db.query(UserTest).filter(UserTest.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(UserTest).filter(UserTest.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(UserTest).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = UserTest(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: ItemCreate, user_id: int):
    db_item = Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
