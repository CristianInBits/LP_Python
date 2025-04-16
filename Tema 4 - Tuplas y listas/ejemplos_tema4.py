# -------------------- TEMA 4 – TUPLAS --------------------

# Tuplas: colecciones inmutables de elementos ordenados
empty_tuple = ()
print(empty_tuple)  # ()

un_dia_de_la_semana = 'Lunes',
print(un_dia_de_la_semana)  # ('Lunes',)

un_dia_de_la_semana = ('Lunes',)
print(un_dia_de_la_semana)  # ('Lunes',)

# Tupla de un único elemento necesita coma
un_dia_de_la_semana = 'Lunes'
print(un_dia_de_la_semana)          # 'Lunes'
print(type(un_dia_de_la_semana))    # <class 'str'>

fin_de_semana = 'Sábado', 'Domingo'
print(fin_de_semana)  # ('Sábado', 'Domingo')

fin_de_semana = ('Sábado', 'Domingo')
print(fin_de_semana)  # ('Sábado', 'Domingo')

# Paréntesis obligatorios en ciertos contextos
un_dia_de_la_semana = 'Lunes',
print(type(un_dia_de_la_semana))  # <class 'tuple'>

print(type(('Lunes',)))           # <class 'tuple'>

# Asignación múltiple desde una tupla
fin_de_semana = ('Sábado', 'Domingo')
a, b = fin_de_semana
print(a)  # 'Sábado'
print(b)  # 'Domingo'

# Intercambio de valores entre tuplas
pares = ('2', '4', '6')
impares = ('1', '3', '5')
pares, impares = impares, pares
print(pares)    # ('1', '3', '5')
print(impares)  # ('2', '4', '6')

# Conversión a tupla con tuple()
saludo = "Hola"
tupla = tuple(saludo)
print(tupla)  # ('H', 'o', 'l', 'a')

lista = [2, 4, 6, 8]
tupla = tuple(lista)
print(tupla)  # (2, 4, 6, 8)

# Unir y repetir tuplas
print(('Sábado',) + ('Domingo', 'Lunes'))  # ('Sábado', 'Domingo', 'Lunes')
print(('hola',) * 3)  # ('hola', 'hola', 'hola')

# Comparación de tuplas
print((1, 2, 3) < (1, 2, 4))     # True
print((5, 1, 3) > (5, 2, 1))     # False
print((1, 2) < (1, 2, 3))        # True
print(("a", 2) < ("b", 1))       # True
print(("a", 2) < ("a", 3))       # True
print((1, "hola") < (2, 5))      # True
# print(("h", 1) < (2, "m"))     # TypeError: '<' not supported...
print((1, 2, 3) != (1, 2, 4))    # True

# Recorrer una tupla con for
words = ('fresh', 'out', 'of', 'ideas')
for word in words:
    print(word)

# Las tuplas son inmutables
# Aunque += parece modificar, realmente crea una nueva tupla

t2 = ('bmw', 'audi', 'mercedes')
t3 = ('honda',)
print(id(t2))
t2 += t3
print(t2)        # ('bmw', 'audi', 'mercedes', 'honda')
print(id(t2))    # ID diferente: se creó una nueva tupla

# -------------------- TEMA 4 – LISTAS --------------------

empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']
leap_years = [2000, 2004, '2008']

another_empty_list = list()
print(another_empty_list)  # []

print(list('cat'))
a_tuple = ('ready', 'fire', 'aim')
print(list(a_tuple))

dia = '9/19/2019'
print(dia.split('/'))
cadena = 'a/b//c/d///e'
print(cadena.split('/'))

colores = ['Rojo', 'Verde', 'Azul']
print(colores[0])
print(colores[1])
print(colores[2])

print(colores[-1])
print(colores[-2])
print(colores[-3])

# print(colores[4])  # IndexError

colores = ['Rojo', 'Verde', 'Azul', 'Naranja', 'Negro']
print(colores[0:4:2])
print(colores[5:2:-1])
print(colores[::-2])
print(colores[::-1])

colores = ['Rojo', 'Verde', 'Azul']
colores.reverse()
print(colores)
print(colores[4:0])
print(colores[-6:3])

colores.append('Gris')
print(colores)

colores = ['Azul', 'Verde', 'Rojo']
colores.insert(-5, 'Gris')
colores.insert(-5, 'Rosa')
colores.insert(2, 'Rojo')
colores.insert(9, 'Negro')
print(colores)

print(['blah'] * 3)

pares = ['2', '4', '6']
otros = ['8', '10']
pares.extend(otros)
print(pares)
mas_pares = ['12', '14']
pares += mas_pares
print(pares)

pares = ['2', '4', '6']
otros = ['8', '10']
pares.append(otros)
print(pares)

pares[3] = 2
print(pares)

numbers = [1, 2, 3, 4]
numbers[1:3] = [8, 9]
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = [7, 8, 9]
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = []
print(numbers)

numbers = [1, 2, 3, 4]
numbers[1:3] = 'wat?'
print(numbers)

numbers = [6, 7, 8, 9]
numbers.remove(8)
print(numbers)

print(numbers.pop(2))

numbers.clear()
print(numbers)

numbers = [1, 5, 7, 3, 4, 3]
numbers.sort()
print(numbers)

numbers2 = numbers.copy()
print(numbers2)
print(id(numbers))
print(id(numbers2))

lista = [10, 5, 7, 10, 3, 5, 10]
print("Lista:", lista)
print("Longitud de la lista:", len(lista))
print("Valor mínimo:", min(lista))
print("Valor máximo:", max(lista))
print("Suma total:", sum(lista))

buscado = 7
if buscado in lista:
    print(f"Sí, el número {buscado} está en la lista.")
    print(f"El núm. {buscado} está en la posición:", lista.index(buscado))
    print(f"El número {buscado} aparece {lista.count(buscado)} veces.")

squares = [x**2 for x in range(5)]
print(squares)

even = [x for x in range(10) if x % 2 == 0]
print(even)

labels = ['even' if x % 2 == 0 else 'odd' for x in range(5)]
print(labels)

pairs = [(x, y) for x in range(3) for y in range(2)]
print(pairs)

raw_data = [" Alice", "Bob ", " Carol "]
cleaned = [name.strip().lower() for name in raw_data]
print(cleaned)
