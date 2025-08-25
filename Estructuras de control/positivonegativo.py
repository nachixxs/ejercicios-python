def positivonegativo(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"
    
print(positivonegativo(5))
print(positivonegativo(-3))