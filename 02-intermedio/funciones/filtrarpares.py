def pares(lista):
    return [num for num in lista if num % 2 == 0]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(pares(numeros))  # Output: [2, 4, 6, 8, 10]


# Seria lo mismo que hacer esto:

#nueva_lista = []
#for x in lista:
#    if x % 2 == 0:  # si el número es divisible entre 2
#        nueva_lista.append(x)  # lo guardo
#return nueva_lista
