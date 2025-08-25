# Problema: Crear una función que devuelva un diccionario con información de una persona,
# permitiendo modificar los valores por defecto, como la edad, el nombre, etc.

def persona(
    nombre: str = "Ignacio",
    apellido: str = "Cabrera",
    edad: int = 30,
    ciudad: str = "Buenos Aires"
) -> dict:
    return {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "ciudad": ciudad
    }

print(persona(edad=31))