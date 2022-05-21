from ClaseFlores import Flores
import csv

import numpy as np
from numpy import ndarray

class ManejadorFlores:
    __arreFlores: ndarray

    def __init__(self):
        self.__arreFlores = self.cargarobjetos()


    def cargarobjetos(self):
        listatemp=[]
        archivo = open("flores.csv")
        reader = csv.reader(archivo, delimiter = ";")
        for fila in reader:
            f = Flores(fila[0], fila[1], fila[2], fila[3])
            listatemp.append(f)

        archivo.close()
        arre = np.array(listatemp)
        return arre


    def obtenerflor(self, nombreflor):
        i=0
        bandera = True
        retornaflor = None
        while i<len(self.__arreFlores) and bandera:
            if self.__arreFlores[i].getnombre() == nombreflor:
                retornaflor = self.__arreFlores[i]
                bandera = False
            i+=1

        return retornaflor


