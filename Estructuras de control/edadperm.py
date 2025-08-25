def edad_permitida():
    edad = int(input("Ingrese su edad: "))
    
    if edad >= 18:
        return "Puedes entrar al club"
    else:
        return "No Puedes entrar al club"
    
print(edad_permitida())