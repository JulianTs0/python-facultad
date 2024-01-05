__name__ = "TP4AED - Doglio, Romano, Santillan, Torres"

from funciones import *
import os.path


def principal():
    op = 1

    while op != "0":
        mostrar_menu()
        op = input("Ingrese una opción: ")
        existe = os.path.exists("archivo_binario.dat")

        if op == "1":
            crear_archivo("peajes-tp4.csv")
        elif op == "2" and existe:
            cargar_datos("archivo_binario.dat")
        elif op == "3" and existe:
            mostrar_datos("archivo_binario.dat")
        elif op == "4" and existe:
            buscar_patente("archivo_binario.dat")
        elif op == "5" and existe:
            buscar_codigo("archivo_binario.dat")
        elif op == "6" and existe:
            mostrar_vehiculo_cabina("archivo_binario.dat")
        elif op == "7" and existe:
            mostrar_filas_columnas_matriz("archivo_binario.dat")
        elif op == "8" and existe:
            promedio_distancia("archivo_binario.dat")
        elif op == "0":
            print("Fin del programa")
        elif op not in "012345678":
            print("Error, ingrese una opción válida")
        else:
            print("Error, cargue el archivo binario antes de usar cualquier opción")


if __name__ == "TP4AED - Doglio, Romano, Santillan, Torres":
    principal()
