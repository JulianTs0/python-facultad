from funciones import *

__name__ = "402079_1K10_T3"


def main():
    op = -1
    vec = []

    while op != 0:
        menu()
        op = int(input("Ingrese una opcion: "))

        if op == 1:
            vec = auto_load()
        elif op == 2 and vec != []:
            show_vec(vec)
        elif op == 3 and vec != []:
            show_matrix(vec)
        elif op == 4 and vec != []:
            create_file(vec)
        elif op == 5 and vec != []:
            show_file()
        elif str(op) not in "012345":
            print("\nIngrese una opcion VALIDA")
        elif op != 0:
            print("\nCarge el vector antes de usar cualquier opcion")


if __name__ == "402079_1K10_T3":
    main()
