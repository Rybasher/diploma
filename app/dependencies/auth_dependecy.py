from fastapi import Depends

from app.database.models.users import User
from app.services.auth import AuthService
from app.utils.session import UserSessionService
from sqlalchemy.orm import Session
from app.database.session import get_db


def get_auth_dependency(db: Session = Depends(get_db),
                        user_session_service: UserSessionService = Depends(UserSessionService)):
    return AuthService(db=db, user_session_service=user_session_service, model=User)
