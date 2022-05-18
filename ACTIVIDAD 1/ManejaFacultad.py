from Facultades import Facultad
from Carrera import Carrera
import csv

class ManejaFacultad:
    __listaFacultad: list

    def __init__(self):
        self.__listaFacultad = self.cargarobjetos()

    def cargarobjetos(self):
        listaf=[]
        archivo = open("facultades.csv")
        reader = csv.reader(archivo, delimiter=",")
        fila=next(reader)
        bandera = True

        while bandera:
            print("Facultad")
            print(fila)
            print("Carreras")
            filaCarrera=next(reader)
            f = Facultad(fila[0], fila[1], fila[2], fila[3], fila[4])
            listaf.append(f)
            while bandera and fila[0] == filaCarrera[0]:
                print(filaCarrera)
                try:
                    c = Carrera(filaCarrera[1], filaCarrera[2], filaCarrera[3], filaCarrera[4], filaCarrera[5])
                    f.agregarcarre(c)
                    filaCarrera=next(reader)
                except StopIteration:
                    bandera=False

            fila=filaCarrera

        archivo.close()
        return listaf


    def mostrarfacu(self, cod):
        i=0
        bandera = True
        while i<len(self.__listaFacultad) and bandera:
            if cod == self.__listaFacultad[i].getcod():
                print(self.__listaFacultad[i].getnombre())
                for j in range(self.__listaFacultad[i].longitudcarre()):
                    print("Carrera: {}  --  Duracion: {}".format(self.__listaFacultad[i].getnomcarre(j), self.__listaFacultad[i].getduracarre(j)))
                bandera = False
            else:
                i+=1


    def mostrarcarre(self, nombre):
        i=0
        bandera = True
        while i<len(self.__listaFacultad) and bandera:
            bandera2 = True
            j=0
            while j<self.__listaFacultad[i].longitudcarre() and bandera2:
                if self.__listaFacultad[i].getnomcarre(j) == nombre:
                    print("Codigo de facultad: {}   --  Codigo de carrera: {}".format(self.__listaFacultad[i].getcod(), self.__listaFacultad[i].getcodcarre(j)))
                    print("Nombre de carrera: {}    --  Localidad: {}".format(self.__listaFacultad[i].getnomcarre(j), self.__listaFacultad[i].getlocalidad()))
                    bandera2 = False
                    bandera = False
                else:
                    j+=1
            i+=1




