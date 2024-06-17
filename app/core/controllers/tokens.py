import jwt
import datetime
from datetime import datetime, timedelta, timezone
from core.exceptions import ExpiredRefreshTokenException, InvalidRefreshTokenException

ACCESS_TOKEN_SECRET = "TEST!@#access"
REFRESH_TOKEN_SECRET = "TEST!@#refresh"


def create_access_token(expires_delta_minutes=15):
    expires_delta = timedelta(minutes=expires_delta_minutes)
    expire = (datetime.now(timezone.utc) + expires_delta).timestamp()
    to_encode = {"exp": expire}
    encoded_jwt = jwt.encode(to_encode, ACCESS_TOKEN_SECRET, algorithm="HS256")
    return encoded_jwt


def create_refresh_token(data):
    expires_delta = timedelta(days=1)
    expire = (datetime.now(timezone.utc) + expires_delta).timestamp()
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, REFRESH_TOKEN_SECRET, algorithm="HS256")
    return encoded_jwt


def validate_refresh_token(refresh_token: str) -> bool:
    try:
        decoded_token = jwt.decode(refresh_token, REFRESH_TOKEN_SECRET, algorithms=["HS256"])

        now = datetime.now(timezone.utc)
        exp = datetime.fromtimestamp(decoded_token["exp"], tz=timezone.utc)

        if now > exp:
            return False

        return True

    except jwt.ExpiredSignatureError:
        raise ExpiredRefreshTokenException()
    except jwt.InvalidTokenError:
        raise InvalidRefreshTokenException()