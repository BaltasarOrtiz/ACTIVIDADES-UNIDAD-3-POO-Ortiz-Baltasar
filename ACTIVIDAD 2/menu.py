import os
from ManejadorRamo import ManejadorRamo
from ManejadorFlores import ManejadorFlores

class Menu:
    __op: int
    __controlFlores: ManejadorFlores
    __controlRamo: ManejadorRamo

    def __init__(self):
        self.__op=0
        self.__controlRamo = ManejadorRamo()
        self.__controlFlores = ManejadorFlores()


    def mostrar(self):
        centinela=None
        while(centinela!=0):
            self.__op=int(input("""
            **Menu**        
Opcion ->[1] : Vender Ramo
Opcion ->[2] : Mostrar el nombre de las 5 flores  más pedidas en un ramo, considerando todos los ramos vendidos.
Opcion ->[3] : Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño considerando todos los ramos vendidos.
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
        self.__controlRamo.venderramo(self.__controlFlores)

    def opcion2(self):
        os.system("cls")
        self.__controlRamo.mostrarmasvendidas()

    def opcion3(self):
        os.system("cls")
        tam = input("Ingrese un tamano de ramo: ")
        self.__controlRamo.mostrarramos(tam)
