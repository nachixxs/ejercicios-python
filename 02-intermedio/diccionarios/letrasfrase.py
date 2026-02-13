# Cuenta cuántas veces aparece cada letra en una frase usando un diccionario.
def letras_frase():
    while True:
    
        frase = input("Ingresa una frase: ").lower()  # Solicita al usuario que ingrese una frase y la convierte a minúsculas
        conteo_letras = {}  # Diccionario para almacenar el conteo de cada letra

        for letra in frase:
            if letra.isalpha():  # Verifica si el carácter es una letra (ignora espacios y puntuación)
                if letra in conteo_letras:
                    conteo_letras[letra] += 1  # Incrementa el conteo si la letra ya está en el diccionario
                else:
                    conteo_letras[letra] = 1   # Inicializa el conteo en 1 si es la primera vez que aparece

        for letra, conteo in conteo_letras.items():
            print(f"La letra '{letra}' aparece {conteo} veces.")  # Muestra el conteo de cada letra

        otra_frase = input("¿Quieres ingresar otra frase? (s/n): ").lower()
        if otra_frase != 's':
            break
letras_frase()  # Llama a la función para ejecutar el conteo de letras