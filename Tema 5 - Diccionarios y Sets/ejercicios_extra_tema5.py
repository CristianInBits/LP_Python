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



## Extra 4: Palabras únicas por longitud
"""
Dada una lista de palabras, extraer solo una palabra por cada longitud distinta usando un set.
"""

words = ["tree", "sun", "moon", "cat", "river", "sky", "star"]

lengths_seen = set()
unique_by_length = []

for word in words:
    l = len(word)
    if l not in lengths_seen:
        unique_by_length.append(word)
        lengths_seen.add(l)

print(unique_by_length)
    


## Extra 5: Frecuencia de letras en una lista de palabras
"""
Contar cuántas veces aparece cada letra en una lista de palabras.
"""

words = ["dog", "cat", "duck"]

letter_counts = {}

for word in words:
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else
            letter_counts[letter] = 1

print(letter_counts)