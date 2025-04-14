# -------------------- EJERCICIO 7: Calculadora avanzada --------------------

"""
- Pide al usuario dos números enteros.
- Pide la operación que desea realizar: suma, resta, multiplicación, división, módulo o exponenciación.
- Devuelve el resultado o un mensaje de error si la operación no es válida.
"""

def calculadora():
    a = int(input("Introduce el primer número: "))
    b = int(input("Introduce el segundo número: "))
    operacion = input("Operación (+, -, *, /, %, **): ").strip()

    if operacion == "+":
        print(f"Resultado: {a + b}")
    elif operacion == "-":
        print(f"Resultado: {a - b}")
    elif operacion == "*":
        print(f"Resultado: {a * b}")
    elif operacion == "/":
        if b != 0:
            print(f"Resultado: {a / b}")
        else:
            print("Error: división entre cero")
    elif operacion == "%":
        print(f"Resultado: {a % b}")
    elif operacion == "**":
        print(f"Resultado: {a ** b}")
    else:
        print("Operación no válida")
