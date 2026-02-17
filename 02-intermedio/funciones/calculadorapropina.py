def calcular_cuenta_restaurante(subtotal, propina=10, personas=1):
    """
    Calcula el monto que debe pagar cada persona en un restaurante.
    
    Args:
        subtotal: Monto antes de propina
        propina: Porcentaje de propina (default: 10)
        personas: Cantidad de personas (default: 1)
    
    Returns:
        float: Monto por persona o mensaje de error
    """
    if personas <= 0:
        return "Número de personas inválido"
    total_con_propina = subtotal + (subtotal * propina / 100)
    monto_por_persona = total_con_propina / personas
    return round(monto_por_persona, 2)

print(calcular_cuenta_restaurante(1000))           # 1100.0
print(calcular_cuenta_restaurante(1000, 15))       # 1150.0
print(calcular_cuenta_restaurante(1000, 20, 4))    # 300.0
print(calcular_cuenta_restaurante(1000, 10, 0))    # "Número de personas inválido"

