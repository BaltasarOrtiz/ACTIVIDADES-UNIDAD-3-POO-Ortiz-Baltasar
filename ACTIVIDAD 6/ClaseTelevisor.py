from ClaseAparatos import Aparatos

class Televisor(Aparatos):
    __tipo_pantalla = ""
    __pulgadas = float
    __tipo_definicion = ""
    __conexion_internet = None

    def __init__(self,marca,model,col,pais,precio,tipo_pant,pulgad,tipo_def,conexion):
        self.__tipo_pantalla = tipo_pant
        self.__pulgadas = pulgad
        self.__tipo_definicion = tipo_def
        self.__conexion_internet = bool(conexion)
        super().__init__(marca,model,col,pais,precio)


    def toJSON(self):
        d = super().toJSON()["__atributos__"] #obtengo el diccionario de la superclase
        print(d)
        d.update(dict(
                    tipodepantalla = self.__tipo_pantalla,
                    pulgadas = self.__pulgadas,
                    tipodefinicion = self.__tipo_definicion,
                    conexionainternet = self.__conexion_internet
                ))
        dT = dict(
                __class__=self.__class__.__name__,
                __atributos__= d
            )

        print(d)
        return dT

    def getImporteF(self):
        total = self.getPreciobase()
        if self.__tipo_definicion.lower() == "sd":
            total = total  + total*0.01
        elif self.__tipo_definicion.lower() == "hd":
            total = total + total * 0.02
        elif self.__tipo_definicion.lower() == "full hd":
            total = total  + total * 0.03
        if self.__conexion_internet == True:
            total = total  + total * 0.10
        return total

