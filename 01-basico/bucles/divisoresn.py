def divisores_n():
    numero = int(input("Ingrese un número entero positivo: "))
    print(f"Divisores de {numero}:")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)

divisores_n()