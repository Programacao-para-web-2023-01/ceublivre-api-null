from apis.correios import Correios
from fastapi import APIRouter, Depends, HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from database import get_db


router = APIRouter()

@cbv(router)
class CorreiosApi:
    session: Session = Depends(get_db)

    @router.get("/correios", response_model=Correios.response)
    def list_students(self, limit: int = 10, offset: int = 0):
        response = {"limit": limit, "offset": offset, "data": Correios.response}

        return response
