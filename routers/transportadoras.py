from database.tbPedido import TbPedido
from fastapi import APIRouter, HTTPException
from fastapi_utils.cbv import cbv

router = APIRouter()

@cbv(router)
class Transportadoras:

    @router.get("/pedido_express")
    def get_pedidos_expressos(self):
        result = TbPedido.list()
        result = [x for x in result if x['expresso_pedido'] == True]
        return result
    
    @router.get("/pedido_normal")
    def get_pedidos_normal(self):
        result = TbPedido.list()
        result = [x for x in result if x['expresso_pedido'] == False]
        return result

    @router.get("/status_pedido/{id}")
    def get_status_pedido_by_id(self, id: str):
        result = TbPedido.get(id_pedido=id)
        if result:
            return result.status_pedido
            # result.localizacao, result.datahora_registro
        else:    
            raise HTTPException(status_code=404, detail="Pedido not found")