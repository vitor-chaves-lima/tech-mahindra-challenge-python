import jwt
import datetime
from datetime import datetime, timedelta, timezone

ACCESS_TOKEN_SECRET = "TEST!@#access"
REFRESH_TOKEN_SECRET = "TEST!@#refresh"


def create_access_token(expires_delta_minutes=15):
    expires_delta = timedelta(minutes=expires_delta_minutes)
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode = {"exp": expire}
    encoded_jwt = jwt.encode(to_encode, ACCESS_TOKEN_SECRET, algorithm="HS256")
    return encoded_jwt


def create_refresh_token(data):
    expires_delta = timedelta(days=1)
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, REFRESH_TOKEN_SECRET, algorithm="HS256")
    return encoded_jwt