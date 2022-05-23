from ManejadorEquipo import ManejadorEquipo
from ManejadorJugador import ManejadorJugador
from ManejadorContrato import ManejadorContrato
import os

class Menu:
    __op: int
    __controlEquipo: ManejadorEquipo
    __controlJugador: ManejadorJugador
    __controlContrato: ManejadorContrato

    def __init__(self):
        self.__op=0
        self.__controlEquipo = ManejadorEquipo()
        self.__controlJugador = ManejadorJugador()
        self.__controlContrato = ManejadorContrato(self.__controlJugador, self.__controlEquipo)

    def mostrar(self):
        centinela=None
        while(centinela!=0):
            self.__op=int(input("""
            **Menu**        
Opcion ->[1] : Crear Contrato
Opcion ->[2] : Consultar jugadores Contratados: Ingresar el DNI de un jugador, si está contratado, mostrar el nombre del Equipo en el que fue contratado, y la fecha de finalización de contrato.
Opcion ->[3] : Consultar Contratos: Ingresar el identificador de un Equipo y listar los datos de los Jugadores cuyo contrato vence en 6 meses.
Opcion ->[4] : Obtener importe de contratos: Para un nombre de equipo leído desde teclado, determinar el importe total de los contratos que posee con los jugadores del equipo.
Opcion ->[5] : Guardar Contratos: Generar un nuevo archivo que contenga los siguientes datos de los contratos: DNI del jugador, Nombre del equipo, fecha de inicio, fecha de fin, y el pago mensual.
Opcion ->[0] : [Finalizar]

Ingrese Opcion-> """))

            if(self.__op==1):
               self.opcion1()

            elif(self.__op==2):
                self.opcion2()

            elif(self.__op==3):
                self.opcion3()

            elif(self.__op==4):
                self.opcion4()

            elif(self.__op==5):
                self.opcion5()

            elif(self.__op==0):
                centinela=0
            else:
                print("Error")


    def opcion1(self):
        os.system("cls")
        dni = input("Ingrese el DNI: ")
        equipo = input("Ingrese el nombre del equipo: ")
        fechaini = input("Ingrese la fecha de inicio: ")
        fechafinal = input("Ingrese la fecha de finalizacion: ")
        pago = input("Ingrese el pago mensual: ")

        self.__controlContrato.crearcontrato(dni, equipo, fechaini, fechafinal, pago)
        self.__controlContrato.prueba()


    def opcion2(self):
        os.system("cls")
        dni = input("Ingrese DNI: ")
        self.__controlContrato.mostrarequipo(dni)

    def opcion3(self):
        os.system("cls")
        nom = input("Ingrese el nombre de un equipo: ")

    def opcion4(self):
        os.system("cls")
        nom = input("Ingrese un nombre de equipo: ")
        self.__controlContrato.obtenerimporte(nom)

    def opcion5(self):
        os.system("cls")
        self.__controlContrato.guardarcontrato()

'''
DNI 1
Equipo a
14/4/2022
14/4/2025
4500
'''
