# Calculadora simple que realiza operaciones básicas

def calculadora():
    print("Bienvenido a la calculadora")
    print("Seleccione la operación que desea realizar:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    operacion = input("Ingrese el número de la operación (1/2/3/4): ")

    if operacion in ['1', '2', '3', '4']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if operacion == '1':
            resultado = num1 + num2
            print(f"{num1} + {num2} = {resultado}")

        elif operacion == '2':
            resultado = num1 - num2
            print(f"{num1} - {num2} = {resultado}")

        elif operacion == '3':
            resultado = num1 * num2
            print(f"{num1} * {num2} = {resultado}")

        elif operacion == '4':
            if num2 != 0:
                resultado = num1 / num2
                print(f"{num1} / {num2} = {resultado}")
            else:
                print("Error: No se puede dividir por cero.")
    else:
        print("Operación inválida. Por favor, seleccione una opción válida.")

    
calculadora()