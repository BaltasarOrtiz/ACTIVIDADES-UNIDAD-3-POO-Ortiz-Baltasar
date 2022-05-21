
class Flores:
    __numero = int
    __nombre = ""
    __color = ""
    __descripcion = ""


    def __init__(self, num, nom, col, desc):
        self.__numero = int(num)
        self.__nombre = nom
        self.__color = col
        self.__descripcion = desc


    def getnombre(self):
        return self.__nombre



