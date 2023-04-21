from database.tbPedido import TbPedido
from fastapi import APIRouter, HTTPException
from fastapi_utils.cbv import cbv

router = APIRouter()

@cbv(router)
class Transportadoras:

    @router.get("/entregas/tipo/{tipo}")
    def get_pedidos(self, tipo: int):
        if tipo not in [1, 2]:
            raise HTTPException(status_code=404, detail="Shipping type not found.")
        return TbPedido.search({'expresso_pedido': tipo == 2})

    @router.get("/status_pedido/{id}")
    def get_status_pedido_by_id(self, id: str):
        result = TbPedido.get(id_pedido=id)
        if result:
            return {"status_pedido": result.status_pedido}
        raise HTTPException(status_code=404, detail="Pedido not found")
