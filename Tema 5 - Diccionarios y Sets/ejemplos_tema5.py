# -------------------- TEMA 5 – DICCIONARIOS --------------------

# Crear diccionarios
empty_dict = {}
print(empty_dict)  # {}

dias_de_la_semana = {1: 'Lunes', 2: 'Martes', 3: 'Miércoles'}
print(dias_de_la_semana)

# Crear usando dict()
acme_customer = dict(first="Wile", middle="E", last="Coyote")
print(acme_customer)

# Convertir estructuras a diccionario
lol = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(dict(lol))

lot = [('a', 'b'), ('c', 'd'), ('e', 'f')]
print(dict(lot))

tol = (['a', 'b'], ['c', 'd'], ['e', 'f'])
print(dict(tol))

los = ['ab', 'cd', 'ef']
print(dict(los))

tos = ('ab', 'cd', 'ef')
print(dict(tos))

# Añadir y modificar elementos
pythons = {'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric','Jones': 'Terry', 'Palin': 'Michael'}
pythons['Gilliam'] = 'Gerry'
print(pythons)
pythons['Gilliam'] = 'Terry'
print(pythons)

# Claves duplicadas: último valor prevalece
some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Jones',
    'Michael': 'Palin'
}
print(some_pythons)

# Acceso a elementos
print(some_pythons['John'])
# print(some_pythons['Groucho'])  # KeyError
print('Groucho' in some_pythons)
print(some_pythons.get('John'))
print(some_pythons.get('Groucho', 'Not a Python'))
print(some_pythons.get('Groucho'))

# keys, values, items
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
print(list(signals.keys()))
print(list(signals.values()))
print(list(signals.items()))
print(dict(signals.items()))

# Longitud
print(len(some_pythons))

# Unión de diccionarios
first = {'a': 'agony', 'b': 'bliss'}
second = {'b': 'bagels', 'c': 'candy'}
merged = {**first, **second}
print(merged)

third = {'b': 'best'}
merged_all = {**first, **third, **second}
print(merged_all)

# Shallow copy vs deepcopy
first = {'a': [1, 2]}
merged = {**first}
first['a'].append(3)
print(first)
print(merged)

import copy
merged2 = copy.deepcopy({**first})
first['a'].append(4)
print(first)
print(merged2)

# update()
pythons.update({'Marx': 'Groucho', 'Howard': 'Moe'})
print(pythons)

# update() sobrescribe
first = {'a': 1, 'b': 2}
second = {'b': 'platypus'}
first.update(second)
print(first)

# Borrar con del y pop()
del pythons['Marx']
del pythons['Howard']
print(pythons)

print(pythons.pop('Palin'))
print(pythons.pop('First', 'No key'))

# clear()
pythons.clear()
print(pythons)
pythons = {'Hola': 'Adios'}
pythons = {}
print(pythons)

# in
pythons = {'Chapman': 'Graham', 'Cleese': 'John', 'Jones': 'Terry', 'Palin': 'Michael', 'Idle': 'Eric'}
print('Chapman' in pythons)
print('Gilliam' in pythons)

# Asignación (=) y copia
signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile'}
save_signals = signals
signals['blue'] = 'confuse everyone'
print(save_signals)

original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
print(signals)
print(original_signals)

signals = {'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'smile']}
signals_copy = signals.copy()
signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)

signals = {'green': 'go', 'yellow': 'go faster', 'red': ['stop', 'smile']}
signals_copy = copy.deepcopy(signals)
signals['red'][1] = 'sweat'
print(signals)
print(signals_copy)

# Comparación
print({'a': 1, 'b': 2} == {'b': 2, 'a': 1})

# Recorrer diccionario
invierno = {'Enero': '1', 'Febrero': '2', 'Marzo': '3'}
for mes in invierno:
    print(mes)

for valor in invierno.values():
    print(valor)

for item in invierno.items():
    print(item)
    print(f"El mes de {item[0]} es el {item[1]}.")

for mes, num in invierno.items():
    print(f"El mes de {mes} es el {num}.")

# Diccionario por comprensión
word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)

letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

vowels = 'aeiou'
word = 'onomatopoeia'
vowel_counts = {letter: word.count(letter) for letter in set(word) if letter in vowels}
print(vowel_counts)
