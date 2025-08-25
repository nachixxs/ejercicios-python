def comparar(a, b):
    if a == b:
        return "Son iguales"
    elif a > b:
        return "a es mayor que b"
    else:
        return "a es menor que b"
    
print(comparar(5, 3))
print(comparar(2, 4))
print(comparar(7, 7))