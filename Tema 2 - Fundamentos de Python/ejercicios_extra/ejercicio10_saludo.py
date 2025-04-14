# -------------------- EJERCICIO 10: Saludo personalizado --------------------

"""
- Define una función `saludar(nombre=None, edad=None)`.
    - Si no se pasa el nombre o edad, los pide por teclado.
    - Muestra un mensaje del tipo:  
        `"Hola Cristian, tienes 30 años. ¡Bienvenido!"`  
        `"Hola, usuario anónimo. ¿Qué edad tienes?"` (si falta algún dato)
"""

def saludar(nombre=None, edad=None):
    if nombre is None:
        nombre = input("Introduce tu nombre: ") or "usuario anónimo"
    if edad is None:
        edad = input("Introduce tu edad: ") or "desconocida"

    print(f"Hola {nombre}, tienes {edad} años. ¡Bienvenido!")
