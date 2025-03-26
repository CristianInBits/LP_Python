""" Ejercicio 1: Operaciones básicas con enteros. Escribe un programa que: 
- Pida al usuario dos números enteros. 
- Muestre la suma, resta, multiplicación y división entera de los dos números.
"""

numero1 = int(input("Introduce el primer número entero: "))
numero2 = int(input("Introduce el segundo número entero: "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division_entera = numero1 // numero2 

print("Resultados de las operaciones:")
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División entera:", division_entera)