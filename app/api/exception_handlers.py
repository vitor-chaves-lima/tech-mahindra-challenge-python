from fastapi import Request, status
from fastapi.responses import JSONResponse

from core.exceptions import EmailExistsException, PasswordLengthException, InvalidPasswordConfirmException


async def email_exists_exception_handler(_: Request, exc: EmailExistsException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "message": f"Email already registered: {exc.email}",
            "error": EmailExistsException.__name__
        },
    )


async def password_length_exception_handler(_: Request, exc: PasswordLengthException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "message": f"Invalid password length: {exc.password_length}, it should be 8 or greater",
            "error": PasswordLengthException.__name__
        },
    )


async def invalid_password_confirm_exception_handler(_: Request, exc: InvalidPasswordConfirmException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "message": f"Invalid password confirm",
            "error": InvalidPasswordConfirmException.__name__
        },
    )


def get_exception_handlers():
    return [
        (EmailExistsException, email_exists_exception_handler),
        (PasswordLengthException, password_length_exception_handler),
        (InvalidPasswordConfirmException, invalid_password_confirm_exception_handler)
    ]