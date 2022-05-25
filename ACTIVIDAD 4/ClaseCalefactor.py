
class Calefactor:
    __marca = ""
    __modelo = ""

    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo


    def __repr__(self): #obtener estado del objeto
        return repr(("Modelo: "+self.__marca, "Marca: "+self.__modelo))


