from fastapi import HTTPException

def verify_secret_key(secret_key: str):
    def dependency(authorization: str):
        if authorization != f"Bearer {secret_key}":
            raise HTTPException(status_code=401, detail="Unauthorized")
        return True
    return dependency
