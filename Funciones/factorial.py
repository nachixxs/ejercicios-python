# Crear una funcion que calcule el factorial de un número dado.

def factorial(n):  # Define la función factorial que recibe un número n
    if n == 0 or n == 1: # Si n es 0 o 1, el factorial es 1 (caso base)
        return 1 # Devuelve 1 si se cumple la condición anterior
    return n * factorial(n - 1) # Si no, multiplica n por el factorial de n-1 (llamada recursiva)

print(factorial(5))  # Output: 120


# Como 5 no es 0 ni 1, entra en el else
# factorial(5) = 5 * factorial(4)
# Como 4 no es 0 ni 1, entra en el else
# factorial(4) = 4 * factorial(3)
# Como 3 no es 0 ni 1, entra en el else
# factorial(3) = 3 * factorial(2)
# Como 2 no es 0 ni 1, entra en el else
# factorial(2) = 2 * factorial(1)
# Como 1 es 1, entra en el if
# factorial(1) = 1