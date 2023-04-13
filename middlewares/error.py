from fastapi import HTTPException, Request, Response

async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except HTTPException as e:
        return Response(e.detail or "Unknown", e.status_code)
