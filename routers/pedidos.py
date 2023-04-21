from fastapi import APIRouter, HTTPException
from fastapi_utils.cbv import cbv
from schemas.post_pedido import CreatePedido
from database.tbPedido import TbPedido
from database.tbEtapasEntrega import TbEtapasEntrega
from apis.correios import Correios

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
        

    @router.post("/create")
    def post_pedido(self, pedido: CreatePedido):
        correios = Correios(
            cep_origem=pedido.cep_origem_pedido, 
            cep_destino=pedido.cep_destino_pedido, 
            peso=pedido.peso_pedido,
            valor_declarado=pedido.valor_declarado_pedido
        )
        
        if pedido.expresso_pedido:
            correios = correios.get_express_delivery_info()
        else:
            correios = correios.response()

        if correios.get("error") != None:
            raise HTTPException(503, correios.get("msg_error"))

        res = TbPedido.create(
            rastreamento_pedido = "a definir",
            nome_pedido = pedido.nome_pedido,
            cep_origem_pedido = pedido.cep_origem_pedido,
            cep_destino_pedido = pedido.cep_destino_pedido,
            peso_pedido = pedido.peso_pedido,
            valor_declarado_pedido = pedido.valor_declarado_pedido,
            expresso_pedido = pedido.expresso_pedido,
            valor_envio_pedido = correios.get("valor"),
            prazo_entrega_pedido = correios.get("prazo_entrega"),
            tem_entrega_domiciliar_pedido = correios.get("entrega_domiciliar"),
            tem_entrega_sabado = correios.get("entrega_sabado"),
            status_pedido = "Separado para envio"
        )
        TbEtapasEntrega.create(res.id_pedido, res.rastreamento_pedido)
        return res.dict()


    @router.get("/code/{codigo_rastreamento}")
    def get_pedido_by_code(self, codigo_rastreamento: str):

        res = TbPedido.get(rastreamento_pedido=codigo_rastreamento)
        if res:
            return res
        else:    
            raise HTTPException(status_code=404, detail="Pedido not found")
        
    @router.delete("/{id}")
    def delete_pedido_by_id(self, id: str):
        ped = TbPedido.get(id_pedido=id)
        ped.delete(id_pedido=id)
        return ped.dict()