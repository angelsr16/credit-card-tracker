from datetime import datetime, timedelta
from jose import JWTError, jwt
from core.config import settings


def create_access_token(data: dict):
    to_encode = data.copy()
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
