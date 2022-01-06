from fastapi import APIRouter
from fastapi import Depends
from fastapi import Response
from fastapi_redis_session import getSessionStorage, SessionStorage
from app.schemas.auth import SignUpUser, SessionResponse, SignInUser
from app.utils.responses_models import signin_responses, signup_responses
from app.dependencies.auth_dependecy import get_auth_dependency
from app.services.auth import AuthService

router = APIRouter(tags=["auth"])


@router.post("/signup", responses=signup_responses, response_model=SessionResponse)
async def signup(response: Response, payload: SignUpUser,
                 session_storage: SessionStorage = Depends(getSessionStorage),
                 auth_service: AuthService = Depends(get_auth_dependency)):
    return await auth_service.signup(user=payload, response=response,
                                     session_storage=session_storage)


@router.post("/signin", responses=signin_responses, response_model=SessionResponse)
async def sign_in(response: Response, payload: SignInUser,
                  session_storage: SessionStorage = Depends(getSessionStorage),
                  auth_service: AuthService = Depends(get_auth_dependency)):
    return await auth_service.sign_in(response=response, user=payload, session_storage=session_storage)
