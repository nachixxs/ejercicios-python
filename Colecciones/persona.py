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