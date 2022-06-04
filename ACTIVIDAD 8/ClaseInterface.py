from zope.interface import Interface

class Interfaz(Interface):
    def insertarelemento(self, posicion, elemento):
        pass

    def agregarelementofinal(self, elemento):
        pass

    def mostrarelemento(self, posicion):
        pass


class ITesorero(Interface):
    def gastosSueldoPorEmpleado(self, dni):
       pass


class IDirector(Interface):
    def modificarBasico(self, dni, nuevoBasico):
        pass

    def modificarPorcentajeporcargo(self, dni, nuevoPorcentaje):
        pass

    def modificarPorcentajeporcategoria(self, dni, nuevoPorcentaje):
        pass

    def modificarImporteExtra(self, dni, nuevoImporteExtra):
        pass
