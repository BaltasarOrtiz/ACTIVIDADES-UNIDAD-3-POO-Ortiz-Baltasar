from ClaseHeladera import Heladera
from ClaseLavarropa import Lavarropa
from ClaseTelevisor import Televisor
from ClaseNodo import Nodo
from ClaseInterface import ClaseInterface
from zope.interface import implementer

@implementer(ClaseInterface)
class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo=None
        self.__actual=None

    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato=self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato

    def agregarAparato(self,aparato):
        nodo=Nodo(aparato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1
        print(self.__tope)

    #interfaces
    def insertarelemento(self, pos, objeto):
        counter = 1
        cabeza = self.__comienzo
        if self.__comienzo is None:
            nodo = Nodo(objeto)
            nodo.setSiguiente(self.__comienzo)
            self.__comienzo = nodo
            self.__actual = nodo
            self.__tope += 1
        while counter < pos - 1 and cabeza is not None:
            counter += 1
            cabeza = cabeza.getSiguiente()
        if pos == 1:
            newNode = Nodo(objeto)
            newNode.setSiguiente(cabeza)
            self.__comienzo = newNode
            self.__actual = newNode
        else:
            newNode = Nodo(objeto)
            newNode.setSiguiente(cabeza.getSiguiente())
            cabeza.setSiguiente(newNode)
        self.__tope+=1

    def agregarelementofinal(self, objeto):
        print("Insertando al final")
        if self.__comienzo is None:
            newNode = Nodo(objeto)
            newNode.setSiguiente(self.__comienzo)
            self.__comienzo = newNode
            self.__actual = newNode
        else:
            cabeza = self.__comienzo
            while cabeza.getSiguiente() is not None:
                cabeza = cabeza.getSiguiente()
            newNode = Nodo(objeto)
            cabeza.setSiguiente(newNode)
        self.__tope+=1

    def mostrarelemento(self, pos):
        dato = None
        cont = 1
        if self.__comienzo is None and pos != 1:
            dato = None
        cabeza = self.__comienzo
        while cabeza.getSiguiente() is not None and cont < pos:
            cont += 1
            cabeza = cabeza.getSiguiente()
        if cont == pos:
            dato = cabeza.getDato()

        return dato

    #funcionalidades
    def mostrarcantidades(self):
        cantlav = 0
        canthel = 0
        canttel = 0
        cabeza = self.__comienzo
        while cabeza is not None:
            if type(cabeza.getDato()) is Heladera and cabeza.getDato().getmarca() == "Philips":
                canthel+=1
            elif type(cabeza.getDato()) is Televisor and cabeza.getDato().getmarca() == "Philips":
                canttel+=1
            elif type(cabeza.getDato()) is Lavarropa and cabeza.getDato().getmarca() == "Philips":
                cantlav+=1

            cabeza = cabeza.getSiguiente()

        print("Cantidad de Heladeras de la marca Philips: {}".format(canthel))
        print("Cantidad de Televisores de la marca Philips: {}".format(canttel))
        print("Cantidad de Lavarropas de la marca Philips: {}".format(cantlav))

    def mostrarcargasup(self):
        cabeza = self.__comienzo
        while cabeza is not None:
            if type(cabeza.getDato()) is Lavarropa and cabeza.getDato().getcarga() == "Superior":
                print("Lavarropa marca: {}".format(cabeza.getDato().getmarca()))

            cabeza = cabeza.getSiguiente()


    def mostrartodos(self):
        cabeza = self.__comienzo
        while cabeza is not None:
            print("Aparatos de la Empresa")
            print("Marca: {} -- Pais de Fabricacion: {} -- Importe de Venta: {}".format(cabeza.getDato().getmarca(), cabeza.getDato().getpais(), cabeza.getDato().getImporteF()))
            cabeza = cabeza.getSiguiente()


    def guardarjson(self, ObjectEncoder):
        lista = []
        cabeza = self.__comienzo
        while cabeza is not None:
            dato = cabeza.getDato()
            dicc = dato.toJSON()
            lista.append(dicc)
            cabeza = cabeza.getSiguiente()

        ObjectEncoder.guardarJSONArchivo(lista, "nuevosaparatos.json")
        print("Archivo Creado Correctamente")



