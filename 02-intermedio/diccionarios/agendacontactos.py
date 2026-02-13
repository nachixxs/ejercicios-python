# Simula una agenda de contactos con nombre, teléfono y correo.

def agenda_contactos():
    agenda = {
        "Juan": {"teléfono": "123456789", "correo": ""},
        "Ana": {"teléfono": "987654321", "correo": ""},
        "Luis": {"teléfono": "555555555", "correo": ""}
        }
    
    while True:
        contacto = input("Ingresa el nombre del contacto: ").title()
        if contacto in agenda:
            print(f"Teléfono: {agenda[contacto]['teléfono']}, Correo: {agenda[contacto]['correo']}")
        else:
            print(f"No se encontró el contacto {contacto}.")

        otro_contacto = input("¿Quieres buscar otro contacto? (s/n): ").lower()
        if otro_contacto != 's':
            break

agenda_contactos()

