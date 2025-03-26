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