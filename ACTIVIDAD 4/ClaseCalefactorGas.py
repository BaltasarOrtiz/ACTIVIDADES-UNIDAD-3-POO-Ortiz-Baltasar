from ClaseCalefactor import Calefactor

class CalefactorGas(Calefactor):
    __matricula = ""
    __calorias = float


    def __init__(self,marca,modelo,matricula,gas):
        self.__matricula = matricula
        self.__calorias = float(gas)
        super().__init__(marca,modelo)

    '''
    def __repr__(self): #obtener estado del objeto
        return repr((super().__repr__(),self.__matricula, self.__calorias))
    '''

    def getcaloria(self):
        return self.__calorias
