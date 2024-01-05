paises = ("Argentina", "Chile", "Brasil", "Bolivia", "Paraguay", "Uruguay", "Otro")
letras = "abcdefghojklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZáéíóúÁÉÍÓÚ"
minusculas = "abcdefghojklmnñopqrstuvwxyzáéíóú"


class Ticket:
    def __init__(self, id_ticket, patente, tipo, pago, pais, km):
        self.id = id_ticket
        self.patente = patente
        self.tipo = tipo
        self.pago = pago
        self.pais = pais
        self.km = km

    def __str__(self):
        return f"Identificador:{self.id},Patente:{self.patente},Tipo de vehículo:{self.tipo},Forma de pago:{self.pago},País de cabina:{self.pais},Km recorridos:{self.km}"


def es_letra(palabra):
    switch = False

    for i in palabra:
        if i in letras:
            switch = True

    return switch


def es_minuscula(palabra):
    switch = False

    for i in palabra:
        if i in minusculas:
            switch = True

    return switch


def mostrar_menu():
    print("\nMenú de opciones")
    print("1 - Cargar arreglo")
    print("2 - Cargar datos de un ticket")
    print("3 - Mostrar todos los registros del arreglo")
    print("4 - Buscar si existe en el arreglo un registro cuya patente sea igual a p y que haya pasado por una cabina del país x")
    print("5 - Buscar si existe en el arreglo un registro cuyo código de ticket sea igual a c")
    print("6 - Determinar la cantidad de vehículos de cada país que pasaron por las cabinas")
    print("7 - Determinar el importe acumulado por pagos de tickets")
    print("8 - Determinar y mostrar cual fue el tipo de vehículo con mayor monto acumulado")
    print("9 - Calcular y mostrar la distancia promedio desde la última cabina")
    print("0 - Salir")


def cargar_arreglo(vec_main, peajes):
    vec = []
    if vec_main:
        opcion = input("Esta a punto de crear un nuevo arreglo\n¿Desea eliminar el anterior arreglo? s/n: ")
    else:
        opcion = "s"

    if opcion in "Ss":
        archivo = open(peajes)
        texto_peajes = archivo.readlines()
        archivo.close()
        i = 0

        for line in texto_peajes:
            i += 1
            if i != 1:
                patente = line
                id_ticket = patente[0:10]
                nombre_patente = patente[10:17]
                tipo_vehiculo = patente[17]
                forma_pago = patente[18]
                pais_cabina = patente[19]
                distancia = patente[20:23]

                ticket = Ticket(id_ticket, nombre_patente, tipo_vehiculo, forma_pago, pais_cabina, distancia)
                vec.append(ticket)
        return vec
    else:
        print("Operacion cancelada")
        return vec_main


def cargar_datos(vector):
    n = input("Ingrese la cantidad de patentes para añadir: ")
    while (n in letras) or (int(n) < 0):
        n = input("Ingrese la cantidad de patentes para añadir, que sea mayor a cero: ")

    for i in range(int(n)):
        id_cargado = input("Ingrese el código identificador del ticket (código de 10 digitos): ")

        while len(id_cargado) != 10 or es_letra(id_cargado):
            id_cargado = input("Error, dato ingresado incorrecto\nIngrese el código identificador del ticket (código de 10 digitos): ")

        patente_cargada = input("Ingrese la patente (código de 7 digitos): ")
        while len(patente_cargada) != 7 or es_minuscula(patente_cargada):
            patente_cargada = input("Error, dato ingresado incorrecto\nIngrese la patente (código de 7 digitos): ")

        tipo_cargado = input("Ingrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): ")
        while len(tipo_cargado) != 1 or not (tipo_cargado in "012"):
            tipo_cargado = input("Error, dato ingresado incorrecto\nIngrese el tipo de vehículo (0: motocicleta, 1: automóvil, 2: camión): ")

        pago_cargado = input("Ingrese el tipo de pago (1: manual, 2 telepeaje): ")
        while len(pago_cargado) != 1 or not (pago_cargado in "12"):
            pago_cargado = input("Error, dato ingresado incorrecto\nIngrese tipo de pago (1: manual, 2 telepeaje): ")

        pais_cargado = input("Ingrese el pais de la cabina (0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay): ")
        while len(pais_cargado) != 1 or not (pais_cargado in "01234"):
            pais_cargado = input("Error, dato ingresado incorrecto\nIngrese el pais de la cabina (0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay): ")

        km_cargado = input("Ingrese el kilometraje desde la ultima cabina de peaje (ingrese 3 digitos o 0 si es la primera cabina por la que pasa el vehiculo): ")
        while len(km_cargado) > 3 or es_letra(km_cargado):
            km_cargado = input("Error, dato ingresado incorrecto\nIngrese el kilometraje desde la ultima cabina de peaje (ingrese 3 digitos o 0 si es la primera cabina por la que pasa el vehiculo): ")

        ticket = Ticket(id_cargado, patente_cargada, tipo_cargado, pago_cargado, pais_cargado, km_cargado)
        vector.append(ticket)


def mostrar_datos(vec):
    n = len(vec)
    print("Registros del arreglo: ")
    for i in range(n):
        pais_patente = pais_de_patente(vec[i].patente)
        print(f"{vec[i]}, País de patente: {paises[pais_patente]}")


def ordenar_menor_mayor(vec):
    n = len(vec)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if vec[i].id > vec[j].id:
                vec[i], vec[j] = vec[j], vec[i]


def pais_de_patente(patente):
    if patente[0].isalpha() and patente[1].isalpha() and patente[2].isnumeric() and patente[3].isnumeric() and patente[4].isnumeric() and patente[5].isalpha() and patente[6].isalpha():
        pais_patente = 0  # Argentina
    elif patente[0] == ' ' and patente[1].isalpha() and patente[2].isalpha() and patente[3].isalpha() and patente[4].isalpha() and patente[5].isnumeric() and patente[6].isnumeric():
        pais_patente = 1  # Chile
    elif patente[0].isalpha() and patente[1].isalpha() and patente[2].isalpha() and patente[3].isnumeric() and patente[4].isalpha() and patente[5].isnumeric() and patente[6].isnumeric():
        pais_patente = 2  # Brasil
    elif patente[0].isalpha() and patente[1].isalpha() and patente[2].isnumeric() and patente[3].isnumeric() and patente[4].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric():
        pais_patente = 3  # Bolivia
    elif patente[0].isalpha() and patente[1].isalpha() and patente[2].isalpha() and patente[3].isalpha() and patente[4].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric():
        pais_patente = 4  # Paraguay
    elif patente[0].isalpha() and patente[1].isalpha() and patente[2].isalpha() and patente[3].isnumeric() and patente[4].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric():
        pais_patente = 5  # Uruguay
    else:
        pais_patente = 6  # Otro

    return pais_patente


def buscar_penpaisx(vec):
    n = len(vec)
    busqueda_patente = input("Ingrese la patente a buscar: ")
    while len(busqueda_patente) != 7 or es_minuscula(busqueda_patente):
        busqueda_patente = input("Error, dato ingresado incorrecto\nIngrese la patente: ")
    busqueda_pais = input("Ingrese el país de la cabina a buscar (0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay): ")
    while len(busqueda_pais) != 1 or not (busqueda_pais in "01234"):
        busqueda_pais = input("Error, dato ingresado incorrecto\nIngrese el país de la cabina a buscar (0: Argentina - 1: Bolivia - 2: Brasil - 3: Paraguay - 4: Uruguay): ")

    for i in range(n):
        if vec[i].patente == busqueda_patente and vec[i].pais == busqueda_pais:
            print("Se encontró la patente:\n", vec[i])
            return None
    print("No se encontró el valor buscado")


def buscar_ticket(vec):
    n = len(vec)
    c = input("Ingrese el código de ticket a buscar: ")
    while len(c) != 10 or es_letra(c):
        c = input("Error, dato ingresado incorrecto\nIngrese el código identificador del ticket: ")

    for i in range(n):
        if vec[i].id == c:
            if vec[i].pago == "1":
                vec[i].pago = "2"
            elif vec[i].pago == "2":
                vec[i].pago = "1"
            print("Registro encontrado y modificado:\n", vec[i])
            return None
    print("No se encontró el valor buscado")


def cantidad_patentes(vec):
    vector_conteo = 7 * [0]
    for i in range(len(vec)):
        pais_patente = pais_de_patente(vec[i].patente)
        vector_conteo[pais_patente] += 1

    print("Cantidad de vehículos por país:")
    for i in range(7):
        print(f"{paises[i]}:{vector_conteo[i]}")


def importe_patente(vec):
    importe_base = importe_basico = importe_pagar_final = 0
    acumulador_importe = 3 * [0]

    for i in vec:
        pais_cabina = int(i.pais)
        tipo_vehiculo = int(i.tipo)
        forma_pago = int(i.pago)

        if pais_cabina == 0:
            importe_base = 300
        elif pais_cabina == 1:
            importe_base = 200
        elif pais_cabina == 2:
            importe_base = 400
        elif pais_cabina == 3:
            importe_base = 300
        elif pais_cabina == 4:
            importe_base = 300

        if tipo_vehiculo == 0:
            importe_basico = importe_base * 50 / 100
        elif tipo_vehiculo == 1:
            importe_basico = importe_base
        elif tipo_vehiculo == 2:
            importe_basico = importe_base + (importe_base * 60 / 100)

        if forma_pago == 1:
            importe_pagar_final = importe_basico
        elif forma_pago == 2:
            importe_pagar_final = importe_basico - (importe_basico * 10 / 100)

        acumulador_importe[tipo_vehiculo] += importe_pagar_final

    return acumulador_importe


def mayor_acu(acu):
    mayor = None
    index = 0
    acumulador_montos = 0
    porcentaje = 0

    for i in range(len(acu)):
        acumulador_montos += acu[i]
        if mayor is None:
            mayor = acu[i]
            index = i
        elif mayor < acu[i]:
            mayor = acu[i]
            index = i

    if acumulador_montos != 0:
        porcentaje = round(((mayor * 100) / acumulador_montos), 2)

    print(f"El tipo de vehículo {index} es el de mayor monto, con un monto de {mayor} y representa el {porcentaje}% del total acumulado")


def promedio_distancia(vec):
    distancia_total = 0
    promedio = 0
    acumulador_mayor = 0

    for i in vec:
        distancia_total += int(i.km)

    if vec:
        promedio = round(distancia_total / len(vec), 2)

    for i in vec:
        if int(i.km) > promedio:
            acumulador_mayor += 1

    print(f"La distancia promedio recorrida fue de {promedio} km y la cantidad de autos en superarla fue de {acumulador_mayor}")
