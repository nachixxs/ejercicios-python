
def positivonegativo():

    positivos = 0
    negativos = 0
    for i in range(5):
        num = int(input("Número: "))
        if num >= 0:
            positivos += 1
        else:
            negativos += 1
    print("Positivos:", positivos)
    print("Negativos:", negativos)

positivonegativo()