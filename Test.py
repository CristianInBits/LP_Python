print("Hello Wolrd.")

import this

# Esto es un comentario en una sola línea
print("Hola, mundo") # Este comentario explca la función print

"""
Esto es un comentario de varias líneas.
Se usa para documentar funciones, clases o módulos.
No se ejecuta cuando el código corre
"""

def sumar(a,b):
    """ Esta función recibe dos números y devuelve su suma"""
    return a + b

help(sumar)

def saludar():
    print("Hola mundoooo")

saludar()


# Método correcto
def long_function_name(
        var_one, 
        var_two, 
        var_three, 
        var_four):
    print("foo")

long_function_name(1,2,3,4)

# Funciona, pero se debería usar espacios en los argumentos
def long_function_name2(
    var_one, 
    var_two, 
    var_three, 
    var_four):
    print("foo2")

long_function_name2(1,2,3,4)

import keyword
print(keyword.kwlist)

# Tipos de datos : Boolean

bool(True) #True
bool(20) #True
bool(-45) #True

bool(False) #False
bool(0) #False
bool(0.0) #False

