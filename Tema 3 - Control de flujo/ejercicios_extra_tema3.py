# -------------------- EJERCICIOS EXTRA TEMA 3 --------------------

# Ejercicio Extra 1: Mostrar todos los múltiplos de 3 entre 1 y 100

print("Múltiplos de 3 entre 1 y 100:")
for i in range(1, 101):
    if i % 3 == 0:
        print(i, end=", ")
print("\n")


# Ejercicio Extra 2: Pedir números hasta que la suma supere 100

suma = 0
while suma <= 100:
    numero = int(input("Introduce un número para sumar: "))
    suma += numero
print(f"Has superado 100 con una suma de {suma}.")


# Ejercicio Extra 3: Dibujar un triángulo de asteriscos

filas = int(input("¿Cuántas filas tendrá el triángulo?: "))
for i in range(1, filas + 1):
    print("*" * i)


# # Ejercicio Extra 4: Contar cuántos positivos y negativos se introducen hasta un 0

positivos = 0
negativos = 0
while True:
    n = int(input("Introduce un número (0 para terminar): "))
    if n == 0:
        break
    if n > 0:
        positivos += 1
    else:
        negativos += 1
print(f"Positivos: {positivos}, Negativos: {negativos}")


# Ejercicio Extra 5: Mostrar los dígitos de un número uno a uno

numero = input("Introduce un número entero: ")
print("Dígitos:")
for digito in numero:
    print(digito)

# Alternativa: acumulando los dígitos en una cadena y luego mostrarla completa
n = input("Introduce un número entero: ")
cadena=""
print("Dígitos:")
for c in n:
    cadena += c
print(cadena)