from ClaseAparatos import Aparatos

class Heladera(Aparatos):
    __capacidad: float
    __freezer = None
    __cicl = None

    def __init__(self,marca,model,col,pais,precio,capacidad,freezer,cicl):
        self.__capacidad = float(capacidad)
        self.__freezer = freezer
        self.__ciclica = cicl
        super().__init__(marca,model,col,pais,precio)


    def toJSON(self):
        d = super().toJSON()["__atributos__"] #obtengo el diccionario de la superclase
        print(d)
        d.update(dict(
                    capacidadlitros = self.__capacidad,
                    freezer = self.__freezer,
                    ciclica = self.__cicl,
                ))
        dH = dict(
                __class__=self.__class__.__name__,
                __atributos__= d
            )

        print(d)
        return dH


    def getImporteF(self):
        total = self.getPreciobase()
        if self.__freezer == False:
            total = total + total*0.01
        elif self.__freezer == True:
            total = total  + total*0.05
        elif self.__ciclica == True:
            total = total  + total*0.10

