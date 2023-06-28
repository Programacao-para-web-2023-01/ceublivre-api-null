from deta import Deta
from os import getenv
import datetime

table = "tbPedido"

class TbPedido:
    def __init__(
        self,
        id_pedido: str,
        rastreamento_pedido: str,
        nome_pedido: str,
        cep_origem_pedido: str,
        cep_destino_pedido: str,
        peso_pedido: float,
        valor_declarado_pedido: float,
        expresso_pedido: bool,
#        id_transportadora: str,
        valor_envio_pedido: float,
        prazo_entrega_pedido: int,
        tem_entrega_domiciliar_pedido: bool,
        tem_entrega_sabado: bool,
        status_pedido: str,
        datahora_criacao: str
    ) -> None:
        self.id_pedido = id_pedido
        self.rastreamento_pedido = rastreamento_pedido
        self.nome_pedido = nome_pedido
        self.cep_origem_pedido = cep_origem_pedido
        self.cep_destino_pedido = cep_destino_pedido
        self.peso_pedido = peso_pedido
        self.valor_declarado_pedido = valor_declarado_pedido
        self.expresso_pedido = expresso_pedido
        #self.id_transportadora #= id_transportadora
        self.valor_envio_pedido = valor_envio_pedido
        self.prazo_entrega_pedido = prazo_entrega_pedido
        self.tem_entrega_domiciliar_pedido = tem_entrega_domiciliar_pedido
        self.tem_entrega_sabado = tem_entrega_sabado
        self.status_pedido = status_pedido
        self.datahora_criacao = datahora_criacao


    def dict(self):
        return {
            "id_pedido": self.id_pedido,
            "rastreamento_pedido": self.rastreamento_pedido,
            "nome_pedido": self.nome_pedido,
            "cep_origem_pedido": self.cep_origem_pedido,
            "cep_destino_pedido": self.cep_destino_pedido,
            "peso_pedido": self.peso_pedido,
            "valor_declarado_pedido": self.valor_declarado_pedido,
            "expresso_pedido": self.expresso_pedido,
            #"id_transportadora": #self.id_transportadora,
            "valor_envio_pedido": self.valor_envio_pedido,
            "prazo_entrega_pedido": self.prazo_entrega_pedido,
            "tem_entrega_domiciliar_pedido": self.tem_entrega_domiciliar_pedido,
            "tem_entrega_sabado": self.tem_entrega_sabado,
            "status_pedido": self.status_pedido,
            "datahora_criacao": self.datahora_criacao
        }


    @classmethod
    def create(
        cls,
        rastreamento_pedido: str,
        nome_pedido: str,
        cep_origem_pedido: str,
        cep_destino_pedido: str,
        peso_pedido: float,
        valor_declarado_pedido: float,
        expresso_pedido: bool,
#        id_transportadora: str,
        valor_envio_pedido: float,
        prazo_entrega_pedido: int,
        tem_entrega_domiciliar_pedido: bool,
        tem_entrega_sabado: bool,
        status_pedido: str
    ) -> None:
        deta = Deta(getenv("DETA_PROJECT_KEY"))
        db = deta.Base(table)

        datahora_criacao = str(datetime.datetime.now())
        ret = db.put({
            "rastreamento_pedido": rastreamento_pedido,
            "nome_pedido": nome_pedido,
            "cep_origem_pedido": cep_origem_pedido,
            "cep_destino_pedido": cep_destino_pedido,
            "peso_pedido": peso_pedido,
            "valor_declarado_pedido": valor_declarado_pedido,
            "expresso_pedido": expresso_pedido,
            #"id_transportadora#": id_transportadora,
            "valor_envio_pedido": valor_envio_pedido,
            "prazo_entrega_pedido": prazo_entrega_pedido,
            "tem_entrega_domiciliar_pedido": tem_entrega_domiciliar_pedido,
            "tem_entrega_sabado": tem_entrega_sabado,
            "status_pedido": status_pedido,
            "datahora_criacao": datahora_criacao
        })

        if (type(ret) != dict):
            raise Exception("Error in create")

        cl = cls(
            ret["key"], # id_pedido
            rastreamento_pedido,
            nome_pedido,
            cep_origem_pedido,
            cep_destino_pedido,
            peso_pedido,
            valor_declarado_pedido,
            expresso_pedido,
#            id_transportadora,
            valor_envio_pedido,
            prazo_entrega_pedido,
            tem_entrega_domiciliar_pedido,
            tem_entrega_sabado,
            status_pedido,
            datahora_criacao
        )

        return cl


    @classmethod
    def get(
        cls,
        id_pedido: str | None = None,
        rastreamento_pedido: str | None = None
    ) -> None:
        deta = Deta(getenv("DETA_PROJECT_KEY"))
        db = deta.Base(table)

        ret = None
        if (id_pedido != None):
            ret = db.get(id_pedido)
        elif (rastreamento_pedido != None):
            try:
                ret = db.fetch({"rastreamento_pedido": rastreamento_pedido}).items[0]
            except:
                ret = None 
        else:
            return None

        if (type(ret) != dict):
            return None

        cl = cls(
            ret["key"], # id_pedido
            ret["rastreamento_pedido"],
            ret["nome_pedido"],
            ret["cep_origem_pedido"],
            ret["cep_destino_pedido"],
            ret["peso_pedido"],
            ret["valor_declarado_pedido"],
            ret["expresso_pedido"],
            #ret["id_transportadora"],
            ret["valor_envio_pedido"],
            ret["prazo_entrega_pedido"],
            ret["tem_entrega_domiciliar_pedido"],
            ret["tem_entrega_sabado"],
            ret["status_pedido"],
            ret["datahora_criacao"]
        )

        return cl


    @classmethod
    def update(
        cls,
        id_pedido: str,
        rastreamento_pedido: str | None = None,
        nome_pedido: str | None = None,
        cep_origem_pedido: str | None = None,
        cep_destino_pedido: str | None = None,
        peso_pedido: float | None = None,
        valor_declarado_pedido: float | None = None,
        expresso_pedido: bool | None = None,
#        id_transportadora: str | None = None,
        valor_envio_pedido: float | None = None,
        prazo_entrega_pedido: int | None = None,
        tem_entrega_domiciliar_pedido: bool | None = None,
        tem_entrega_sabado: bool | None = None,
        status_pedido: str | None = None,
        datahora_criacao: datetime.datetime | None = None
    ) -> None:
        pedido = cls.get(id_pedido=id_pedido)

        deta = Deta(getenv("DETA_PROJECT_KEY"))
        db = deta.Base(table)

        db.update(key=id_pedido, updates={
            "rastreamento_pedido": rastreamento_pedido or pedido.rastreamento_pedido,
            "nome_pedido": nome_pedido or pedido.nome_pedido,
            "cep_origem_pedido": cep_origem_pedido or pedido.cep_origem_pedido,
            "cep_destino_pedido": cep_destino_pedido or pedido.cep_destino_pedido,
            "peso_pedido": peso_pedido or pedido.peso_pedido,
            "valor_declarado_pedido": valor_declarado_pedido or pedido.valor_declarado_pedido,
            "expresso_pedido": expresso_pedido or pedido.expresso_pedido,
            #"id_transportadora#": id_transportadora or #pedido.id_transportadora,
            "valor_envio_pedido": valor_envio_pedido or pedido.valor_envio_pedido,
            "prazo_entrega_pedido": prazo_entrega_pedido or pedido.prazo_entrega_pedido,
            "tem_entrega_domiciliar_pedido": tem_entrega_domiciliar_pedido or pedido.tem_entrega_domiciliar_pedido,
            "tem_entrega_sabado": tem_entrega_sabado or pedido.tem_entrega_sabado,
            "status_pedido": status_pedido or pedido.status_pedido,
            "datahora_criacao": datahora_criacao or pedido.datahora_criacao
        })

        return cls.get(id_pedido=id_pedido)


    @classmethod
    def delete(cls, id_pedido: str) -> None:
        deta = Deta(getenv("DETA_PROJECT_KEY"))
        db = deta.Base(table)

        db.delete(id_pedido)

        return None


    @classmethod
    def list(cls, limit: int = 1000) -> list:
        deta = Deta(getenv("DETA_PROJECT_KEY"))
        db = deta.Base(table)

        ret = db.fetch(limit=limit).items

        if (type(ret) != list):
            raise Exception("Error in list")

        return ret


    @classmethod
    def search(cls, query: str, limit: int = 1000) -> list:
        deta = Deta(getenv("DETA_PROJECT_KEY"))
        db = deta.Base(table)

        ret = db.fetch(query=query, limit=limit).items

        if (type(ret) != list):
            raise Exception("Error in search")

        return ret
