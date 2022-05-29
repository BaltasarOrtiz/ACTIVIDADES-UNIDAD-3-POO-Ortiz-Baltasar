
class Aparatos:
    __marca = ""
    __model = ""
    __col = ""
    __pais = ""
    __precio = float


    def __init__(self, marca, model, col, pais, precio):
        self.__marca = marca
        self.__model = model
        self.__col = col
        self.__pais = pais
        self.__precio = float(precio)


    def toJSON(self):
        d = dict(
                __class__=self.__class__.__name__,
                __atributos__=dict(
                    marca=self.__marca,
                    modelo = self.__model,
                    color = self.__col,
                    paisdefabrica = self.__pais,
                    precio = self.__precio
                )
            )
        return d


    def getmarca(self):
        return self.__marca

    def getPreciobase(self):
        return self.__precio

    def getpais(self):
        return self.__pais
