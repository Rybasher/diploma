import re
from pydantic import BaseModel, EmailStr, constr, validator, root_validator
from faker import Faker

fake = Faker()

password_regular = re.compile(r'(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$')


class SessionResponse(BaseModel):
    session_id: str


class SignUpUser(BaseModel):
    username: constr(max_length=80, strip_whitespace=True)
    email: EmailStr
    password: str

    @validator("password", pre=True)
    def validate_password(cls, value):
        if not re.fullmatch(password_regular, value):
            raise ValueError(
                'Password must contain 8 characters, at least one'
                'uppercase and one lowercase letter, one number and one special character')
        return value

    class Config:
        schema_extra = {
            "example": {
                "username": fake.name(),
                "email": fake.email(),
                "password": fake.password(),
                }
            }


class SignInUser(BaseModel):
    email: EmailStr
    password: str

    @validator("password", pre=True)
    def validate_password(cls, value):
        if not value:
            raise ValueError('password required')
        return value

    class Config:
        schema_extra = {
            "example": {
                "email": "useremail@gmail.com",
                "password": "testpassword123"
            },
        }


# class RemindPassword(BaseModel):
#     email: EmailStr
#
#     class Config:
#         schema_extra = {
#             "example": {
#                 "email": "useremail@gmail.com",
#             },
#         }
#
#
# class ResetPasswordConfirm(BaseModel):
#     new_password1: str
#     new_password2: str
#
#     @root_validator
#     def passwords_match(cls, values):
#         if not re.fullmatch(password_regular, values['new_password1']):
#             raise ValueError(
#                 'Password must contain 8 characters, at least one'
#                 'uppercase and one lowercase letter, one number and one special character')
#         if values['new_password1'] != values['new_password2']:
#             raise ValueError('new password and new password confirm do not match')
#         return values
#
#     class Config:
#         schema_extra = {
#             "example": {
#                 "new_password1": "New password",
#                 "new_password2": "Confirm new password"
#             },
#         }
#
#
# class ResetPasswordConfirmSession(ResetPasswordConfirm):
#     current_password: str
#
#     class Config:
#         schema_extra = {
#             "example": {
#                 "current_password": "Your current password",
#                 "new_password1": "New password",
#                 "new_password2": "Confirm new password"
#             },
#         }
