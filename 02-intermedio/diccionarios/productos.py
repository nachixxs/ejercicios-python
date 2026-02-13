# Haz un diccionario con productos y precios. Pide al usuario un producto y muestra su precio.
def productosprecios():
    productos = {"manzana": 0.5,"banana": 0.3,"naranja": 0.7,"pera": 0.6}
    producto = input("Ingresa el nombre del producto: ").lower()
    
    while producto in productos:
            print(f"El precio de {producto} es ${productos[producto]}")
            producto = input("Ingresa otro producto (o uno que no esté para salir): ").lower()
    else:
        print(f"Lo siento, no tenemos {producto} en el inventario.")
productosprecios()