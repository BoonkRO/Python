
def eje1():
    print("¿Cuanto cobras? ")
    sueldo = int(input())

    def retencion(x):
        i = (x * 0.2)
        z = x - i
        print("En realidad cobras ", z)

    retencion(sueldo)


def eje2y3():
    import math

    print("Introduce un número: ")

    radio = int(input())

    longitud = (radio * 2) * math.pi
    area = (radio * radio) * math.pi

    print("La longitud es: ", longitud)
    print("El area es: ", area)


def eje4():
    print("Introduce altura: ")
    altura = int(input())

    print("Introduce ancho: ")
    ancho = int(input())

    area = altura * ancho
    perimetro = (altura * 2) + (ancho * 2)

    print(area)

    print(perimetro)


def eje5():
    print("¿Cuanto cobras? ")
    sueldo = int(input())

    def retencion(x):
        i = (x * 0.2)
        z = x - i
        print("En realidad cobras ", z)

    retencion(sueldo)


def eje6():
    print("Primer valor: ")
    v1 = int(input())
    print("Segundo valor: ")
    v2 = int(input())

    print("v1 vale: ", v1)
    print("v2 vale: ", v2)

    z = v2
    v2 = v1
    v1 = z

    print("Ahora v1 vale: ", v1)
    print("Ahora v2 vale: ", v2)


def eje7():
    print("Introduce un numero: ")
    numero = int(input())

    if numero<0:
        print("El numero leido es negativo.")
    else:
        print("El numero leido es positivo")


def eje8():
    print("Primer numero: ")
    n1 = int(input())
    print("Segundo numero: ")
    n2 = int(input())
    if n1==n2:
        print("Ambos numeros tienen el mismo valor,", n1)
    elif n1>n2:
        print("El primer valor,", n1, "es mayor que el segundo, ", n2)
    else:
        print("El segundo valor,", n2, "es mayor que el primero, ", n1)


def eje9y10():
    print("Primer numero: ")
    n1 = int(input())
    print("Segundo numero: ")
    n2 = int(input())

    if n1>=0 and n2>=0:
        print("La suma de los dos numeros es", n1+n2)
    elif n1<0 and n2>=0:
        print("No se calcula la suma porque el primer numero es negatvo. ")
    elif n1>=0 and n2<0:
        print("No se calcula la suma porque el segundo numero es negativo. ")
    else:
        print("No se calcula la suma porque los dos numeros son negativos ")


def eje11():
    print("Primer numero: ")
    n1 = int(input())
    print("Segundo numero: ")
    n2 = int(input())
    print("Tercer numero: ")
    n3 = int(input())

    if n1<0 or n2<0 or n3<0:
        print("Los numeros no cumplen la condicion.")
    else:
        if n1 + n2 == n3:
            print("Numero introducidos", n1, n2, n3)
            print("Se cumple que:", n3, "=", n1, "+", n2)
        if n2 + n3 == n1:
            print("Numero introducidos", n1, n2, n3)
            print("Se cumple que:", n1, "=", n2, "+", n3)
        if n3 + n1 == n2:
            print("Numero introducidos", n1, n2, n3)
            print("Se cumple que:", n2, "=", n1, "+", n3)
    print("Los numeros no cumplen las condiciones.")


def eje12():
    print("Primer numero: ")
    n1 = int(input())
    print("Segundo numero: ")
    n2 = int(input())

    if n1%2 != 0 or n2%2 != 0:
        print("ERROR:¡Los numeros no cumplen las condiciones!")
    else:
        if n1<50 and n2>99 and n2<501:
            print("La suma es", n1+n2)
        else:
            print("ERROR!:¡Los numeros no cumplen las condiciones!")


def eje13():
    print("Valor de la venta: ")
    vprinc = int(input())

    if vprinc<=20:
        print("Cantidad a pagar:", vprinc, "(no hay descuento)")
    else:
        if vprinc>20 and vprinc<=100:
            pagoFinal = vprinc * 0.95
            print("Cantidad a pagar:", pagoFinal, "(5% descuento)")
        else:
            pagoFinal = vprinc * 0.9
            print("Cantidad a pagar:", pagoFinal, "(10% descuento)")


def eje14():
    print("Valor de la venta: ")
    cantidad = int(input())
    dinero = [[100, 0], [50, 0], [20, 0], [10, 0], [5, 0], [2, 0], [1, 0]]
    pos = 0
    while cantidad != 0:
        cantidad = cantidad - dinero[pos][0]
        if cantidad < 0:
            cantidad = cantidad + dinero[pos][0]
            pos += 1

        else:
            dinero[pos][1] += 1

    index = 0
    for valor in dinero:
        print(dinero[index][1], " billetes de ", dinero[index][0])
        index += 1


eje14()
