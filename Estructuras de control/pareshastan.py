# Este código muestra que los sets (conjuntos) en Python no permiten duplicados.
# Al intentar añadir el número 1 (que ya está en el set), el set no cambia.

def pares_hasta():
    num1 = int(input("Ingrese el número: "))
    for i in range(1, num1 + 1):
        if i % 2 == 0:
            print(i)

pares_hasta()