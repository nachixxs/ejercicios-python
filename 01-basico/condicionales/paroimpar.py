# Crear una función que determine si un número es par o impar

def paroimpar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"
    
print(paroimpar(4))
print(paroimpar(7))
print(paroimpar(0))
