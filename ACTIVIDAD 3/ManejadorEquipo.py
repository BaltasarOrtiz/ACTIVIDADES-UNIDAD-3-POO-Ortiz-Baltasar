from ClaseEquipo import Equipo
import csv

from numpy import ndarray
import numpy as np


class ManejadorEquipo:
    __arreEquipo: ndarray



    def __init__(self):
        self.__arreEquipo = self.cargarobjetos()


    def cargarobjetos(self):
        listatemp=[]
        archivo = open("equipos.csv")
        reader = csv.reader(archivo, delimiter=";")

        fila = next(reader)
        cant = int(fila[0])
        i=0
        while i<cant:
            fila = next(reader)
            e = Equipo(fila[0], fila[1])
            listatemp.append(e)
            print(fila)
            i+=1

        archivo.close()
        arre = np.array(listatemp)
        return arre

    def prueba(self):
        print("Longitud del arreglo de equipo: {}".format(len(self.__arreEquipo)))

    def getequipo(self, nomequipo):
        i=0
        bandera = True
        valorretorno = None
        while i<len(self.__arreEquipo) and bandera:
            print(self.__arreEquipo[i].getnombre())
            if self.__arreEquipo[i].getnombre() == nomequipo:
                valorretorno = self.__arreEquipo[i]
                bandera = False
            else:
                valorretorno = None
            i+=1

        return valorretorno

