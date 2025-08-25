# Este código muestra que los sets (conjuntos) en Python no permiten duplicados.
# Al intentar añadir el número 1 (que ya está en el set), el set no cambia.

def multiplicacion():
    num1 = int(input("Ingrese el número: "))

    for i in range(1, 11):
        print(num1, 'x', i, '=', num1 * i)

multiplicacion()