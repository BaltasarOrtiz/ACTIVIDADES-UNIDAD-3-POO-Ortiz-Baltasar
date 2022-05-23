from ClaseContrato import Contrato
from ManejadorEquipo import ManejadorEquipo
from ManejadorJugador import ManejadorJugador
import datetime
import numpy as np




class ManejadorContrato:
    __controljugador: ManejadorJugador
    __controlequipo: ManejadorEquipo
    __arrecontrato: np.ndarray


    def __init__(self, manjug, maneq):
        self.__controljugador = manjug
        self.__controlequipo = maneq
        self.__arrecontrato = np.empty(0, Contrato)


    def crearcontrato(self, dni, equipo, fechaini, fechafinal, pagomensual):
        jug = self.__controljugador.getjugador(dni)
        equip = self.__controlequipo.getequipo(equipo)
        if jug is not None and equip is not None:
            c = Contrato(fechaini, fechafinal, float(pagomensual), jug, equip)
            self.__arrecontrato = np.append(self.__arrecontrato, c)
        else:
            print("Nombre de jugador o equipo invalidos")


    def prueba(self):
        print(len(self.__arrecontrato))


    def mostrarequipo(self, dni):
        i=0
        bandera = True
        while i<len(self.__arrecontrato) and bandera:
            if self.__arrecontrato[i].getdnijugador( ) == dni:
                print("El jugador esta contratado")
                print("Nombre de equipo: {} -- Fecha de finalizacion del contrato: {}".format(self.__arrecontrato[i].getnomequipo(), self.__arrecontrato[i].getfechafin()))
                bandera = False
            i+=1


    def mostrarcontratos(self, nom):
        bandera = False
        for i in range(len(self.__arrecontrato)):
            fechaactual = datetime.date.today()
            vence6meses = fechaactual + datetime.timedelta(days=365/2)
            fechafin = self.__arrecontrato[i].getfechafin()
            eq = self.__arrecontrato[i].getequipo()
            if eq.getnombre() == nom:
                if fechafin >= fechaactual and fechafin <= vence6meses:
                    jugador = self.__arrecontrato[i].getjugador()
                    print("Jugador: {}, su contrato vence en {} mes/meses".format(jugador, fechafin.month - fechaactual.month))
                    bandera = True
        if not bandera:
            print("El equipo, {} no posee contratos que tiene una fecha de vencimiento dentro de los proximos 6 meses".format(eq.getnombre()))



    def obtenerimporte(self, nom):
        total: float = 0
        for elem in self.__arrecontrato:
            if elem.getnomequipo() == nom:
                total+=elem.getpago()

        print("Para el equipo: {}, el importe total es: {}".format(nom, total))


    def guardarcontrato(self):

        with open("contratoguardar.txt", "w") as file:
            file.write("PagoMensual;FechaInicio;FechaFin;DNIjugador;NombreEquipo\n")

            for contrato in self.__arrecontrato:
                file.write(
                    str(contrato.getpago()) + ";" +
                    str(contrato.getfechaini()) + ";" +
                    str(contrato.getfechafin()) +  ";" +
                    contrato.getdnijugador() + ";" +
                    contrato.getnomequipo() + ";" + "\n"
                )
