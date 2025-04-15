# -------------------- ESTRUCTURAS CONDICIONALES --------------------

edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# Operadores relacionales y lógicos
# >, <, >=, <=, ==, !=
# and, or, not

# -------------------- BUCLES WHILE --------------------

x = 1
while x < 5:
    print(x)
    x += 1

# Bucle infinito con break
while True:
    text = input("String to capitalize [type q to quit]: ")
    if text == "q":
        break
    print(text.capitalize())

# Bucle equivalente evitando break
text = ""
while text != "q":
    text = input("String to capitalize [type q to quit]: ")
    if text != "q":
        print(text.capitalize())

# Uso de continue
while True:
    value = input("Integer, please [q to quit]: ")
    if value == 'q':
        break
    number = int(value)
    if number % 2 == 0:
        continue
    print(number, "squared is", number*number)

# Bucle while con else (si no hubo break)
numbers = [1, 3, 5]
position = 0
while position < len(numbers):
    number = numbers[position]
    if number % 2 == 0:
        print('Found even number', number)
        break
    position += 1
else:
    print('No even number found')

# -------------------- BUCLES FOR --------------------

# Recorrer elementos de una secuencia
frutas = ('fresa', 'melón', 'uva')
for fruta in frutas:
    print(fruta)

numeros = ['uno', 'dos', 'tres']
for i in numeros:
    print(i)

for letra in "Python":
    print(letra)

# Uso de break y continue
word = 'Hueso'
for letter in word:
    if letter == 's':
        break
    print(letter)

word2 = 'Casa'
for letter in word2:
    if letter == 's':
        continue
    print(letter)

# Bucle for con else
word = 'Casa'
for letter in word:
    if letter == 'x':
        print("\u00a1Una 'x'!")
        break
    print(letter)
else:
    print("No hay una 'x' en", word)

# Uso de range()
for i in range(1, 4):
    print(i)  # 1, 2, 3

for i in range(1, 6, 2):
    print(i)  # 1, 3, 5
