# Crear una función que indique si hace frío, calor o está agradable según la temperatura ingresada.

def abrigo(temp):
    if temp < 15:
        return print("Frio")
    elif temp >= 15 and temp <= 25:
        return print("Agradable")
    else:
        return print("Calor")
    
abrigo(10)
abrigo(20)
abrigo(30)
