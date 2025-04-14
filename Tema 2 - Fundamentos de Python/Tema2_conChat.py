# ------------------------IDENTACIÓN-------------------------------

nombre = "Cristian"

def presentacion(nombre):
    """Función que te presenta mostrando un saludo y tu nombre"""
    print(f"Hola, mi nombre es {nombre}")

help(presentacion)

presentacion(nombre)

# ----------------------BOOLEAN & INTEGER---------------------------

"""
Ejercicio 1: Nombres válidos
Di cuáles de las siguientes variables son válidas en Python:

1nombre = "Ana"
_nombre = "Luis"
nombre1 = "Carlos"
nombre completo = "Ana Pérez"
def = 5
__variable__ = "oculta"

"""



"""
Ejercicio 2: Booleanos
¿Qué imprime cada línea?

"""

print(bool(""))        # ?
print(bool("Python"))  # ?
print(bool(0))         # ?
print(bool([]))        # ?
print(bool([1, 2, 3])) # ?



"""
Ejercicio 3: Números y bases
- Crea un número binario que represente el número 23 y conviértelo a decimal.
- Convierte el número 255 a hexadecimal y octal.
- ¿Cuál es el resultado de divmod(19, 4)?
"""

num_decimal = int("10111", 2)
print(num_decimal)

num_hex=hex(255)
num_oct=oct(255)

divmod(19,4) # (4,3)



"""
Crea un programa que:
- Pida al usuario un número en binario como string (por ejemplo '1101').
- Convierta ese número a decimal e imprima el resultado.
- Diga si el número convertido es par o impar usando un booleano.
"""

num1 = "100" # 4

def convertir_decimal(n):
    num_decimal1 = int(n, 2)
    print(f"El número decimal es: {num_decimal1}")
    es_par = (num_decimal1 % 2 == 0)
    print(f"¿Es par?: {es_par}")

convertir_decimal(num1)

# convertir_decimal("100")
# 4
# Es par?: False

# -----------------------FLOAT & COMPLEX-----------------------------

"""
Ejercicio 1: Float
¿Qué valor devuelve cada línea?
"""

print(float('3.1416'))  # 3.1416
print(float(10))        # 10.0
print(float(True))      # 1.0
print(10 + 2.5)         # 12.5
print(False + 4.0)      # 4.0



"""
Ejercicio 2: Float
1- ¿Qué imprime este bloque?
- Escribe una expresión que convierta la cadena "2.5e2" a float y la multiplique por 2.
"""

x = float("3.14")
y = 2
z = True
print(x + y + z)
# 6.140000000000001


print(float(2.5e2)*2)


"""
Ejercicio 3: Complex
Escribe código que:
- Cree un número complejo z = 5 + 6j
- Imprima la parte real e imaginaria
- Sume z con 2 - 3j y multiplica el resultado por 1 + j
- Muestra el resultado final
"""

z1 = 5 + 6j
print(z1.real)
print(z1.imag)
# print(z1 + (2-3j))
z2 = z1 + (2-3j)
z3 = z2 * (1+1j)
print(z3)
# 5.0
# 6.0
# (4+10j)

# --------------------------STRING----------------------------------

"""
Ejercicio 1: Comparar estilos de formateo
Dadas las variables
- Escribe una cadena usando el formato antiguo con % que diga: 
"Cristian tiene 30 años".
- Haz lo mismo con .format().
- Hazlo con f-strings.
"""

nombre = "Cristian"
edad = 30

print("%s tiene %d años" % (nombre,edad))
print("{} tiene {} años" .format(nombre,edad))
print(f"{nombre} tiene {edad} años")



"""
Ejercicio 2: Formateo alineado
Dadas las variables
Muestra la frase "El gato está en el techo" con:
- Alineación a la izquierda
- Alineación a la derecha
- Alineación al centro
- Relleno con *
"""

animal = "gato"
lugar = "techo"

print("El {:<10s} está en el {:<12s}".format(animal, lugar))   # Alineación izquierda
print("El {:>10s} está en el {:>12s}".format(animal, lugar))   # Alineación derecha
print("El {:^10s} está en el {:^12s}".format(animal, lugar))   # Alineación centrada
print("El {:*^10s} está en el {:*^12s}".format(animal, lugar)) # Alineación centrada con relleno



"""
Ejercicio: Reporte de producto
Vas a crear una función que genere un pequeño informe de producto a partir de los siguientes datos:
- nombre_producto = "smartphone"
- categoria = "electrónica"
- precio = 899.99
- unidades_disponibles = 32

La función debe imprimir lo siguiente:
PRODUCTO: Smartphone         | CATEGORÍA: ELECTRÓNICA  
PRECIO:     899.99 €         | UNIDADES: 32
---------------------------------------------
Resumen: El producto "Smartphone" pertenece a la categoría "ELECTRÓNICA" y cuesta 899.99 €.

Reglas y requisitos:
1. Usa f-strings para toda la salida.
2. Formatea el precio con dos decimales y alineado a la derecha en un campo de 10 caracteres.
3. Convierte nombre_producto a capitalizado y categoria a mayúsculas.
4. Usa slicing para mostrar solo las primeras 3 letras de la categoría dentro del resumen final.
5. Rellena con guiones - una línea separadora de longitud 45.
6. Convierte el resumen final a mayúsculas alternadas (ejemplo: "eL PrOdUcTo...") usando .swapcase().
"""

nombre_producto = "smartphone"
categoria = "electrónica"
precio = 899.99
unidades_disponibles = 32

print(f"PRODUCTO: {nombre_producto.capitalize():<20s}| CATEGORÍA: {categoria.upper():<20s}")
print(f"PRECIO: {(('%s' % precio)+" €"):^22s}| UNIDADES: {unidades_disponibles:<20d}")
print("-"*45)
print(f'Resumen: El producto "{nombre_producto.capitalize()}" pertenece a la categoría "{categoria.upper()[:3]}" y cuesta {('%s' % precio)+" €"}')
print((f'Resumen: El producto "{nombre_producto.capitalize()}" pertenece a la categoría "{categoria.upper()[:3]}" y cuesta {('%s' % precio)+" €"}').swapcase())

print(f"PRODUCTO: {nombre_producto.capitalize():<20}| CATEGORÍA: {categoria.upper():<20}")
print(f"PRECIO: {f'{precio:.2f} €':^22}| UNIDADES: {unidades_disponibles:<20}")
print("-" * 45)
resumen = f'Resumen: El producto "{nombre_producto.capitalize()}" pertenece a la categoría "{categoria.upper()[:3]}" y cuesta {precio:.2f} €'
print(resumen)
print(resumen.swapcase())

# ---------------------------NONE-----------------------------------

"""
Ejercicio: Registro de usuario opcional
1. Define una función registro(nombre=None) que:
    - Si se pasa el nombre, imprima: "Bienvenido, <nombre>!"
    - Si no se pasa, imprima: "Usuario anónimo, bienvenido."
2. Llama a la función una vez con tu nombre y otra vez sin argumentos.
"""

def registro(nombre=None):
    if nombre is None:
        print("Usuario anónimo, bienvenido")
    else:
        print(f"Bienvenido, {nombre}!")

# registro("Ana")
# Bienvenido, Ana!

# registro()
# Usuario anónimo, bienvenido