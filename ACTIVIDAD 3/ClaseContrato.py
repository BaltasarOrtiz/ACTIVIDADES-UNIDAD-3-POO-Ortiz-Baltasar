import datetime

class Contrato:
    __fechainicio: datetime
    __fechadefin: datetime
    __pagomensual = float
    __jugador = None
    __equipo = None


    def __init__(self, fechaini, fechafin, pagomen, jugador, equipo):
        self.__fechainicio = self.setfecha(fechaini)
        self.__fechadefin = self.setfecha(fechafin)
        self.__pagomensual = float(pagomen)
        self.__jugador = jugador
        self.__equipo = equipo

    def setfecha(self, fechafin):
        f = datetime.datetime.strptime(fechafin, "%d/%m/%Y").date()
        return f

    def getfechaini(self):
        return self.__fechainicio

    def getfechafin(self):
        return self.__fechadefin

    def getdnijugador(self):
        return self.__jugador.getdni()

    def getnomequipo(self):
        return self.__equipo.getnombre()

    def getpago(self):
        return self.__pagomensual

    #obtener jugador y equipo
    def getequipo(self):
        return self.__equipo
    def getjugador(self):
        return self.__jugador
