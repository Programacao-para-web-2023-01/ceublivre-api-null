from apis.correios import Correios
from fastapi import APIRouter
from fastapi_utils.cbv import cbv

router = APIRouter()

@cbv(router)
class CorreiosApi:

    @router.get("/")
    def get_frete(self, peso: float, cep_origem: str, cep_destino:str, valor_declarado:float, entrega_expressa: bool = False):

        res = Correios(cep_origem, cep_destino, peso, valor_declarado)
        if entrega_expressa:
            return res.get_express_delivery_info()

        return res.response()
