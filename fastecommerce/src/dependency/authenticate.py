from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

def authenticate(
    header: HTTPAuthorizationCredentials = Depends(security)
):
    token = header.credentials

    if not token:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    return token