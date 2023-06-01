from deta import Deta
from os import getenv
from datetime import datetime, timedelta
from database.tbPedido import TbPedido
from apis_fake.localizacao import Localizacao

table = "tbEtapasEntrega"

class TbEtapasEntrega:
    def __init__(
        self,
        id_etapa_entrega: str,
        id_pedido: str,
        rastreamento_pedido: str,
        etapas_entrega: list
    ) -> None:
        self.id_etapa_entrega = id_etapa_entrega
        self.id_pedido = id_pedido
        self.rastreamento_pedido = rastreamento_pedido
        self.etapas_entrega = etapas_entrega


    def dict(self):
        return {
            "id_etapa_entrega": self.id_etapa_entrega,
            "id_pedido": self.id_pedido,
            "rastreamento_pedido": self.rastreamento_pedido,
            "etapas_entrega": self.etapas_entrega
        }


    @classmethod
    def create(
        cls,
        id_pedido: str,
        rastreamento_pedido: str
        # etapas_entrega: list
    ) -> None:
        # if (
        #     len(etapas_entrega) == 0 or
        #     any(
        #         type(x) != dict or
        #         "datahora" not in x or
        #         "local" not in x or
        #         "status" not in x
        #         for x in etapas_entrega
        #     )
        # ):
        #     raise Exception("Invalid etapas_entrega")

        dias = TbPedido.get(id_pedido = id_pedido).prazo_entrega_pedido
        local = Localizacao.gerar()
        etapas_entrega = [
            {
                "datahora": str(datetime.now() + timedelta(days=i)),
                "local": f"{local.lat}, {local.lon}"
            } for i in range(dias)
        ]

        deta = Deta(getenv("DETA_PROJECT_KEY"))
        db = deta.Base(table)

        ret = db.put({
            "id_pedido": id_pedido,
            "rastreamento_pedido": rastreamento_pedido,
            "etapas_entrega": etapas_entrega
        })

        if (type(ret) != dict):
            raise Exception("Error in create")

        cl = cls(
            ret["key"], # id_etapa_entrega
            id_pedido,
            rastreamento_pedido,
            etapas_entrega
        )

        return cl


    @classmethod
    def get(
        cls,
        id_etapa_entrega: str | None = None,
        id_pedido: str | None = None,
        rastreamento_pedido: str | None = None
    ) -> None:
        deta = Deta(getenv("DETA_PROJECT_KEY"))
        db = deta.Base(table)

        ret = None
        if (id_etapa_entrega != None):
            ret = db.get(id_etapa_entrega)
        elif (id_pedido != None):
            ret = db.get(id_pedido)
        elif (rastreamento_pedido != None):
            ret = db.fetch({"rastreamento_pedido": rastreamento_pedido}).items[0]
        else:
            return None

        if (type(ret) != dict):
            return None

        cl = cls(
            ret["key"], # id_etapa_entrega
            ret["id_pedido"],
            ret["rastreamento_pedido"],
            ret["etapas_entrega"]
        )

        return cl


    @classmethod
    def update(
        cls,
        id_etapa_entrega: str,
        id_pedido: str | None = None,
        rastreamento_pedido: str | None = None,
        etapas_entrega: list | None = None
    ) -> None:
        eta = cls.get(id_etapa_entrega=id_etapa_entrega)

        deta = Deta(getenv("DETA_PROJECT_KEY"))
        db = deta.Base(table)

        db.update(key=id_etapa_entrega, updates={
            "id_pedido": id_pedido or eta.id_pedido,
            "rastreamento_pedido": rastreamento_pedido or eta.rastreamento_pedido,
            "etapas_entrega": etapas_entrega or eta.etapas_entrega
        })

        return cls.get(id_etapa_entrega=id_etapa_entrega)


    @classmethod
    def delete(cls, id_etapa_entrega: str) -> None:
        deta = Deta(getenv("DETA_PROJECT_KEY"))
        db = deta.Base(table)

        db.delete(id_etapa_entrega)

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
