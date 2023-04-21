from pydantic import BaseModel

class CreatePedido(BaseModel):
    nome_pedido: str
    cep_origem_pedido: str
    cep_destino_pedido: str
    peso_pedido: float
    valor_declarado_pedido: float
    expresso_pedido: bool
