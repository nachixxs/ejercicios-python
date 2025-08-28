# Crea un diccionario con nombres de alumnos y sus notas. Luego imprime el promedio.

def traduciringles(espanol):
    diccionario = {
        "hola": "hello",
        "adiós": "goodbye",
        "gracias": "thank you",
        "por favor": "please",
        "sí": "yes",
        "no": "no",
        "perro": "dog",
        "gato": "cat",
        "casa": "house",
        "comida": "food"
    }
    return diccionario.get(espanol.lower(), "Palabra no encontrada")

print(traduciringles("hola"))       # Output: hello
print(traduciringles("gracias"))    # Output: thank you
print(traduciringles("amigo"))      # Output: Palabra no encontrada
