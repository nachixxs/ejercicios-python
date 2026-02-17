
def cuadrados_pares(n):
    return [x**2 for x in range(n) if x % 2 == 0]
    
def palabras_largas(lista_palabras, minimo=5):
    return [p.upper() for p in lista_palabras if len(p) >= minimo]

def extraer_numeros(lista_mixta):
    return [x for x in lista_mixta if isinstance(x, (int, float)) and not isinstance(x, bool)]

def matriz_identidad(n):
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]



print(cuadrados_pares(10))

palabras = ["python", "es", "genial", "y", "poderoso"]
print(palabras_largas(palabras))

print(palabras_largas(palabras, 7))

mixta = [1, "hola", 3.14, True, 42, "mundo", 7.5, None]
print(extraer_numeros(mixta))

print(matriz_identidad(3))
print(matriz_identidad(4))