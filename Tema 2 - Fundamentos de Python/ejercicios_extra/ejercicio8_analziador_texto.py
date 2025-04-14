# -------------------- EJERCICIO 8: Analizador de texto --------------------

"""
- Pide al usuario una frase.
- Muestra:
    - La longitud del texto.
    - El número de palabras. 
    - La frase en mayúsculas y en minúsculas.
    - Si contiene la palabra `"Python"` (insensible a mayúsculas).
"""

def analizar_texto():
    frase = input("Introduce una frase: ")
    print(f"Longitud: {len(frase)} caracteres")
    print(f"Número de palabras: {len(frase.split())}")
    print(f"Mayúsculas: {frase.upper()}")
    print(f"Minúsculas: {frase.lower()}")
    print(f"Contiene 'Python'?: {'python' in frase.lower()}")