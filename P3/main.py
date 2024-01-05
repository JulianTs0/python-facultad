from funciones import *

__name__ = "main"


def main():
    op = -1
    vector = []

    while op != 0:
        print("\n1- Cargar el vector")
        print("2- Mostrar los datos")
        print("3- Determinar los servicios")
        print("4- Buscar servicio")
        print("0- Salir")
        op = int(input("Ingrese una opcion: "))
        if op == 1:
            vector = auto_load()
        elif op == 2 and vector != []:
            show_vec(vector)
        elif op == 3 and vector != []:
            by_type(vector)
        elif op == 4 and vector != []:
            search_name(vector)
        elif str(op) in "234" and vector == []:
            print("\nCarge el vector antes de usar alguna opcion")
        elif op != 0:
            print("\nIngrese una opcion valida")


if __name__ == "main":
    main()
