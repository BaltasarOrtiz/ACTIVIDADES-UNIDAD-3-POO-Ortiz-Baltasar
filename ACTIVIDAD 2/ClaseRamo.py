from ClaseFlores import Flores
from typing import Literal

class Ramo:
    __tamano = Literal["grande", "mediano", "chico"]
    __flor: list

    def __init__(self, tam: Literal["grande", "mediano", "chico"]):
        self.__tamano = tam
        self.__flor = []


    def getcantidaflores(self):
        return len(self.__flor)

    def agregarflor(self, flor):
        self.__flor.append(flor)

    def getlistaflores(self):
        return self.__flor

    def gettamano(self):
        return self.__tamano
