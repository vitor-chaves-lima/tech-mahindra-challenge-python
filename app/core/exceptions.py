class EmailExistsException(Exception):
    def __init__(self, email: str):
        self.email = email


class EmailNotFoundException(Exception):
    def __init__(self, email: str):
        self.email = email


class PasswordLengthException(Exception):
    def __init__(self, password_length: int):
        self.password_length = password_length


class InvalidPasswordConfirmException(Exception):
    ...


class InvalidCredentialsException(Exception):
    ...


class ExpiredRefreshTokenException(Exception):
    ...


class InvalidRefreshTokenException(Exception):
    ...