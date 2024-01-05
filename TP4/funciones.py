from clase import *
import os.path
import pickle


def mostrar_menu():
    print("\nMenú de opciones")
    print("1 - Crear archivo binario con datos de ticket")
    print("2 - Cargar manualmente datos de ticket")
    print("3 - Mostrar todos los datos del archivo binario")
    print("4 - Buscar tickets por patente en el archivo binario")
    print("5 - Buscar tickets por código en el archivo binario")
    print("6 - Determinar y mostrar la combinacion de la cantidad de vehículos por tipo de vehículo y país de cabina")
    print("7 - Mostrar la cantidad de vehiculos por tipo y por cabina")
    print("8 - Calcular y mostrar la distancia promedio de los tickets del archivo binario")
    print("0 - Salir")


def es_letra(palabra):
    switch = False
    letras = "abcdefghojklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ"

    for i in palabra:
        if i in letras:
            switch = True

    return switch


def es_minuscula(palabra):
    minusculas = "abcdefghojklmnñopqrstuvwxyzáéíóú"
    switch = False

    for i in palabra:
        if i in minusculas:
            switch = True

    return switch


def shell_sort(vec):
    n = len(vec)
    h = 1
    while h <= n // 9:
        h = 3 * h + 1
    while h > 0:
        for j in range(h, n):
            y = vec[j]
            k = j - h
            while k >= 0 and y.km < vec[k].km:
                vec[k + h] = vec[k]
                k -= h
            vec[k + h] = y
        h //= 3


def obtener_ticket(line):
    codigo = line[0]
    patente = line[1]
    tipo_vehiculo = line[2]
    forma_pago = line[3]
    pais_cabina = line[4]
    distancia = line[5]
    ticket = Ticket(codigo, patente, tipo_vehiculo, forma_pago, pais_cabina, distancia)
    return ticket


def obtener_texto(ruta):
    archivo = open(ruta, "rt")
    texto = archivo.readlines()
    archivo.close()
    return texto


def aniadir_binario(obj, archivo):
    archivo = open(archivo, "ab")
    pickle.dump(obj, archivo)
    archivo.close()


def crear_archivo(archivo):
    i = 0

    if os.path.exists(archivo):
        op = input("Estas apunto de crear un archivo nuevo, quieres eliminar el anterior? S/N: ")
        while op not in "SsNn":
            op = input("Error, ingrese S/N: ")
        if op in "Nn":
            return
    else:
        print("ERROR, El archivo seleccionado no existe")
        return

    texto = obtener_texto(archivo)

    archivob = open("archivo_binario.dat", "wb")
    for line in texto:
        i += 1
        if line[-1] == "\n":
            line = line[:-1]
        line = line.split(",")
        if i > 2:
            ticket = obtener_ticket(line)
            pickle.dump(ticket, archivob)
    archivob.close()


def cargar_datos(archivo):
    n = input("Ingrese la cantidad de patentes para añadir: ")
    while (es_letra(n)) or (int(n) < 0):
        n = input("Ingrese la cantidad de patentes para añadir (que sea mayor a cero): ")

    for i in range(int(n)):
        id_cargado = input("Ingrese el código identificador del ticket (un número y mayor a 0): ")
        while id_cargado <= "0" or es_letra(id_cargado):
            id_cargado = input(
                "Error, dato ingresado incorrecto\nIngrese el código identificador del ticket (un número y mayor a 0): ")

        patente_cargada = input("Ingrese la patente: ")
        while es_minuscula(patente_cargada):
            patente_cargada = input("Error, dato ingresado incorrecto\nIngrese la patente (con letras en mayúscula): ")

        tipo_cargado = input("Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): ")
        while len(tipo_cargado) != 1 or not (tipo_cargado in "012"):
            tipo_cargado = input("Error, dato ingresado incorrecto\n"
                                 "Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): ")

        pago_cargado = input("Ingrese el tipo de pago (1: manual, 2 telepeaje): ")
        while len(pago_cargado) != 1 or not (pago_cargado in "12"):
            pago_cargado = input("Error, dato ingresado incorrecto\nIngrese tipo de pago (1: manual, 2 telepeaje): ")

        pais_cargado = input(
            "Ingrese el pais de la cabina (0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay): ")
        while len(pais_cargado) != 1 or not (pais_cargado in "01234"):
            pais_cargado = input("Error, dato ingresado incorrecto\n"
                                 "Ingrese el pais de la cabina (0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - "
                                 "4: Uruguay): ")

        km_cargado = input("Ingrese el kilometraje desde la última cabina de peaje "
                           "(ingrese 3 dígitos o 0 si es la primera cabina por la que pasa el vehículo): ")
        while len(km_cargado) > 3 or es_letra(km_cargado):
            km_cargado = input("Error, dato ingresado incorrecto\n"
                               "Ingrese el kilometraje desde la última cabina de peaje "
                               "(ingrese 3 dígitos o 0 si es la primera cabina por la que pasa el vehículo): ")

        ticket = Ticket(id_cargado, patente_cargada, tipo_cargado, pago_cargado, pais_cargado, km_cargado)
        aniadir_binario(ticket, archivo)


def mostrar_datos(archivo):
    binario = open(archivo, 'rb')
    tamanio = os.path.getsize(archivo)

    while binario.tell() < tamanio:
        ticket = pickle.load(binario)
        print(ticket)
        print()

    binario.close()


def buscar_patente(archivo):
    binario = open(archivo, "rb")
    tamanio = os.path.getsize(archivo)
    cant_patentes = 0

    patente = input("Ingrese la patente a buscar: ")
    while es_minuscula(patente):
        patente = input("Error, dato ingresado incorrecto\nIngrese la patente a buscar: ")

    print(f"Las pantentes iguales a {patente} son:")
    while binario.tell() < tamanio:
        ticket = pickle.load(binario)
        if ticket.patente == patente:
            cant_patentes += 1
            print(ticket)

    binario.close()

    print(f"Cantidad de patentes: {cant_patentes}")


def buscar_codigo(archivo):
    binario = open(archivo, "rb")
    tamanio = os.path.getsize(archivo)

    codigo = input("Ingrese el código a buscar: ")
    while codigo <= "0":
        codigo = input("Error, dato ingresado incorrecto\nIngrese el código a buscar: ")

    while binario.tell() < tamanio:
        ticket = pickle.load(binario)
        if ticket.codigo == codigo:
            print(f"El registro con el código {codigo} es:")
            print(ticket)
            binario.close()
            return

    binario.close()
    print("No se ha encontrado el registro deseado")


def generar_vehiculo_cabina(archivo):
    binario = open(archivo, "rb")
    tamanio = os.path.getsize(archivo)
    mat = [[0] * 3 for i in range(5)]

    while binario.tell() < tamanio:
        ticket = pickle.load(binario)
        mat[int(ticket.pais)][int(ticket.tipo)] += 1

    binario.close()
    return mat


def mostrar_vehiculo_cabina(archivo):
    paises = ("Argentina", "Chile", "Brasil", "Bolivia", "Paraguay", "Uruguay", "Otro")
    vehiculos = ("motocicleta", "automóvil", "camión")
    mat = generar_vehiculo_cabina(archivo)
    for i in range(5):
        print(f"\nTipos de vehículos de {paises[i]}: ")
        for j in range(3):
            if mat[i][j] != 0:
                print(f"Cantidad de vehículos tipo {vehiculos[j]}: {mat[i][j]}")


def mostrar_filas_columnas_matriz(archivo):
    p = ("Argentina", "Chile", "Brasil", "Bolivia", "Paraguay", "Uruguay", "Otro")
    v = ("motocicleta", "automóvil", "camión")
    mat = generar_vehiculo_cabina(archivo)
    vehiculos = 3 * [0]
    paises = 5 * [0]

    for i in range(5):
        for j in range(3):
            paises[i] += mat[i][j]
            vehiculos[j] += mat[i][j]

    for auto in range(len(vehiculos)):
        print(f"Cantidad de vehículos tipo {v[auto]}: {vehiculos[auto]}")

    for pais in range(len(paises)):
        print(f"Cantidad de vehículos de {p[pais]}: {paises[pais]}")


def promedio_distancia(archivo):
    binario = open(archivo, "rb")
    tamanio = os.path.getsize(archivo)
    distancia_total = acu_tick = promedio = 0
    vec_acu = []

    while binario.tell() < tamanio:
        ticket = pickle.load(binario)
        distancia_total += int(ticket.km)
        acu_tick += 1

    binario.close()

    if acu_tick > 0:
        promedio = round(distancia_total / acu_tick, 2)

    binario = open(archivo, "rb")

    while binario.tell() < tamanio:
        ticket = pickle.load(binario)
        if int(ticket.km) > promedio:
            vec_acu.append(ticket)

    binario.close()

    shell_sort(vec_acu)

    for i in vec_acu:
        print(i)

    print("La distancia promedio desde la última cabina recorrida es:", promedio)
