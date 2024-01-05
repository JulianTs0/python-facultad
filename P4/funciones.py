from clase import *
from pickle import *
from os.path import *
import random


def menu():
    print("\nMenu de opciones")
    print("1. Cargar vector")
    print("2. Mostrar vector")
    print("3. Determinar stock")
    print("4. Generar archivo")
    print("5. Mostrar archivo")
    print("0. Cargar vector")


def validar_n():
    n = int(input("\nIngrese la cantidad de pantalones a cargar: "))
    while n <= 0:
        n = int(input("Ingrese una cantidad VALIDA de pantalones a cargar: "))
    return n


def add_in_order(elem, vec):
    n = len(vec)
    pos = n
    izq, der = 0, n - 1

    while izq <= der:
        c = (izq + der) // 2
        if vec[c].codigo == elem.codigo:
            pos = c
            break
        elif vec[c].codigo < elem.codigo:
            izq = c + 1
        else:
            der = c - 1

    if izq > der:
        pos = izq

    vec[pos:pos] = [elem]


def auto_load():
    vec = []
    n = validar_n()
    nombres = ("Acu", "Lit", "San", "Jed", "Ror", "Lar", "Pir", "Nan", "Las", "Boba", "Lir", "Sit")

    for i in range(n):
        codigo = random.randint(1, 1000000)
        nombre = random.choice(nombres)
        largo = random.randint(30, 50)
        cintura = random.randint(30, 50)
        tela = random.randint(1, 3)
        stock = random.randint(0, 100)
        pantalon = Pantalon(codigo, nombre, largo, cintura, tela, stock)
        add_in_order(pantalon, vec)

    print("\nVector cargado...")
    return vec


def show_vec(vec):
    print("")
    for i in vec:
        print(i)


def create_matrix(vec):
    mat = [[0] * 21 for i in range(21)]
    for i in vec:
        mat[i.largo - 30][i.cintura - 30] += i.stock
    return mat


def show_matrix(vec):
    mat = create_matrix(vec)
    u = int(input("\nIngrese un maximo de stock para mostrar: "))
    while u < 0:
        u = int(input("Ingrese un maximo VALIDO de stock para mostrar: "))

    for i in range(len(mat)):
        print(f"\nStock de los pantalones con largo {i + 30}: ")
        for j in range(len(mat[i])):
            if mat[i][j] > u:
                print(f"Y con cintura {j + 30} : {mat[i][j]}")


def create_file(vec):
    binario = open("pantalones.dat", "wb")
    t = int(input("\nIngrese una tela para crear el archivo: "))
    while t < 1 or t > 3:
        t = int(input("Ingrese una tela VALIDA para crear el archivo: "))

    for i in vec:
        if i.stock > 0 and i.tela == t:
            dump(i, binario)

    binario.close()

    print("\nArchivo creado...")


def show_file():
    if not exists("pantalones.dat"):
        print("\nNo existe ningun archivo para poder mostrar")
        return

    tot = stt = promedio = 0

    binario = open("pantalones.dat", "rb")
    tamanio = getsize("pantalones.dat")

    print()
    while binario.tell() < tamanio:
        tot += 1
        pantalon = load(binario)
        stt += pantalon.stock
        print(pantalon)

    binario.close()

    if tot != 0:
        promedio = stt // tot

    print(f"\nEl stock promedio de los pantalones del archivo es : {promedio}")
