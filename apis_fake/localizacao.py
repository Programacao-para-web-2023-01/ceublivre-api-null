from random import random
from datetime import datetime

class Localizacao:
    def __init__(self, lat, lon, data_hora):
        self.lat = lat
        self.lon = lon
        self.data_hora = data_hora

    @classmethod
    def gerar(cls):
        lat = ((random()*35.48) - 31.24)
        lon = ((random()*(-36)) - 35)
        data_hora = datetime.now()

        return cls(lat, lon, data_hora)
