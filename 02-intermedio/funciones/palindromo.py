def palindromo():
    palabra = input("Ingresa una palabra: ")  # Solicita al usuario que ingrese una palabra
    palabra = palabra.lower().replace(" ", "")# Convierte la palabra a minúsculas y elimina espacios
    if palabra == palabra[::-1]:              # Compara la palabra con su reverso (usando slicing)
        print(f"{palabra} es un palíndromo") # Si son iguales, es un palíndromo
    else:
        print(f"{palabra} no es un palíndromo")  # Si no son iguales, no es un palíndromo

palindromo()  # Llama a la función para ejecutar el chequeo de palíndromo