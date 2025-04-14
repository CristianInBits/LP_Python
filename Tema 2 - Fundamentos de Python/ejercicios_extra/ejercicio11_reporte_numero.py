# -------------------- EJERCICIO 11: Reporte de número --------------------

"""
Pide al usuario un número decimal.
Muestra:
    - Su parte entera.
    - Su valor redondeado con 2 decimales.
    - Si es mayor que 100.
    - Su valor convertido a string y la longitud de la cadena.
"""


def reporte_numero():
    numero = float(input("Introduce un número decimal: "))
    parte_entera = int(numero)
    redondeado = round(numero, 2)
    mayor_que_100 = numero > 100
    cadena = str(numero)

    print(f"Parte entera: {parte_entera}")
    print(f"Redondeado (2 decimales): {redondeado}")
    print(f"¿Es mayor que 100?: {mayor_que_100}")
    print(f"Convertido a string: '{cadena}' con longitud {len(cadena)}")