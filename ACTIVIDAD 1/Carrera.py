
class Carrera:
    __codigo = int
    __nombre = ""
    __fechaini = ""
    __duracion = ""
    __titulo = ""


    def __init__(self, cod, name, fecha, dura, tit):
        self.__codigo = int(cod)
        self.__nombre = name
        self.__fechaini = fecha
        self.__duracion = dura
        self.__titulo = tit


    def getnomcarre(self):
        return self.__nombre

    def getduracarre(self):
        return self.__duracion

    def getcodcarre(self):
        return self.__codigo
