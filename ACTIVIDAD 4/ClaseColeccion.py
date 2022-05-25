import csv

from ClaseCalefactor import Calefactor
from ClaseCalefactorGas import CalefactorGas
from ClaseCalefactorElectrico import CalefactorElectrico
from numpy import ndarray
import numpy as np


class Coleccion:
    __arreEstufas: ndarray

    def __init__(self, dim):
        self.__arreEstufas = np.empty(0, dtype=Calefactor)
        self.cargarEstufaGas()
        self.cargarEstufaElectrica()



    def cargarEstufaGas(self):
        archivo = open("calefactor-a-gas.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            eg = CalefactorGas(fila[0], fila[1], fila[2], fila[3])
            self.__arreEstufas = np.append(self.__arreEstufas, eg)

        archivo.close()


    def cargarEstufaElectrica(self):
        archivo = open("calfactor-electrico.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            ee = CalefactorElectrico(fila[0], fila[1], fila[2])
            self.__arreEstufas = np.append(self.__arreEstufas, ee)

        archivo.close()

    def prueba(self):
        print(len(self.__arreEstufas))
        print(self.__arreEstufas)

    def mostrarmenorG(self, costoporm3, cantesperada):
        min = 999999999

        for elem in self.__arreEstufas:
            if type(elem) == CalefactorGas:
                costot = float((elem.getcaloria()/1000) * cantesperada * costoporm3)
                if costot < min:
                    min = costot
                    mincale = elem

        print("Calefactor de menor consumo")
        print(mincale)

    def mostrarmenorE(self, costohora, cantesperada):
        min = 999999999

        for elem in self.__arreEstufas:
            if type(elem) == CalefactorElectrico:
                costot = float((elem.getpotencia()/1000) * cantesperada * costohora)
                if costot < min:
                    min = costot
                    mincale = elem

        print("Calefactor de menor consumo")
        print(mincale)



