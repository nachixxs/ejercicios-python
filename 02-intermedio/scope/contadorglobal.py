contador = 0

def incrementar_contador():
    global contador
    contador += 1
    print(f"Contador: {contador}")

def incrementar_local():
    contador = 100
    contador += 1
    print(f"Contador local: {contador}")

def resetear_contador():
    global contador
    contador = 0
    print("Contador reseteado a 0")

# Estado inicial
print(f"Inicio: {contador}")  # Inicio: 0

# Incrementar global
incrementar_contador()  # Contador: 1
incrementar_contador()  # Contador: 2
incrementar_contador()  # Contador: 3

# Incrementar local (NO afecta global)
incrementar_local()  # Local: 101
incrementar_local()  # Local: 101  ← Siempre empieza en 100

# Ver global
print(f"Global: {contador}")  # Global: 3  ← NO cambió

# Resetear
resetear_contador()  # Contador reseteado
print(f"Después reset: {contador}")  # Después reset: 0