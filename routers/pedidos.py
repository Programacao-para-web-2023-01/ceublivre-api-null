from database.tbPedido import TbPedido
from fastapi import APIRouter, HTTPException
from fastapi_utils.cbv import cbv

router = APIRouter()

@cbv(router)
class Pedidos:

    @router.get("/pedidos")
    def get_pedidos(self):
        return TbPedido.list()

    
    @router.get("/pedido_id/{id}")
    def get_pedido_by_id(self, id: str):


        res = TbPedido.get(id_pedido=id)
        if not(res):
            raise HTTPException(status_code=404, detail="Pedido not found")
        
        return res
    

    @router.get("/pedido_code/{codigo_rastreamento}")
    def get_pedido_by_code(self, codigo_rastreamento: str):

        res = TbPedido.get(rastreamento_pedido=codigo_rastreamento)
        
        return res
