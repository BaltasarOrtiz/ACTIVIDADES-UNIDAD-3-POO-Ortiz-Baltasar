from Carrera import Carrera

class Facultad:
    __codigo = int
    __nombre = ""
    __direccion = ""
    __localidad = ""
    __telefono = ""
    __carreras: list[Carrera]

    def __init__(self, cod, nom, direc, local, tel):
        self.__codigo = int(cod)
        self.__nombre = nom
        self.__direccion = direc
        self.__localidad = local
        self.__telefono = tel
        self.__carreras = []

    def agregarcarre(self, objeto):
        self.__carreras.append(objeto)

    def getcod(self):
        return self.__codigo

    def getnombre(self):
        return self.__nombre

    def getlocalidad(self):
        return self.__localidad

    #CARRERA
    def longitudcarre(self):
        return len(self.__carreras)

    def getnomcarre(self, pos):
         return self.__carreras[pos].getnomcarre()

    def getduracarre(self, pos):
        return self.__carreras[pos].getduracarre()

    def getcodcarre(self, pos):
        return self.__carreras[pos].getcodcarre()
