def suma():
    num1 = int(input("Ingrese el número: "))
    suma = 0
    for i in range(1, num1 + 1):
        suma += i
        print(f"Después de sumar {i}, suma es {suma}")
    return suma

print(suma())