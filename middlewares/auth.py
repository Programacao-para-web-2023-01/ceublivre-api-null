from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware

from apis.auth import Auth

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        if (request.url.path in ("/", "/docs", "/redoc", "/openapi.json")):
            return await call_next(request)

        auth = Auth.validate(request.headers.get("Authorization"))

        if auth.error:
            raise HTTPException(status_code=auth.code or 401, detail=auth.detail or "Invalid token")
        auth_header = request.headers.get("Authorization")
        # if request.url.path not in ("/"):
        #     auth_header = request.headers.get("Authorization")
        #     if not auth_header:
        #         raise HTTPException(status_code=401, detail="Authorization header missing")

        #     token = auth_header.split("Bearer ")[1]
        #     if not token or token != "your_token":
        #         raise HTTPException(status_code=401, detail="Invalid token")

        response = await call_next(request)
        return response
