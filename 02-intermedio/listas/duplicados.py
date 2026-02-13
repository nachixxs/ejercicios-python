# Este código muestra que los sets (conjuntos) en Python no permiten duplicados.
# Al intentar añadir el número 1 (que ya está en el set), el set no cambia.

def duplicados(numeros):
    numeros.add(1)
    return numeros

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

print(duplicados(numeros))