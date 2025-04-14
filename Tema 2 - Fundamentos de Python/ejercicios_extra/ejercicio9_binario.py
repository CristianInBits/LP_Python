# -------------------- EJERCICIO 9: Binario interactivo --------------------

"""
- Pide un número entero al usuario. 
- Muestra:
    - Su valor en binario, octal y hexadecimal.
    - Si el número es par o impar.
    - El resultado de elevarlo al cuadrado.
"""

def info_numero():
    numero = int(input("Introduce un número entero: "))
    print(f"Binario: {bin(numero)}")
    print(f"Octal: {oct(numero)}")
    print(f"Hexadecimal: {hex(numero)}")
    print(f"¿Es par?: {numero % 2 == 0}")
    print(f"Al cuadrado: {numero ** 2}")
