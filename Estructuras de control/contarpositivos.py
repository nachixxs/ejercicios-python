def positivonegativo():
    # Inicializa los contadores de positivos y negativos en 0
    positivos = 0
    negativos = 0

    # Pide 5 números al usuario usando un bucle
    for i in range(5):
        num = int(input("Número: "))  # Solicita un número al usuario

        # Si el número es mayor o igual a 0, suma 1 a positivos
        if num >= 0:
            positivos += 1
        # Si el número es menor que 0, suma 1 a negativos
        else:
            negativos += 1

    # Muestra la cantidad de números positivos y negativos ingresados