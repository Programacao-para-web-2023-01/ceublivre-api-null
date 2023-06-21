from fastapi import APIRouter, HTTPException
from fastapi_utils.cbv import cbv
from schemas.pedidos import CreatePedido, UpdatePedido
from database.tbPedido import TbPedido
from database.tbEtapasEntrega import TbEtapasEntrega
from apis.correios import Correios
import random
import string

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
            valor_declarado=pedido.valor_declarado_pedido,
            id_transportadora=pedido.id_transportadora
        )
        characters = string.ascii_letters + string.digits
        
        if pedido.expresso_pedido:
            correios = correios.get_express_delivery_info()
        else:
            correios = correios.response()

        if correios.get("error") != None:
            raise HTTPException(503, correios.get("msg_error"))
        

        res = TbPedido.create(
            rastreamento_pedido = ''.join(random.choice(characters) for i in range(8)),
            nome_pedido = pedido.nome_pedido,
            cep_origem_pedido = pedido.cep_origem_pedido,
            cep_destino_pedido = pedido.cep_destino_pedido,
            peso_pedido = pedido.peso_pedido,
            valor_declarado_pedido = pedido.valor_declarado_pedido,
            expresso_pedido = pedido.expresso_pedido,
            id_transportadora = pedido.id_transportadora,
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
        
    @router.put("/{id}")
    def update_pedido_by_id(self, pedido:UpdatePedido, id: str):

        pedidoInfo = TbPedido.get(id_pedido=id)

        res = TbPedido.update(id_pedido=id,
            rastreamento_pedido=pedido.rastreamento_pedido,
            nome_pedido=pedido.nome_pedido,
            cep_origem_pedido=pedido.cep_origem_pedido,
            cep_destino_pedido=pedido.cep_destino_pedido,
            peso_pedido=pedido.peso_pedido,
            valor_declarado_pedido=pedido.valor_declarado_pedido,
            expresso_pedido=pedido.expresso_pedido,
            valor_envio_pedido=pedido.valor_envio_pedido,
            prazo_entrega_pedido=pedido.prazo_entrega_pedido,
            tem_entrega_domiciliar_pedido=pedido.tem_entrega_domiciliar_pedido,
            tem_entrega_sabado=pedido.tem_entrega_sabado,
            status_pedido=pedido.status_pedido,
            datahora_criacao=pedidoInfo.datahora_criacao
            )
        if res:
            return res
        else:    
            raise HTTPException(status_code=404, detail="Pedido not found")

    @router.delete("/{id}")
    def delete_pedido_by_id(self, id: str):
        ped = TbPedido.get(id_pedido=id)
        ped.delete(id_pedido=id)
        return ped.dict()