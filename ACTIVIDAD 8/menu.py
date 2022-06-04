import os
from ObjectEncoder import ObjectEncoder
from ClaseLista import Lista
from ClaseManejadorInterface import ManejadorInterface

class Menu:
    __op: int
    __ObjectEncoder: ObjectEncoder
    __controlLista: Lista
    __ManejadorInterface: ManejadorInterface


    def __init__(self):
        self.__op=0
        self.__ObjectEncoder = ObjectEncoder()
        self.__controlLista = Lista()
        self.__ObjectEncoder.cargarobjeto(self.__controlLista)
        self.__ManejadorInterface = ManejadorInterface()


    def mostrar(self):

        centinela=None
        while(centinela!=0):
            self.__op=int(input("""
            --------------------------------------------OPCIONES GENERALES--------------------------------------------
            **Menu**
Opcion ->[12] : Crear Archivo .json
----------------------------------------
Opcion ->[1] : Insertar a agentes a la colección.
Opcion ->[2] : Agregar agentes a la colección.
Opcion ->[3] : Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.
Opcion ->[4] : Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.
Opcion ->[5] : Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.
Opcion ->[6] : Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.
Opcion ->[7] : Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría, al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada.
Opcion ->[8] : Almacenar los datos de todos los agentes en el archivo “personal.json”   

Opcion ->[0] : [SALIR DE OPCIONES GENERALES]
------------------------------------------------------------------------------------------------------------------------------------
Ingrese Opcion-> """))

            if(self.__op==12):
               self.opcion12()

            elif(self.__op==1):
               self.opcion1()

            elif(self.__op==2):
                self.opcion2()

            elif(self.__op==3):
                self.opcion3()

            elif(self.__op==4):
                self.opcion4()

            elif(self.__op==5):
                self.opcion5()

            elif(self.__op==6):
                self.opcion6()

            elif(self.__op==7):
                self.opcion7()

            elif(self.__op==8):
                self.opcion8()

            elif(self.__op==0):
                centinela=0
            else:
                print("Error")

    def menuTesorero(self):
        centinela = None
        while(centinela!=0):
            opcion=input("""
            **Menu TESORERO**
Opcion ->[A]: Consultar el gasto de sueldos
Opcion ->[F]: SALIR DE USUARIO

Opcion ->[X]: Volver a opciones generales 
Ingrese Opcion->""").upper()

            if opcion=="A":
                self.__ManejadorInterface.llamarinterfaces(self.__controlLista, "Tesorero")
            elif opcion == "F":
                centinela=0
            elif opcion == "X":
                self.mostrar()
            else:
                print("Opcion Incorrecta")



    def menuDirector(self):
        centinela = None
        while(centinela!=0):
            opcion=input("""
            **Menu DIRECTOR**
Opcion ->[A]: Modificar el sueldo básico de todos los agentes.
Opcion ->[B]: Modificar porcentaje por cargo.
Opcion ->[C]: Modificar porcentaje extra para un docente investigador.
Opcion ->[D]: Modificar importe extra.
Opcion ->[F]: SALIR DE USUARIO

Opcion ->[X]: Volver a opciones generales 
Ingrese Opcion->""").upper()

            if opcion=="A":
                self.__ManejadorInterface.llamarinterfaces(self.__controlLista, "Director", "A")
            elif opcion == "B":
                self.__ManejadorInterface.llamarinterfaces(self.__controlLista, "Director", "B")
            elif opcion == "C":
                self.__ManejadorInterface.llamarinterfaces(self.__controlLista, "Director", "C")
            elif opcion == "D":
                self.__ManejadorInterface.llamarinterfaces(self.__controlLista, "Director", "D")
            elif opcion == "F":
                centinela=0
            elif opcion == "X":
                self.mostrar()
            else:
                print("Opcion Incorrecta")



    #cargar Json
    def opcion12(self):
        os.system("cls")
        self.__ObjectEncoder.cargaJson("personal.json")

    #opciones de menu generales
    def opcion1(self):
        os.system("cls")
        self.__ManejadorInterface.llamarinterfaces(self.__controlLista,1)

    def opcion2(self):
        os.system("cls")
        self.__ManejadorInterface.llamarinterfaces(self.__controlLista,2)

    def opcion3(self):
        os.system("cls")
        self.__ManejadorInterface.llamarinterfaces(self.__controlLista,3)

    def opcion4(self):
        os.system("cls")
        carrera = input("Ingrese el nombre de la carrera: ")
        self.__controlLista.mostrardocenteinv(carrera)

    def opcion5(self):
        os.system("cls")
        area = input("Ingrese el area de investigacion: ")
        self.__controlLista.contar(area)

    def opcion6(self):
        os.system("cls")
        self.__controlLista.listadoOrdenado()

    def opcion7(self):
        os.system("cls")
        categ = input("Ingrese una categoria de investigacion (I, II, III, IV o V): ")
        self.__controlLista.mostrarlistadoinv(categ)

    def opcion8(self):
        os.system("cls")
        listaguardar = self.__controlLista.obtenerlista()
        self.__ObjectEncoder.guardarJSONArchivo(listaguardar, "nuevospersonal.json")

