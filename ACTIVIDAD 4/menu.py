import os
from ClaseColeccion import Coleccion

class Menu:
    __op: int
    __coleccion: Coleccion

    def __init__(self):
        self.__op=0
        self.__coleccion = Coleccion(int(input("Ingrese dimension: ")))



    def mostrar(self):
        centinela=None
        while(centinela!=0):
            self.__op=int(input("""
            **Menu**        
Opcion ->[1] : Ingresar por teclado el  costo por m3 y cantidad que se estima consumir en m3 y mostrar marca y modelo del calefactor a gas natural de menor costo de consumo.
Opcion ->[2] : Ingresar por teclado el costo de el kilowatt/h, la cantidad que se estima consumir por hora y mostrar  marca  y modelo del calefactor eléctrico de menor consumo.
Opcion ->[3] : Teniendo en cuenta los dos ítems anteriores, muestre: tipo de calefactor y todos los datos del calefactor de menor consumo.
Opcion ->[0] : [Finalizar]

Ingrese Opcion-> """))

            if(self.__op==1):
               self.opcion1()

            elif(self.__op==2):
                self.opcion2()

            elif(self.__op==3):
                self.opcion3()

            elif(self.__op==0):
                centinela=0
            else:
                print("Error")


    def opcion1(self):
        os.system("cls")
        #self.__coleccion.prueba()
        costoporm3 = float(input("Ingrese el costo por metro cubico: "))
        cantesperada = float(input("Ingrese la cantidad que se estima consumir en metro cubico: "))
        self.__coleccion.mostrarmenorG(costoporm3, cantesperada)

    def opcion2(self):
        os.system("cls")
        costohora = float(input("Ingrese el costo de kw por hora: "))
        cantesperada = float(input("Ingrese la cantidad que se estima consumir por hora: "))
        self.__coleccion.mostrarmenorE(costohora, cantesperada)

    def opcion3(self):
        os.system("cls")

