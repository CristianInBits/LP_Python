# -------------------- EJERCICIOS EXTRA TEMA 5 --------------------

## Extra 1: Agrupar palabras por longitud
"""
Dado un conjunto de palabras, agruparlas en un diccionario según su longitud.
"""

words = ["apple", "banana", "kiwi", "plum", "grape", "pear"]

length_groups = {}

for word in words:
    length = len(word)
    if length not in length_groups:
        length_groups[length] = [word]
    else:
        length_groups[length].append(word)

print(length_groups)



## Extra 2: Combinar inventarios de tiendas
"""
Combinar dos diccionarios de inventario sumando las cantidades de productos que coincidan.
"""

store1 = {"apple": 10, "banana": 5, "orange": 8}
store2 = {"banana": 4, "apple": 6, "grape": 12}

combined = store1.copy()

for product, quantity in store2.items():
    if product in combined:
        combined[product] += quantity
    else:
        combined[product] = quantity

print(combined)



## Extra 3: Eliminar claves duplicadas con mismo valor
"""
Eliminar de un diccionario las claves que tengan el mismo valor para quedarnos solo con una de ellas.
"""

data = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}

seen = set()
unique_dict = {}

for key, value in data.items():
    if value not in seen:
        unique_dict[key] = value
        seen.add(value)

print(unique_dict)
