from datetime import timedelta
from typing import Any

from fastapi import Depends, FastAPI, Request, Response, APIRouter
from fastapi_redis_session import deleteSession, getSession, getSessionId, getSessionStorage, setSession, SessionStorage
import random
from fastapi_redis_session.config import basicConfig
from pydantic import BaseModel

from app.core.config import AUTH_COOKIE_AGE
from app.utils.exceptions import handle_auth_exception

basicConfig(
    redisURL="redis://localhost:6379/1",
    sessionIdName="sessionId",
    sessionIdGenerator=lambda: str(random.randint(1000, 9999)),
    expireTime=timedelta(days=1),
    )


class SessionData(BaseModel):
    user_id: str


class UserSessionService:

    async def get_session(self, session: Any = Depends(getSession)):
        provided_session = session
        if not provided_session:
            return handle_auth_exception("Invalid session provided")
        return provided_session

    async def set_session(self, response: Response, session: Any, sessionStorage: SessionStorage) -> str:
        session_id = sessionStorage.genSessionId()
        sessionStorage[session_id] = session
        response.set_cookie("sessionId", session_id, httponly=True, secure=True, samesite="none", expires=AUTH_COOKIE_AGE)
        return session_id

    async def create_session(self, user_id: str, response: Response, session_storage: SessionStorage):
        session_data = SessionData(user_id=user_id)
        session = await self.set_session(response, session_data, session_storage)

        return session
