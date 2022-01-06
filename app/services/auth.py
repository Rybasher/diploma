from fastapi.encoders import jsonable_encoder
from fastapi_redis_session import SessionStorage

from app.database.db import Base
from app.schemas.auth import SessionResponse, SignUpUser, SignInUser
from app.utils.session import UserSessionService
from fastapi import Response
from sqlalchemy.orm import Session
from typing import TypeVar, Type

ModelType = TypeVar("ModelType", bound=Base)


class AuthService:
    def __init__(self, db: Session, user_session_service: UserSessionService, model: Type[ModelType]):
        self.user_session_service = user_session_service
        self.db = db
        self.model = model

    async def signup(self, user: SignUpUser, response: Response,
                     session_storage: SessionStorage) -> SessionResponse:
        obj_in_data = jsonable_encoder(user)
        new_user = self.model(**obj_in_data)  # type: ignore
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        session_id = await self.user_session_service.create_session(new_user.id, response, session_storage)
        return SessionResponse(session_id=session_id)

    async def sign_in(self, response: Response, user: SignInUser, session_storage: SessionStorage) -> SessionResponse:

        # return SessionResponse(session_id=session)
        return ""