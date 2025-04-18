# -------------------- EJERCICIOS PROPUESTOS --------------------

## Ejercicio 1: Contar ocurrencias
"""
Cuenta el número de veces que una palabra se repite:
    words = ["cpu", "gpu", "ram", "cpu", "gpu", "cpu"]
    # Output: {'cpu': 3, 'gpu': 2, 'ram': 1}
"""

words = ["cpu", "gpu", "ram", "cpu", "gpu", "cpu"]

word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

# Versión con diccionario por comprensión (usando set para evitar repeticiones):
word_count2 = { word: words.count(word) for word in set(words)}
print(word_count2)



## Ejercicio 2: Nota media por estudiante
"""
Calcula la nota media de cada estudiante y muéstralo en un diccionario:
grades = {
	"Alice": [8, 9, 7],
	"Bob": [6, 7, 7],
	"Charlie": [10, 9, 10]
}
# Output: {'Alice': 8.0, 'Bob': 6.67, 'Charlie': 9.67}
"""

grades = {
	"Alice": [8, 9, 7],
	"Bob": [6, 7, 7],
	"Charlie": [10, 9, 10]
}

# Versión 1 - clásica con índices:
averages = {}
for student in grades.items():
    averages[student[0]] = round(sum(student[1])/len(student[1]), 2)
print(averages)

# Versión 2 - desempaquetando:
averages2 = {}
for name, scores in grades.items():
    averages2[name] = round(sum(scores) / len(scores), 2)
print(averages2)

# Versión 3 - comprensión de diccionarios:
averages3 = { student: round(sum(scores)/len(scores),2) for student,scores in grades.items()}
print(averages3)


## Ejercicio 3: Carácter más repetido
"""
Muestra el carácter que se repita más veces:
    text = "engineering"
    # Output: 'e' aparece 3 tres veces
"""

text = "engineering"

# Versión 1, usando solo valores y luego buscando la letra correspondiente:
letter_counts = { letter: text.count(letter) for letter in text }
max_value = max(letter_counts.values())
for letter in letter_counts:
    if letter_counts[letter] == max_value:
        print(f"'{letter}' aparece {max_value} veces")
        break

# Versión 2
char_count = {}
for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

max_count = 0
most_common = ''
for char in char_count:
    if char_count[char] > max_count:
        max_count = char_count[char]
        most_common = char

print(f"'{most_common}' aparece {max_count} veces")


# Versión 3, alternativa con una tupla:
most_common2 = sorted(char_count.items(), key=lambda x: x[1], reverse=True)[0]
print(f"'{most_common2[0]}' aparece {most_common2[1]} veces")


## Ejercicio 4: IPs únicas
"""
Mediante el uso de un set, identifique el número de ips únicas:

ip_logs = [
	"192.168.0.1",
	"10.0.0.1",
	"192.168.0.1",
	"10.0.0.2",
	"10.0.0.1",
	"192.168.0.2"
]
# Output: 4 unique IPs
"""

ip_logs = [
	"192.168.0.1",
	"10.0.0.1",
	"192.168.0.1",
	"10.0.0.2",
	"10.0.0.1",
	"192.168.0.2"
]

unique_ips = set(ip_logs)
print(f"Total de IPs únicas: {len(unique_ips)}")


## Ejercicio 5: Comparación de cursos
"""
Partiendo de los siguientes sets:
    alice_courses = {"Math", "Electronics", "AI", "Data Structures"}
    bob_courses = {"AI", "Cybersecurity", "Math", "Robotics"}

- Encontrar los cursos en común.
- Encontrar los cursos que sólo Alice asiste.
- Encontrar los cursos que sólo uno de ellos asiste.
"""

alice_courses = {"Math", "Electronics", "AI", "Data Structures"}
bob_courses = {"AI", "Cybersecurity", "Math", "Robotics"}

# Cursos en común
common_courses = alice_courses & bob_courses
common_courses2 = alice_courses.intersection(bob_courses)
print("Cursos en común:", common_courses)
print("Cursos en común:", common_courses2)

# Solo Alice
only_alice = alice_courses - bob_courses
only_alice2 = alice_courses.difference(bob_courses)
print("Solo Alice:", only_alice)
print("Solo Alice:", only_alice2)

# Solo uno de los dos
only_one = alice_courses ^ bob_courses
only_one2 = alice_courses.symmetric_difference(bob_courses)
print("Solo uno de ellos:", only_one)
print("Solo uno de ellos:", only_one2)



## Ejercicio 6: Detección de duplicados en MACs
"""
Indicar si hay ips duplicadas:
    mac_addresses = ["00:1B:44:11:3A:B7", "00:1B:44:11:3A:B8 "00:1B:44:11:3A:B7"]
# Output: True (there are duplicates)
"""

mac_addresses = ["00:1B:44:11:3A:B7", "00:1B:44:11:3A:B8", "00:1B:44:11:3A:B7"]

has_duplicates = len(mac_addresses) != len(set(mac_addresses))
print("¿Hay duplicados?:", has_duplicates)



## Ejercicio 7: Invertir diccionario
"""
Crea y muestra un diccionario invertido mediante diccionarios por comprensión a partir del siguiente diccionario:
# Diccionario original: asignatura → profesor
profesores = {
	"Física": "Ana",
	"Química": "Luis",
	"Matemáticas": "Ana",
	"Informática": "Carlos"
}
# Diccionario invertido: profesor -> asignatura/s
"""

subjects = {
	"Physics": "Ana",
	"Chemistry": "Luis",
	"Mathematics": "Ana",
	"Computer Science": "Carlos"
}

# Crear un nuevo diccionario: teacher → lista de subjects
inverted = {}
for subject, teacher in subjects.items():
    if teacher in inverted:
        inverted[teacher].append(subject)
    else:
        inverted[teacher] = [subject]

print(inverted)

# {'Ana': ['Physics', 'Mathematics'], 'Luis': ['Chemistry'], 'Carlos': ['Computer Science']}

# Alternativa con diccionario por comprensión (menos eficiente pero válido):
inverted2 = {teacher: [s for s in subjects if subjects[s] == teacher] for teacher in set(subjects.values())}
print(inverted2)
