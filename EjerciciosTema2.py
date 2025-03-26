""" Ejercicio 1: Operaciones básicas con enteros. Escribe un programa que: 
- Pida al usuario dos números enteros. 
- Muestre la suma, resta, multiplicación y división entera de los dos números.
"""

def operaciones(numero1=None, numero2=None):
    if numero1 is None or numero2 is None:
        numero1 = int(input("Introduce el primer número entero: "))
        numero2 = int(input("Introduce el segundo número entero: "))
    
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    
    if numero2 != 0:
        division_entera = numero1 // numero2
    else:
        division_entera = "No se puede dividir entre cero"
    
    print("Resultados de las operaciones:")
    print("Suma:", suma)
    print("Resta:", resta)
    print("Multiplicación:", multiplicacion)
    print("División entera:", division_entera)

# Llamadas a la función
operaciones()
operaciones(10, 2)
operaciones(10, 0)

# -----------------------------------------------------------------

"""
## Ejercicio 2: Área de un círculo.
Escribe un programa que:
- Pida al usuario el radio de un círculo (float).
- Calcule el área del círculo usando la fórmula Área = π * radio².
- Muestre el resultado con dos decimales.
"""

import math

def area(radio = None):
    if radio is None:
        radio = float(input("Introduce el radio del circulo: "))
    
    area = math.pi * radio**2
    print(f"El área del circulo es: {area:.2f}")

area()         # pide el radio por teclado
area(3.5)      # calcula con un valor dado

# -----------------------------------------------------------------

"""
## Ejercicio 3: Comparación de números.
Escribe un programa que:
- Pida dos números al usuario.
- Determine si el primer número es mayor que el segundo y muestre el resultado como un booleano (True o False).
"""

def comparacion(numero1=None, numero2=None):
    if numero1 is None or numero2 is None:
        numero1 = float(input("Introduce el primer número a comparar: "))
        numero2 = float(input("Introduce el segundo número a comparar: "))
    
    print(f"¿{numero1} es mayor que {numero2}? : {numero1>numero2}")

comparacion(10, 5)      # → 10 es mayor que 5 ? : True
comparacion(4.2, 9.1)   # → 4.2 es mayor que 9.1 ? : False
comparacion()           # → pide datos por teclado

# -----------------------------------------------------------------

"""
## Ejercicio 4: Manipulación de cadenas.
Escribe un programa que:
- Pida al usuario una palabra.
- Muestre el nombre en mayúsculas, minúsculas, con la primera letra en mayúscula y con las mayúsculas y minúsculas alternadas.
"""

def cadenas (nombre=None):
    if nombre is None:
        nombre = input("Introduce el nombre: ")

    print("Mayúsculas:", nombre.upper())        # Mayúsculas
    print("Minúsculas:", nombre.lower())        # Minúsculas
    print("Capitalizada:", nombre.capitalize()) # Primera letra mayúscula
    print("Alternadas:", nombre.swapcase())     # Mayúsculas y minúsculas alternadas

cadenas("Cristian")
cadenas() # → pide entrada

# -----------------------------------------------------------------

"""
## Ejercicio 5: Manipulación de cadenas. 
Escribe un programa que:
- Pida al usuario una palabra y una letra.
- Verifique si la letra se encuentra o no y se lo diga al usuario.
"""

def existe(palabra=None, letra=None):
    if palabra is None or letra is None:
        palabra = input("Introduce la palabra: ").strip()
        letra = input("Introduce la letra: ").strip()
    
    print(f'¿La letra "{letra}" se encuentra en la palabra "{palabra}"? : {letra in palabra}')

existe()
existe("palabra","a") # True

# -----------------------------------------------------------------