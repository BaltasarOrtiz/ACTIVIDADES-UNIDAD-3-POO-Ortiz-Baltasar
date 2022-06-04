from ClaseInterface import Interfaz
from ClaseInterface import ITesorero
from ClaseInterface import IDirector
from ObjectEncoder import ObjectEncoder


class ManejadorInterface:
    __controlEncoder: ObjectEncoder

    def __init__(self):
        self.__controlEncoder = ObjectEncoder()

    def invocarinter(self, clista: Interfaz, op):

        if op == 1:
            pos = int(input("Ingrese la posicion: "))
            tipo = input("Ingrese un tipo de personal: ")
            objeto = self.__controlEncoder.retornarobjeto(tipo) #obtengo el objeto
            if objeto is not None:
                clista.insertarelemento(pos, objeto) #interfaz de insertar en cualquier posicion
            else:
                print("El elemento a insertar no es un objeto")

        if op == 2:
            tipo = input("Ingrese un tipo de personal: ")
            objeto = self.__controlEncoder.retornarobjeto(tipo) #obtengo el objeto
            if objeto is not None:
                clista.agregarelementofinal(objeto) #interfaz de agregaralfinal
            else:
                print("El elemento a insertar no es un objeto")

        if op == 3:
            pos = int(input("Ingrese una posicion de la lista: "))
            dato = clista.mostrarelemento(pos) #interfaz de mostrar
            if dato is not None:
                print(dato)
            else:
                print("Posicion incorrecta")

    def interfacesTesorero(self, clista: ITesorero):
        cuil = input("Ingrese el CUIL del agente: ")
        clista.gastosSueldoPorEmpleado(cuil)

    def interfacesDirector(self, clista: IDirector, opdirect):
        if opdirect == "A":
            print("MODIFICACION DE SUELDO BASICO")
            cuil = input("Ingrese el cuil del agente: ")
            nuevoBasico = float(input("Ingrese el nuevo sueldo basico: "))
            clista.modificarBasico(cuil, nuevoBasico)
        elif opdirect == "B":
            print("MODIFICACION DE PORCENTAJE POR CARGO")
            cuil = input("Ingrese el cuil del agente: ")
            nuevoPorcentaje = float(input("Ingrese el nuevo sueldo basico: "))
            clista.modificarPorcentajeporcargo(cuil, nuevoPorcentaje)
        elif opdirect == "C":
            print("MODIFICACION DE PORCENTAJE POR CATEGORIA")
            cuil = input("Ingrese el cuil del agente: ")
            nuevoPorcentaje = float(input("Ingrese el nuevo sueldo basico: "))
            clista.modificarPorcentajeporcategoria(cuil, nuevoPorcentaje)
        elif opdirect == "D":
            print("MODIFICACION DE IMPORTE EXTRA")
            cuil = input("Ingrese el cuil del agente: ")
            nuevoImporteExtra = float(input("Ingrese el nuevo sueldo basico: "))
            clista.modificarImporteExtra(cuil, nuevoImporteExtra)





    def llamarinterfaces(self, clista, opcion, opdirect=None):
        if type(opcion) is int:
            self.invocarinter(Interfaz(clista), opcion)
        elif opcion == "Tesorero":
            self.interfacesTesorero(ITesorero(clista))
        elif opcion == "Director":
            self.interfacesDirector(IDirector(clista), opdirect)
        else:
            print("Opcion incorrecta")



