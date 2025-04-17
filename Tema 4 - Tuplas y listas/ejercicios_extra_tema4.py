# -------------------- EJERCICIOS EXTRA TEMA 4 --------------------

# Ejercicio Extra 1: Unir dos listas de nombres eliminando duplicados

nombres1 = ["Ana", "Luis", "Pedro", "Marta"]
nombres2 = ["Luis", "Carlos", "Ana", "Sofía"]

combinados = nombres2.copy()
for nombre1 in nombres1:
    if nombre1 not in nombres2:
        combinados.append(nombre1)
print("Lista combinada sin duplicados:", combinados)

# Versión alternativa usando bucle y lista auxiliar
combinados_alt = []
for nombre in nombres1 + nombres2:
    if nombre not in combinados_alt:
        combinados_alt.append(nombre)
print("Lista combinada alternativa:", combinados_alt)


# Ejercicio Extra 2: Contar cuántas veces aparece cada número en una lista
numeros = [4, 2, 7, 4, 2, 4, 7, 8, 2, 2]

# Crear lista de únicos
unicos = []
for n in numeros:
    if n not in unicos:
        unicos.append(n)

# Contar ocurrencias
for n in unicos:
    contador = 0
    for x in numeros:
        if x == n:
            contador += 1
    print(f"El número {n} aparece {contador} veces")


# Versión alternativa usando índice (con lista de frecuencias)
frecuencias = [0] * (max(numeros) + 1)
for n in numeros:
    frecuencias[n] += 1

print("\nFrecuencias por índice:")
for i in range(len(frecuencias)):
    if frecuencias[i] > 0:
        print(f"El número {i} aparece {frecuencias[i]} veces")


# Ejercicio Extra 3: Mostrar tuplas (nombre, longitud) para cada palabra de una frase

frase = input("Introduce la frase: ")
palabras = frase.split()
longitudes = [(palabra,len(palabra)) for palabra in palabras]
print("Palabras y longitudes:", longitudes)


# Ejercicio Extra 4: Crear una lista con los cuadrados de los números impares entre 1 y 20

cuadrados_impares = [x**2 for x in range(1, 21) if x % 2 != 0]
print("Cuadrados de impares del 1 al 20:", cuadrados_impares)



# Ejercicio Extra 5: Aplanar una lista de tuplas
lista_tuplas = [(1, 2), (3, 4), (5, 6)]
lista_única = [elemento for tupla in lista_tuplas for elemento in tupla]
print("Lista aplanada:", lista_única)