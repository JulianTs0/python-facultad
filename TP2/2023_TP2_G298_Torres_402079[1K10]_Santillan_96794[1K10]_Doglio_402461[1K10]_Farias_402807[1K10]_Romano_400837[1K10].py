# Trabajo Practico 1 - Gestion de Cabinas de Peaje
import math


def importe_total_por_pais(patente):
    importe_base = importe_pagar_final = 0
    pais_cabina = int(patente[9])
    tipo_vehiculo = int(patente[7])
    forma_pago = int(patente[8])
    nombre_patente = patente[0:7]

    # Ticket pais de la cabina
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

    # Ticket monto a pagar segun tipo de vehiculo
    if tipo_vehiculo == 0:
        importe_basico = importe_base * 50 / 100
    elif tipo_vehiculo == 1:
        importe_basico = importe_base
    elif tipo_vehiculo == 2:
        importe_basico = importe_base + (importe_base * 60 / 100)

    # Ticket tipo de pago
    if forma_pago == 1:
        importe_pagar_final = importe_basico
    elif forma_pago == 2:
        importe_pagar_final = importe_basico - (importe_basico * 10 / 100)

    return importe_pagar_final, nombre_patente


def principal():
    archivo = open('peajes.txt', 'r')
    i = 0
    carg = cbol = cbra = cchi = cpar = curu = cotr = 0
    idioma = ''
    imp_total_arg = imp_total_chi = imp_total_bra = imp_total_bol = imp_total_par = imp_total_uru = imp_total_otr = 0
    primera = cpp = maypat = 0
    mayimp = None
    sp = se = False
    cpat_total = 0
    distancia_total = 0
    carg_bra = 0

    for line in archivo:
        i += 1
        if i == 1:
            for car in line:
                if car == 'P':
                    sp = True
                elif car == "T" and sp is True:
                    idioma = "Portugués"
                    sp = False
                else:
                    sp = False

                if car == "E":
                    se = True
                elif car == 'S' and se is True:
                    idioma = "Español"
                    se = False
                else:
                    se = False

        if i != 1:
            cpat_total += 1
            patente = line
            if patente[0].isalpha() and patente[1].isalpha() and patente[2].isnumeric() and patente[3].isnumeric() and \
                    patente[4].isnumeric() and patente[5].isalpha() and patente[6].isalpha():
                carg += 1
                importe, nombre_patente = importe_total_por_pais(patente)
                imp_total_arg += importe
                distancia = int(patente[10:13])
                pais_cabina = int(patente[9])

                if pais_cabina == 2:
                    distancia_total += distancia
                    carg_bra += 1
            elif patente[0] == ' ' and patente[1].isalpha() and patente[2].isalpha() and patente[3].isalpha() and \
                    patente[4].isalpha() and patente[5].isnumeric() and patente[6].isnumeric():
                cchi += 1
                importe, nombre_patente = importe_total_por_pais(patente)
                imp_total_chi += importe
            elif patente[0].isalpha() and patente[1].isalpha() and patente[2].isalpha() and patente[3].isnumeric() and \
                    patente[4].isalpha() and patente[5].isnumeric() and patente[6].isnumeric():
                cbra += 1
                importe, nombre_patente = importe_total_por_pais(patente)
                imp_total_bra += importe
            elif patente[0].isalpha() and patente[1].isalpha() and patente[2].isnumeric() and patente[3].isnumeric() and \
                    patente[4].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric():
                cbol += 1
                importe, nombre_patente = importe_total_por_pais(patente)
                imp_total_bol += importe
            elif patente[0].isalpha() and patente[1].isalpha() and patente[2].isalpha() and patente[3].isalpha() and \
                    patente[4].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric():
                cpar += 1
                importe, nombre_patente = importe_total_por_pais(patente)
                imp_total_par += importe
            elif patente[0].isalpha() and patente[1].isalpha() and patente[2].isalpha() and patente[3].isnumeric() and \
                    patente[4].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric():
                curu += 1
                importe, nombre_patente = importe_total_por_pais(patente)
                imp_total_uru += importe
            else:
                cotr += 1
                importe, nombre_patente = importe_total_por_pais(patente)
                imp_total_otr += importe

            importe_pagar_final, nombre_patente = importe_total_por_pais(patente)

            if mayimp is None:
                mayimp = math.trunc(importe_pagar_final)
                maypat = nombre_patente
            elif importe_pagar_final > mayimp:
                mayimp = math.trunc(importe_pagar_final)
                maypat = nombre_patente

        if i != 1 and i == 2:
            primera = line[0:7]

        if primera == line[0:7]:
            cpp += 1

    imp_acu_total = math.trunc(
        imp_total_arg + imp_total_chi + imp_total_bra + imp_total_par + imp_total_bol + imp_total_uru + imp_total_otr)
    porc = round((cotr * 100) / cpat_total, 2)
    if carg_bra != 0:
        prom = round(distancia_total / carg_bra, 2)
    else:
        prom = 0

    archivo.close()

    return idioma, carg, cbol, cbra, cchi, cpar, curu, cotr, imp_acu_total, primera, cpp, mayimp, maypat, porc, prom


idioma, carg, cbol, cbra, cchi, cpar, curu, cotr, imp_acu_total, primera, cpp, mayimp, maypat, porc, prom = principal()

print('(r1) - Idioma a usar en los informes:', idioma)
print()
print('(r2) - Cantidad de patentes de Argentina:', carg)
print('(r2) - Cantidad de patentes de Bolivia:', cbol)
print('(r2) - Cantidad de patentes de Brasil:', cbra)
print('(r2) - Cantidad de patentes de Chile:', cchi)
print('(r2) - Cantidad de patentes de Paraguay:', cpar)
print('(r2) - Cantidad de patentes de Uruguay:', curu)
print('(r2) - Cantidad de patentes de otro país:', cotr)
print()
print('(r3) - Importe acumulado total de importes finales:', imp_acu_total)
print()
print('(r4) - Primera patente del archivo:', primera, '- Frecuencia de aparición:', cpp)
print()
print('(r5) - Mayor importe final cobrado:', mayimp, '- Patente a la que se cobró ese importe:', maypat)
print()
print('(r6) - Porcentaje de patentes de otros países:', porc, '\b%')
print()
print('(r7) - Distancia promedio recorrida por vehículos argentinos pasando por cabinas brasileñas:', prom, '\bkm')
