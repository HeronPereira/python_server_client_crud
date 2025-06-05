from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from config import settings, EXPIRE_DELTA
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

bearer_scheme = HTTPBearer()

def create_token(username: str):
    expire_timeout = datetime.now(timezone.utc) + timedelta(minutes=EXPIRE_DELTA)
    payload = {
        "sub": username,
        "exp": expire_timeout
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return token


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        subject = payload.get("sub")
        if subject is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return subject
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Token inválido ou expirado",
                            headers={"WWW-Authenticate": "Bearer"})