from database.tbPedido import TbPedido
from fastapi import APIRouter, HTTPException
from fastapi_utils.cbv import cbv

router = APIRouter()

@cbv(router)
class Pedidos:

    @router.get("/pedidos")
    def get_pedidos(self):
        return TbPedido.list()

    
    @router.get("/pedido/{codigo}")
    def get_pedido_by_code(self, id: str = None, codigo_rastreamento: str = None):

        if not(codigo_rastreamento and id):
            raise HTTPException(status_code=404, detail="Pedido not found")
        elif(codigo_rastreamento):
            return TbPedido.get(rastreamento_pedido=codigo_rastreamento)
        
        return TbPedido.get(id_pedido=id)
