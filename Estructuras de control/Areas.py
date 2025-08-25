#Area de un triangulo
def area_triangulo(base, altura):
    return (base * altura) / 2

print("El area del triangulo es:", area_triangulo(5, 10))

#Area de un cuadrado
def area_cuadrado(lado):
    return lado * lado
print("El area del cuadrado es:", area_cuadrado(4))

#Area de un circulo
def area_circulo(radio):
    import math
    return math.pi * radio * radio
print("El area del circulo es:", area_circulo(3))