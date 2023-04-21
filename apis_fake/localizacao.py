from random import random

class Localizacao:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    @classmethod
    def gerar(cls):
        lat = ((random()*35.48) - 31.24)
        lon = ((random()*(-36)) - 35)

        return cls(lat, lon)
