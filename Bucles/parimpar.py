def parimpar():
    pares = 0
    impares = 0


    for _ in range(5):
        num = int(input("Ingrese un número: "))
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1

    print("Cantidad de números pares:", pares)
    print("Cantidad de números impares:", impares)
parimpar()