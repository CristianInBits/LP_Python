"""
1.- Convertir una temperatura introducida por el usuario de Celsius
a Fahrenheit (ºF = ºC * 9/5 + 32)
"""

def temperatura():
    while True:
        entrada = input("Introduce la temperatura en °C [q para salir]: ").strip()
        if entrada.lower() == "q":
            print("Saliendo del programa.")
            break
        try:
            grados = float(entrada)
            fahrenheit = grados * 9 / 5 + 32
            print(f"{grados:.1f} °C equivalen a {fahrenheit:.1f} °F\n")
        except ValueError:
            print("Entrada inválida. Por favor, introduce un número o 'q' para salir.\n")

temperatura()

# ----------------------------------------------------------------------------------

"""
2.- Mostrar el cuadrado de los números impares de 1 a 20.
"""

def cuadrados ():
    for num in range (1,20,2):
        print(f"El cuadrado de {num:2} es: {num**2:3}")

cuadrados()

# ----------------------------------------------------------------------------------