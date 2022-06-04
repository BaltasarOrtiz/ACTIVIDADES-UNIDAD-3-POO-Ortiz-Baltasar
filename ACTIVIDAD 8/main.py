from menu import Menu

if __name__ == '__main__':
    m = Menu()

    bandera = True
    while bandera is True:
        usuario = input("Ingrese el usuario (Director/Tesorero) - (Fin para terminar): ")
        if usuario != "Fin":
            contra = input("Ingrese la contraseña: ")

            if usuario == "Tesorero" and contra == "uTesoreso/ag@74ck":
                m.menuTesorero()
            elif usuario == "Director" and contra == "uDirector/ufC77#!1":
                m.menuDirector()
            else:
                print("Contraseña o Usuario Incorrecto")

        elif usuario == "Fin":
            bandera = False

