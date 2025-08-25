# Cree una función que solicite un número al usuario y calcule la suma de todos los números desde 1 hasta ese número.

def suma():
    num1 = int(input("Ingrese el número: "))
    suma = 0
    for i in range(1, num1 + 1):
        suma += i
        print(f"Después de sumar {i}, suma es {suma}")
    return suma

print(suma())