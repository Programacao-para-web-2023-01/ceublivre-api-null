from database.tbPedido import TbPedido
from fastapi import APIRouter, HTTPException
from fastapi_utils.cbv import cbv

router = APIRouter()

@cbv(router)
class Transportadoras:

    @router.get("/entregas_por_tipo")
    def get_pedidos(self, entrega_expressa: bool = False):
        return TbPedido.search({'expresso_pedido': entrega_expressa})

    @router.get("/status_pedido/{id}")
    def get_status_pedido_by_id(self, id: str):
        result = TbPedido.get(id_pedido=id)
        if result:
            return result.status_pedido
        else:    
            raise HTTPException(status_code=404, detail="Pedido not found")
