from ClaseAparatos import Aparatos

class Lavarropa(Aparatos):
    __capacidad = float
    __velocidad = int
    __ct_program = int
    __tipo_de_carga = ""

    def __init__(self, marca,model,col,pais,precio,capacidad,velocidad,ct,tipo):
        self.__capacidad = int(capacidad)
        self.__velocidad = int(velocidad)
        self.__ct_program = int(ct)
        self.__tipo_de_carga = tipo
        super().__init__(marca,model,col,pais,precio)

    def toJSON(self):
        d = super().toJSON()["__atributos__"] #obtengo el diccionario de la superclase
        print(d)
        d.update(dict(
                    capacidadlavado = self.__capacidad,
                    velocidadcentrifugado = self.__velocidad,
                    cantidadprogramas = self.__ct_program,
                    tipodecarga = self.__tipo_de_carga
                ))
        dL = dict(
                __class__=self.__class__.__name__,
                __atributos__= d
            )
        print(d)
        return dL


    def getcarga(self):
        return self.__tipo_de_carga

    def getImporteF(self):
        total = self.getPreciobase()
        if self.__capacidad <= 5:
            total = total + total*0.01
        elif self.__capacidad > 5:
            total = total  + total*0.03
        return total

