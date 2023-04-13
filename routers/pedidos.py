from database.tbPedido import TbPedido
from fastapi import APIRouter, HTTPException
from fastapi_utils.cbv import cbv

router = APIRouter()

@cbv(router)
class Pedidos:

    @router.get("/")
    def get_pedidos(self):
        return TbPedido.list()

    
    @router.get("/id/{id}")
    def get_pedido_by_id(self, id: str):


        res = TbPedido.get(id_pedido=id)
        if res:
            return res
        else:    
            raise HTTPException(status_code=404, detail="Pedido not found")
        
    

    @router.get("/code/{codigo_rastreamento}")
    def get_pedido_by_code(self, codigo_rastreamento: str):

        res = TbPedido.get(rastreamento_pedido=codigo_rastreamento)
        if res:
            return res
        else:    
            raise HTTPException(status_code=404, detail="Pedido not found")
        
