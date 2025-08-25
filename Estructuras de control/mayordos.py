def numeros(nums):
    input1 = int(input("Ingrese el primer numero: "))
    input2 = int(input("Ingrese el segundo numero: "))

    if input1 > input2:
        return "El numero mayor es: " + str(input1)
    elif input2 > input1:
        return "El numero mayor es: " + str(input2)
    else:
        return "Los numeros son iguales"
    
print(numeros(0))