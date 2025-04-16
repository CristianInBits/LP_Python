# -------------------- EJERCICIOS PROPUESTOS TEMA 4 --------------------

# Ejercicio 1: Análisis de notas de estudiantes

"""
Descripción: Dada una lista de tuplas donde cada tupla contiene el nombre de un estudiante y una lista con sus calificaciones, muestra:
- Promedio de cada estudiante.
- El nombre del estudiante con mejor promedio.
- Solo los estudiantes que tienen una media mayor o igual a 7.
"""

def analizar_estudiantes(estudiantes):
    mejor_estudiante = None
    mejor_promedio = 0
    print("Promedios:")
    for nombre, notas in estudiantes:
        promedio = sum(notas) / len(notas)
        print(f"{nombre}: {promedio:.2f}")
        if promedio > mejor_promedio:
            mejor_promedio = promedio
            mejor_estudiante = nombre
    print(f"\nEstudiante con mejor promedio: {mejor_estudiante} ({mejor_promedio:.2f})")
    print("\nEstudiantes con promedio >= 7:")
    for nombre, notas in estudiantes:
        promedio = sum(notas) / len(notas)
        if promedio >= 7:
            print(f"{nombre}: {promedio:.2f}")

estudiantes = [
    ("Ana", [7, 8.5, 9]),
    ("Luis", [5, 6, 4]),
    ("Marta", [9, 9.5, 10]),
    ("Pedro", [6.5, 7, 6])
]
analizar_estudiantes(estudiantes)




# Ejercicio 2: Filtrado de productos por stock y precio

"""
Descripción: Dada una lista de productos (tuplas con nombre, precio y cantidad en stock), pide al usuario un presupuesto y muestra los productos que puede comprar (al menos 1 unidad), ordenados por precio ascendente. 
"""

def filtrar_productos(productos):
    presupuesto = float(input("Introduce tu presupuesto: "))
    disponibles = [p for p in productos if p[1] <= presupuesto and p[2] > 0]
    disponibles.sort(key=lambda x: x[1])
    print("\nProductos disponibles dentro de tu presupuesto:")
    for nombre, precio, stock in disponibles:
        cantidad = int(presupuesto // precio)
        print(f"{nombre} - {precio}€ - {stock} unidades (Puedes comprar hasta {cantidad})")

productos = [
    ("Teclado", 25.0, 10),
    ("Ratón", 15.5, 0),
    ("Monitor", 150.0, 2),
    ("USB", 8.0, 50)
]
filtrar_productos(productos)



# Ejercicio 3: Gestor de tareas
"""
 Descripción: Crea una lista vacía y un menú que permita al usuario:
 - Agregar tareas
 - Ver todas las tareas
 - Eliminar una tarea por índice
 - Salir del programa
"""

# Ejercicio 3: Gestor de tareas (versión con enumerate)
tareas = list()
while True:
    print("\n1. Agregar tarea\n2. Ver tareas\n3. Eliminar tarea\n4. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        tarea = input("Introduce la tarea: ")
        tareas.append(tarea)
    elif opcion == "2":
        print("Tareas:")
        for i, t in enumerate(tareas):
            print(f"{i}. {t}")
    elif opcion == "3":
        index = int(input("Introduce el índice de la tarea a eliminar: "))
        if 0 <= index < len(tareas):
            tareas.pop(index)
        else:
            print("Índice inválido")
    elif opcion == "4":
        break
    else:
        print("Opción no válida")

# Ejercicio 3: Gestor de tareas (versión sin enumerate)
tareas = []
while True:
    print("\n1. Agregar tarea\n2. Ver tareas\n3. Eliminar tarea\n4. Salir")
    opcion = input("Elige una opción: ")
    if opcion == "1":
        tarea = input("Introduce la tarea: ")
        tareas.append(tarea)
    elif opcion == "2":
        print("Tareas:")
        for i in range(len(tareas)):
            print(f"{i}. {tareas[i]}")
    elif opcion == "3":
        index = int(input("Introduce el índice de la tarea a eliminar: "))
        if 0 <= index < len(tareas):
            tareas.pop(index)
        else:
            print("Índice inválido")
    elif opcion == "4":
        break
    else:
        print("Opción no válida")



# Ejercicio 4: Separar pares e impares desde lista de números introducidos por el usuario
"""
Descripción: Dada una lista de números enteros que introduzca el usuario separados por coma, crea una nueva lista con los números pares y otras lista con los números impares.
"""
entrada = input("Introduce una lista de números separados por coma: ")
numeros = [int(n.strip()) for n in entrada.split(",")]
pares = [n for n in numeros if n % 2 == 0]
impares = [n for n in numeros if n % 2 != 0]
print("Pares:", pares)
print("Impares:", impares)


# Ejercicio 4: Versión alternativa con listas y bucle for
"""
Descripción: Dada una lista de números enteros que introduzca el usuario separados por coma, crea una nueva lista con los números pares y otras lista con los números impares.
"""
entrada_numeros = input("Introduce los números separados por coma: ")
lista_numeros = entrada_numeros.split(',')

pares_alt = []
impares_alt = []

for n in lista_numeros:
    numero = int(n.strip())
    if numero % 2 == 0:
        pares_alt.append(numero)
    else:
        impares_alt.append(numero)

print("Pares (versión alternativa):", pares_alt)
print("Impares (versión alternativa):", impares_alt)



# Ejercicio 5: Filtrado y conversión de temperaturas con listas por comprensión
"""
Usando listas por comprensión, dada una lista de temperaturas en Celsius, descartar las que tengan un valor menor que -50ºC o mayor a 100ºC y el resto, convertirlos a Fahrenheit y meterlos en otra lista para mostrarla por pantalla.
"""

lecturas_C = [22, -100, 35, 45, 120, 0, -10, 38, 29, 90, -55, 100]
filtradas = [c * 9/5 + 32 for c in lecturas_C if -50 <= c <= 100]
print("Temperaturas válidas en ºF:", filtradas)

