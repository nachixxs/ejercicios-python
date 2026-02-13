import random  # Importa el módulo random para generar números aleatorios

# Genera un número secreto aleatorio entre 1 y 10
secreto = random.randint(1, 10)

adivinado = False  # Variable para controlar si el número ya fue adivinado

# Bucle que se repite hasta que el usuario adivine el número
while not adivinado:
    intento = int(input("Adivina (1-10): "))  # Pide al usuario que ingrese un número

    # Si el número ingresado es igual al secreto
    if intento == secreto:
        print("¡Correcto!")  # Informa que adivinó correctamente
        adivinado = True     # Cambia la variable para salir del bucle
    else:
        print("Intenta otra vez")  # Informa que el intento fue incorrecto