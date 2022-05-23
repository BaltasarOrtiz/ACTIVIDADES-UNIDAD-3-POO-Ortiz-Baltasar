
class Equipo:
    __nombre = ""
    __ciudad = ""


    def __init__(self, nom, ciu):
        self.__nombre = nom
        self.__ciudad = ciu


    def getnombre(self):
        return self.__nombre

    def getciudad(self):
        return self.__ciudad

    def getdni(self):
        return self.__nombre
