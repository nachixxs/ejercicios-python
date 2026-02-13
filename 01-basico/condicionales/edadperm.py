def edad_permitida():
    try:
        edad = int(input("Ingrese su edad: "))
        if edad >= 18:
            return "Puedes entrar al club"
        else:
            return "No puedes entrar al club"
    except ValueError:
        return "Por favor, ingrese un número válido."

print(edad_permitida())
