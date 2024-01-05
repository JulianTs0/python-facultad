from clases import *
import random


def valid_n(n):
    while n <= 0:
        n = int(input("Ingrese un valor valido: "))
    return n


def auto_load():
    vec = []

    n = int(input("\nIngrese la cantidad de vectores a cargar: "))
    n = valid_n(n)

    for i in range(n):
        codigo = random.randint(1, 100000)
        nombre = "Nombre " + str(random.randint(1, 50))
        servicio = random.randint(1, 10)
        importe = round(random.uniform(10, 1000), 2)
        servicio = Servicio(codigo, nombre, servicio, importe)
        vec.append(servicio)

    print("Vector cargado...")
    return vec


def sort_cod(vec):
    n = len(vec)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if vec[i].codigo > vec[j].codigo:
                vec[i], vec[j] = vec[j], vec[i]


def show_vec(vec):
    sort_cod(vec)
    acu = 0

    i1 = int(input("\nIngrese el extremo izquierdo del rango de importe: "))
    while i1 < 0:
        i1 = int(input("Ingrese un extremo izquierdo valido del rango de importe: "))
    i2 = int(input("Ingrese el extremo derecho del rango de importe: "))
    while i2 < 0 or i2 < i1:
        i2 = int(input("Ingrese un extremo derecho valido del rango de importe: "))

    print("\nEl listado de importes en el rango seleccionado es: ")
    for i in vec:
        if i1 <= i.importe <= i2:
            print(i)
            acu += 1

    print(f"\nLa cantidad de servicios mostrados fueron: {acu}")


def by_type(vec):
    vec_acu = 10 * [0]

    for i in vec:
        vec_acu[i.servicio - 1] += 1

    print("\nListado de servicios por tipo")
    for j in range(len(vec_acu)):
        if vec_acu[j] != 0:
            print(f"Cantidad de servicios del tipo {j+1} : {vec_acu[j]}")


def search_name(vec):
    nom = input("\nIngrese el nombre del cliente a buscar: ")

    for i in vec:
        if i.nombre == nom:
            print(f"\nServicio encontrado.\nSe modifico el servicio sumandole 2000 al importe:")
            i.importe += 2000
            print(i)
            return

    print("\nNo existe ningun cliente con ese nombre")