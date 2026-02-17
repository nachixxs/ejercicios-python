def registrar_usuario(nombre, *hobbies, **datos_personales):
    return {
        "nombre": nombre,
        "hobbies": list(hobbies),
        "datos": datos_personales
    }

    
usuario1 = registrar_usuario("Nacho")
print(usuario1)

usuario2 = registrar_usuario("Nacho", "LoL", "programación", "gimnasio")
print(usuario2)

usuario3 = registrar_usuario(
    "Nacho", 
    "LoL", 
    "programación",
    edad=20,
    ciudad="Mendoza",
    profesion="Programador"
)
print(usuario3)

usuario4 = registrar_usuario("Nacho", edad=20, universidad="UTN")
print(usuario4)