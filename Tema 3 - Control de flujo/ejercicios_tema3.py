# -------------------- EJERCICIOS CONTROL DE FLUJO --------------------

# Ejercicio 1: Conversión Celsius a Fahrenheit
"""
Convertir una temperatura introducida por el usuario de Celsius a Fahrenheit (ºF = ºC * 9/5 + 32)
"""
celsius = float(input("Introduce la temperatura en ºC: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"{celsius} ºC son {fahrenheit:.2f} ºF")


# Ejercicio 2: Cuadrado de impares del 1 al 20
"""
Mostrar el cuadrado de los números impares de 1 a 20.
"""
for i in range(1,21):
    if i % 2 != 0:
        print(f"{i}^2 = {i ** 2}")


# Ejercicio 3: Adivinar un número del 1 al 10
"""
Definir un número del 1 al 10 que tiene que ser adivinado por el usuario.
"""
numero_secreto = 3
intento = 0
print("Adivina el número secreto (entre 1 y 10):")
while True:
    intento = int(input("Introduce tu número: "))
    if intento == numero_secreto:
        print("¡Correcto! Has adivinado el número secreto.")
        break
else:
    print("Incorrecto, intenta de nuevo.")


# Ejercicio 4: Calcular el factorial de un número del 1 al 10
"""
Calcular el factorial de un número introducido (del 1 al 10) por el usuario.
"""

factorial=1
num = int(input("Introduce un número entre 0 y 10: "))
if 0 <= num <= 10:
    i=1
    for i in range(1,num+1):
        factorial *= i
    print(f"El factorial de {num} es {factorial}.")
else:
    print("Número fuera del rango permitido.")


# Ejercicio 5: Cuenta atrás desde número positivo hasta cero
"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas en la misma línea.
"""

numero = int(input("Introduce un número entero positivo"))
if (numero > 0):
    cadena= str(numero)
    while (numero>0):
        numero -= 1
        cadena += "," + str(numero)         
    print (f"{cadena}")
else:
    print("Número fuera del rango permitido.")

# otra versión:
n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1):
    end_char = ", " if i != 0 else "\n"
    print(i, end=end_char)


# Ejercicio 6: Inversión con interés compuesto
"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""

inversion = int(input("¿Cuánto quiere invertir?"))
interes =   int(input("¿Cuál es el interés (%)"))
años = int(input("¿Cuántos años durará la inversión?"))
i=1
capital = inversion
while (i<=años):
    capital += (capital * interes / 100)
    print(f"Después del año {i}, obtendrá un capital de {round(capital,2)} euros.")
    i += 1

# otra versión:
capital = float(input("Cantidad a invertir: "))
interes = float(input("Interés anual (en %): "))
años = int(input("Número de años: "))
for i in range(1, años + 1):
    capital *= (1 + interes / 100)
    print(f"Año {i}: capital acumulado = {capital:.2f} €")


# Ejercicio 7: Tabla de multiplicar del 1 al 10
"""
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
"""

i=1
for i in range(1,11):
    j=1
    cadena=""
    for j in range(1,11):
        cadena += str(i) + "x" + str(j) + "=" + str(i*j) + " "
    print(f'{cadena}')

# otra versión:
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("-")


# Ejercicio 8: Comprobar si un número es primo
"""
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
"""

numero = int(input("Introduce un número entero: "))
for i in range(1,numero+1):
        if ((1<i<numero) and ((numero % i) == 0)):
            print(f"El número {numero} no es primo.")
            break;
else: 
    print(f"El número {numero} es primo.")


# otra versión:
n = int(input("Introduce un número entero: "))
if n < 2:
    print(f"{n} no es primo")
else:
    es_primo = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{n} es un número primo")
    else:
        print(f"{n} no es un número primo")