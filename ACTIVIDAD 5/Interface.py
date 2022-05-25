from zope.interface import Interface


class Interfaz(Interface):
    def insertarelemento(self, objeto, posicion):
        pass

    def agregarelemento(self, elemento):
        pass

    def mostrarelemento(self, posicion):
        pass
