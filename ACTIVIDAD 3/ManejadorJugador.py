from ClaseJugador import Jugador
import datetime
import csv

class ManejadorJugador:
    __listajugador: list


    def __init__(self):
        self.__listajugador = self.cargarobjeto()


    def cargarobjeto(self):
        listatemp = []
        archivo = open("jugadores.csv")
        reader = csv.reader(archivo, delimiter = ";")
        next(reader)
        for fila in reader:
            j = Jugador(fila[0], fila[1], fila[2], fila[3], fila[4])
            listatemp.append(j)

        archivo.close()
        return listatemp


    def getjugador(self, dni):
        i=0
        bandera = True
        valorretorno = None
        while i<len(self.__listajugador) and bandera:
            if self.__listajugador[i].getdni() == dni:
                valorretorno = self.__listajugador[i]
                bandera = False
            else:
                valorretorno = None
            i+=1

        return valorretorno



