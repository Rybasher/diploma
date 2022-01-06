from fastapi import HTTPException, status


class BaseException(HTTPException):
    """
    Base exception
    """
    def __init__(self, message,  status_code=status.HTTP_400_BAD_REQUEST, exc=None):
        super(BaseException, self)
        self.detail = message
        self.status_code = status_code
        self.exc = exc


class TextNotFound(HTTPException):
    def __init__(self, text_id: str):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=f"Text with id {text_id} not found")


class AuthError(HTTPException):

    def __init__(self, details: str):
        super().__init__(status_code=status.HTTP_401_UNAUTHORIZED,
                         detail=details)


def handle_http_exception(message, exc=None):
    raise BaseException(message=message, exc=exc)


def handle_auth_exception(message,  status_code=status.HTTP_401_UNAUTHORIZED, exc=None):
    raise BaseException(message=message, status_code=status_code, exc=exc)


def handle_internal_exception(message,  status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, exc=None):
    raise BaseException(message=message, status_code=status_code, exc=exc)


def handle_not_found_exception(message,  status_code=status.HTTP_404_NOT_FOUND, exc=None):
    raise BaseException(message=message, status_code=status_code, exc=exc)


def handle_already_exists_exception(message, status_code=status.HTTP_409_CONFLICT, exc=None):
    raise BaseException(message=message, status_code=status_code, exc=exc)
