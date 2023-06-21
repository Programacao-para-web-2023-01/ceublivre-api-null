from deta import Deta
from os import getenv
from database.tbTransportadora import TbTransportadora

table = "tbTransportadora"

class TbTransportadora:
    def __init__(
        self,
        id_transportadora: str,
        nome_transportadora: str,
        tele_transportadora: str
    ) -> None:
        self.id_transportadora = id_transportadora
        self.nome_transportadora = nome_transportadora
        self.tele_transportadora = tele_transportadora


    def dict(self):
        return {
            "id_transportadora": self.id_transportadora,
            "nome_transportadora": self.nome_transportadora,
            "tele_transportadora": self.tele_transportadora
        }


    @classmethod
    def create(
        cls,
        id_transportadora: str,
        nome_transportadora: str,
        tele_transportadora: str
    ) -> None:

        deta = Deta(getenv("DETA_PROJECT_KEY"))
        db = deta.Base(table)

        ret = db.put({
            "id_transportadora": id_transportadora,
            "nome_transportadora": nome_transportadora,
            "tele_transportadora": tele_transportadora
        })

        if (type(ret) != dict):
            raise Exception("Error in create")

        cl = cls(
            ret["key"], # id_etapa_entrega
            id_transportadora,
            nome_transportadora,
            tele_transportadora
        )

        return cl


    @classmethod
    def get(
        cls,
        id_transportadora: str | None = None,
        nome_transportadora: str | None = None,
        tele_transportadora: str | None = None
    ) -> None:
        deta = Deta(getenv("DETA_PROJECT_KEY"))
        db = deta.Base(table)

        ret = None
        if (id_transportadora != None):
            ret = db.get(id_transportadora)
        elif (nome_transportadora != None):
            ret = db.fetch({"nome_transportadora": nome_transportadora}).items[0]
        elif (tele_transportadora != None):
            ret = db.fetch({"tele_transportadora": tele_transportadora}).items[0]
        else:
            return None

        if (type(ret) != dict):
            return None

        cl = cls(
            ret["key"],
            ret["id_transportadora"],
            ret["nome_transportadora"],
            ret["tele_transportadora"]
        )

        return cl


    @classmethod
    def update(
        cls,
        id_transportadora: str | None = None,
        nome_transportadora: str | None = None,
        tele_transportadora: str | None = None
    ) -> None:
        eta = cls.get(id_transportadora=id_transportadora)
        
        deta = Deta(getenv("DETA_PROJECT_KEY"))
        db = deta.Base(table)

        db.update(key=id_transportadora, updates={
            "id_transportadora": id_transportadora or eta.id_transportadora,
            "nome_transportadora": nome_transportadora or eta.nome_transportadora,
            "tele_transportadora": tele_transportadora or eta.tele_transportadora
        })

        return cls.get(id_transportadora=id_transportadora)


    @classmethod
    def delete(cls, id_transportadora: str) -> None:
        deta = Deta(getenv("DETA_PROJECT_KEY"))
        db = deta.Base(table)

        db.delete(id_transportadora)

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
