from database.tbTransportadora import TbTransportadora
from database.tbPedido import TbPedido
from fastapi import APIRouter, HTTPException
from fastapi_utils.cbv import cbv
from schemas.transportadoras import CreateTransportadora

router = APIRouter()

@cbv(router)
class Transportadoras:

    @router.get("/")
    def get_transportadoras(self):
        result = TbTransportadora.list()
        if result:
            return result
        raise HTTPException(status_code=404, detail="Transportadora not found")

    @router.get("/type/{expresso}")
    def get_transportadora_by_type(self, expresso: bool):
        return TbPedido.search({'expresso_pedido': expresso})
    

    @router.get("/{id}")
    def get_transportadora_by_id(self, id: str):
        result = TbTransportadora.get(id_transportadora=id)
        if result:
            return {"transportadora": result}
        raise HTTPException(status_code=404, detail="Transportadora not found")

    @router.post("/create")
    def post_transportadora(self, transportadora: CreateTransportadora):
        res = TbTransportadora.create(
            nome_transportadora=transportadora.nome_transportadora,
            tele_transportadora=transportadora.tele_transportadora
        )
        return res.dict()
    
    @router.delete("/{id}")
    def delete_transportadora_by_id(self, id: str):
        res = TbTransportadora.get(id_transportadora=id)
        res.delete(id_transportadora=id)
        return res.dict()