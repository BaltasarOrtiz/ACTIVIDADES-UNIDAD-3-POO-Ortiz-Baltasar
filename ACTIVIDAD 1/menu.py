from ManejaFacultad import ManejaFacultad
import os

class Menu:
    __op: int
    __controlFacul: ManejaFacultad

    def __init__(self):
        self.__op=0
        self.__controlFacul = ManejaFacultad()

    def mostrar(self):
        centinela=None
        while(centinela!=0):
            self.__op=int(input("""
            **Menu**        
Opcion ->[1] : Ingresar el código  de una facultad y mostrar nombre de la facultad, nombre  y duración de cada una de las carreras que se dictan en esa facultad.
Opcion ->[2] : Dado el nombre de una carrera, mostrar código (se conforma con número de código de Facultad y código de carrera), nombre y localidad de la facultad donde esta se dicta.
Opcion ->[0] : [Finalizar]

Ingrese Opcion-> """))

            if(self.__op==1):
               self.opcion1()

            elif(self.__op==2):
                self.opcion2()

            elif(self.__op==0):
                centinela=0
            else:
                print("Error")

    def opcion1(self):
        os.system("cls")
        cod = int(input("Ingrese el codigo de una facultad: "))
        self.__controlFacul.mostrarfacu(cod)

    def opcion2(self):
        os.system("cls")
        nombre = input("Ingrese el nombre de una carrera: ")
        self.__controlFacul.mostrarcarre(nombre)

    def opcion4(self):
        os.system("cls")


