def caract(char):
    if char in "AEIOUaeiou":
        return 1
    elif char in "0123456789":
        return 2
    else:
        return 3


def principal():
    file = open("entrada.txt")
    texto = file.read()
    file.close()

    i = p = p2 = cons4 = vocal3 = 0
    ultchar = 0
    dig = hayvocal = hayd = hayde = hayt = False
    r1 = r2 = r3 = r4 = 0

    for car in texto:
        if car == " " or car == ".":
            p += 1

            # Punto 1
            if dig and cons4 >= 2:
                r1 += 1

            # Punto 2
            if hayvocal and caract(ultchar) == 2:
                p2 += 1

            # Punto 3
            if i >= 4 and vocal3 == 3:
                r3 += 1

            # Punto 4
            if hayde and hayt:
                r4 += 1

            dig = hayvocal = hayd = hayde = hayt = False
            ultchar = 0
            i = cons4 = vocal3 = 0
        else:
            i += 1

            # Punto 1
            if (i == 2 or i == 3) and caract(car) == 2:
                dig = True

            # Punto 2
            if caract(car) == 1:
                hayvocal = True

            if i >= 4 and caract(car) == 3:
                cons4 += 1

            # Punto 3
            if i == 1 and caract(car) == 1:
                vocal3 += 1
            elif i == 2 and caract(car) == 1:
                vocal3 += 1
            elif i == 3 and caract(car) == 1:
                vocal3 += 1

            # Punto 4
            if car in "Dd":
                hayd = True
            elif hayd and car in "Ee":
                hayd = False
                hayde = True
            elif hayde and car == "t":
                hayt = True
            else:
                hayd = False

            ultchar = car

    # Punto 2
    if p != 0:
        r2 = (p2 * 100) // p

    print("Primer resultado:", r1)
    print("Segundo resultado:", r2)
    print("Tercer resultado:", r3)
    print("Cuarto resultado:", r4)


if __name__ == "__main__":
    principal()
