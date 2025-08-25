# Crear una función que determine el precio de entrada a un parque de diversiones
# según la edad y si es estudiante o no.

def entrada_parque(edad, estudiante):
    if edad < 12:
        return print("$5")
    elif edad >= 12 and edad < 60:
        return print("$7")
    
    if edad >= 25 and estudiante == True:
        return print("$8")
    else:
        return print("$10")
    
entrada_parque(10, False)
entrada_parque(30, False)
entrada_parque(23, True)
entrada_parque(70, False)