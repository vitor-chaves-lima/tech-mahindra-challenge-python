from core.db.schemas import UserRole


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


class InvalidUserRoleException(Exception):
    def __init__(self, expected_role: UserRole, found_role: UserRole):
        self.expected_role = expected_role
        self.found_role = found_role
