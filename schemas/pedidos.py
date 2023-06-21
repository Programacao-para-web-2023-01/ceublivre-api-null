from pydantic import BaseModel
import datetime

class CreatePedido(BaseModel):
    nome_pedido: str
    cep_origem_pedido: str
    cep_destino_pedido: str
    peso_pedido: float
    valor_declarado_pedido: float
    expresso_pedido: bool

class UpdatePedido(BaseModel):
    rastreamento_pedido: str
    nome_pedido: str
    cep_origem_pedido: str
    cep_destino_pedido: str
    peso_pedido: float
    valor_declarado_pedido: float
    expresso_pedido: bool
    valor_envio_pedido: float
    prazo_entrega_pedido: int
    tem_entrega_domiciliar_pedido: bool
    tem_entrega_sabado: bool
    status_pedido: str
