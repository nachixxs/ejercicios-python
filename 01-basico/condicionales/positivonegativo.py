# Crear una función que determine si un número es positivo, negativo o cero.

def positivonegativo(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"
    
print(positivonegativo(5))
print(positivonegativo(-3))