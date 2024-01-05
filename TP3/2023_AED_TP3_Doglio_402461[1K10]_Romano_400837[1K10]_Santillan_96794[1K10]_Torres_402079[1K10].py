__name__ = "TP3AED - Doglio, Romano, Santillan, Torres"

from FuncionesTP3 import *


def principal():
    vec_main = []
    op = 1

    while op != "0":
        mostrar_menu()
        op = input("Ingrese una opción: ")

        if op == "1":
            vec_main = cargar_arreglo(vec_main, "peajes-tp3.txt")
        elif op == "2":
            cargar_datos(vec_main)
        elif op == "3":
            if vec_main:
                ordenar_menor_mayor(vec_main)
                mostrar_datos(vec_main)
            else:
                print("Por favor cargar el arreglo")
        elif op == "4":
            if vec_main:
                buscar_penpaisx(vec_main)
            else:
                print("Por favor cargar el arreglo")
        elif op == "5":
            if vec_main:
                buscar_ticket(vec_main)
            else:
                print("Por favor cargar el arreglo")
        elif op == "6":
            if vec_main:
                cantidad_patentes(vec_main)
            else:
                print("Por favor cargar el arreglo")
        elif op == "7":
            if vec_main:
                importe_tipo = importe_patente(vec_main)
                for i in range(len(importe_tipo)):
                    print(f"Importe acumulado del vehículo tipo {i}: {importe_tipo[i]}")
            else:
                print("Por favor cargar el arreglo")
        elif op == "8":
            if vec_main:
                acumulador_tipo = importe_patente(vec_main)
                mayor_acu(acumulador_tipo)
            else:
                print("Por favor cargar el arreglo")
        elif op == "9":
            if vec_main:
                promedio_distancia(vec_main)
            else:
                print("Por favor cargar el arreglo")
        elif op == "0":
            print("Fin del programa")
        else:
            print("Error, ingrese una opción valida")


if __name__ == "TP3AED - Doglio, Romano, Santillan, Torres":
    principal()
