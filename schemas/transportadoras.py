from pydantic import BaseModel
import datetime

class CreateTransportadora(BaseModel):
    nome_transportadora: str
    tele_transportadora: str