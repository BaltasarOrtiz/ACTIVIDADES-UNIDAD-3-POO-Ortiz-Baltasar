from ClaseCalefactor import Calefactor


class CalefactorElectrico(Calefactor):
    __potencia = float

    def __init__(self, marca, modelo, potencia):
        self.__potencia = float(potencia)
        super().__init__(marca, modelo)

    '''
    def __repr__(self): #obtener estado del objeto
        return repr((super().__repr__(),self.__potencia))
    '''

    def getpotencia(self):
        return self.__potencia
