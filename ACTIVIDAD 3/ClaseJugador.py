import datetime

class Jugador:
    __nombre = ""
    __DNI = ""
    __ciudNatal = ""
    __paisOrg = ""
    __fechanacimi: datetime

    def __init__(self, nom, dni, ciud, pais, fecha):
        self.__nombre = nom
        self.__DNI = dni
        self.__ciudNatal = ciud
        self.__paisOrg = pais
        self.__fechanacimi = self.setdate(fecha)


    def getdni(self):
        return self.__DNI

    def getnombre(self):
        return self.__nombre

    def setdate(self, fecha):
        f = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
        return f

