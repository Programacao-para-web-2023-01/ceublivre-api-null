from apis.correios import Correios
from fastapi import APIRouter
from fastapi_utils.cbv import cbv

router = APIRouter()

@cbv(router)
class CorreiosApi:

    @router.get("/correios")
    def list_students(self, peso: float, cep_origem: str, cep_destino:str, valor_declarado:str):

        response = {"Correios response": Correios(cep_origem, cep_destino, peso, valor_declarado).response()}

        return response
