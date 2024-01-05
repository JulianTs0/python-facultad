#Trabajo Practico 1 - Gestion de Cabinas de Peaje
print('Gestion de Cabinas de Peaje\n')

#Datos
monto_peaje = 0

print('Por favor ingrese los siguientes datos:\n1) Código de patente del vehiculo (todo en mayúscula y sin espacios en blanco)')

patente = input('Ingrese el código de patente: ')

longitud_patente = len(patente)

if longitud_patente == 7:
    bandera = True
else:
    bandera = False

print('\n2) Tipo de vehiculo (elija una opción)\n0 - motocicleta \n1 - automóvil \n2 - camión')

tipo_vehiculo = int(input('Ingrese la opción elegida: '))

print('\n3) Forma de pago (elija una opción)\n1 - manual \n2 - telepeaje')

forma_pago = int(input('Ingrese la opción elegida: '))

print('\n4) Pais de la cabina de peaje (elija una opción)\n0 - Argentina \n1 - Bolivia \n2 - Brasil \n3 - Paraguay \n4 - Uruguay')

pais_cabina = int(input('Ingrese la opción elegida: '))

print('\n5) Distancia recorrida por el vehiculo desde la ultima cabina de peaje (en kilometros)\nSi esta es su primera cabina, por favor ingrese el valor 0 (cero)')

distancia = float(input('Ingrese la distancia recorrida (km): '))

#Procesos
if patente[0].isalpha() and patente[1].isalpha() and patente[2].isnumeric() and patente[3].isnumeric() and patente[4].isnumeric() and patente[5].isalpha() and patente[6].isalpha() and bandera:
    #Ticket pais del vehiculo
    pais_vehiculo = "Argentina"
elif patente[0].isalpha() and patente[1].isalpha() and patente[2].isalpha() and patente[3].isnumeric() and patente[4].isalpha() and patente[5].isnumeric() and patente[6].isnumeric() and bandera:
    #Ticket pais del vehiculo
    pais_vehiculo = "Brasil"
elif patente[0].isalpha() and patente[1].isalpha() and patente[2].isnumeric() and patente[3].isnumeric() and patente[4].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric() and bandera:
    #Ticket pais del vehiculo
    pais_vehiculo = "Bolivia"
elif patente[0].isalpha() and patente[1].isalpha() and patente[2].isalpha() and patente[3].isalpha() and patente[4].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric() and bandera:
    #Ticket pais del vehiculo
    pais_vehiculo = "Paraguay"
elif patente[0].isalpha() and patente[1].isalpha() and patente[2].isalpha() and patente[3].isnumeric() and patente[4].isnumeric() and patente[5].isnumeric() and patente[6].isnumeric() and bandera:
    #Ticket pais del vehiculo
    pais_vehiculo = "Uruguay"
else:
    # Ticket pais del vehiculo
    pais_vehiculo = "Otro"

#Ticket pais de la cabina
if pais_cabina == 0:
    monto_peaje = 300
elif pais_cabina == 1:
    monto_peaje = 200
elif pais_cabina == 2:
    monto_peaje = 400
elif pais_cabina == 3:
    monto_peaje = 300
elif pais_cabina == 4:
    monto_peaje = 300

#Ticket monto a pagar segun tipo de vehiculo
if tipo_vehiculo == 0:
    importe_pagar_vehiculo = monto_peaje * 50/100
elif tipo_vehiculo == 1:
    importe_pagar_vehiculo = monto_peaje
elif tipo_vehiculo == 2:
    importe_pagar_vehiculo = monto_peaje + (monto_peaje * 60/100)

#Ticket tipo de pago
if forma_pago == 1:
    forma_pago = "manual"
    importe_pagar_final = importe_pagar_vehiculo
elif forma_pago == 2:
    forma_pago = "telepeaje"
    importe_pagar_final = importe_pagar_vehiculo - (importe_pagar_vehiculo * 10/100)

#Ticket distancia
if distancia != 0:
    valor_promedio = monto_peaje / distancia
    valor_promedio_final = round(valor_promedio, 2)
else:
    valor_promedio_final = "0 (es la primera cabina que atraviesa)"

print('\nAqui tiene su ticket:\nPais del vehiculo:', pais_vehiculo, '\nMonto a pagar por tipo de vehiculo:', importe_pagar_vehiculo, '\nMonto final a pagar:', importe_pagar_final, '\nValor promedio por cantidad de km:', valor_promedio_final)
