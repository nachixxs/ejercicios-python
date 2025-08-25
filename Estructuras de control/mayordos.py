# Este código compara dos números ingresados por el usuario y determina cuál es mayor o si son iguales.

def numeros():
    input1 = int(input("Ingrese el primer número: "))
    input2 = int(input("Ingrese el segundo número: "))

    if input1 > input2:
        return f"El número mayor es: {input1}"
    elif input2 > input1:
        return f"El número mayor es: {input2}"
    else:
        return "Los números son iguales"

print(numeros())
