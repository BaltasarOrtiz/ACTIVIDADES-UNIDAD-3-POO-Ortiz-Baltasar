from ClaseRamo import Ramo


class ManejadorRamo:
    __listaramo: list


    def __init__(self):
        self.__listaramo = []


    def venderramo(self, controlflor):

        tamano = input("Ingrese el tamaño del ramo: ")

        if tamano not in ["grande", "mediano", "chico"]:
            print("El tamaño del ramo elegido no es valido")
        else:
            ramo = Ramo(tamano)
            bandera=True
            while ramo.getcantidaflores()<= 5 and bandera:
                nombreFlor = input("Ingrese el nombre de la flor, escriba 'Terminar' para finalizar: ")

                if nombreFlor == "Terminar":
                    bandera=False #finaliza la carga

                flor = controlflor.obtenerflor(nombreFlor)

                if flor is None:
                    print("La flor no existe")
                else:
                    ramo.agregarflor(flor)

            self.__listaramo.append(ramo)


    def mostrarmasvendidas(self):
        diccionario: dict[str, int] = {}

        for elem in self.__listaramo:
            for flor in elem.getlistaflores():
                nom=flor.getnombre()
                if nom in diccionario:
                    diccionario[nom]+=1
                else:
                    diccionario[nom]=1

        lista = sorted(diccionario.items(), key=lambda x: x[1], reverse=True)

        print("Nombre de las 5 flores mas vendidas")
        i=0
        while i<5 and i<len(lista):
            print(lista[i][0])
            i+=1



    def mostrarramos(self, tiporamo):
        print(len(self.__listaramo))
        print("Para el ramo de tamaño: {}".format(tiporamo))
        for elem in self.__listaramo:
            if elem.gettamano() == tiporamo:
                for flor in elem.getlistaflores():
                    print("Flores vendidas: {}".format(flor.getnombre()))

