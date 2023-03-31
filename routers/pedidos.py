from database.tbPedido import TbPedido
from fastapi import APIRouter
from fastapi_utils.cbv import cbv

router = APIRouter()

@cbv(router)
class CorreiosApi:

    @router.get("/pedidos")
    def get_pedidos(self):
        return TbPedido.list()

    
    @router.get("/pedido/:id")
    def get_pedido_by_id(self, id: str):
        
        res = TbPedido.get(id_pedido=id)

        return res
    

    @router.get("/pedido/:codigo_rastreamento")
    def get_pedido_by_rastreamento(self, codigo_rastreamento: str):
        
        res = TbPedido.get(rastreamento_pedido=codigo_rastreamento)

        return res
    

    @router.post("/pedido")
    def get_pedido_by_id(self, id: str):
        
        res = TbPedido.get(id_pedido=id)

        return res
