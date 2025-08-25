def puede_votar(edad):
    if edad >= 18:
        return print("Debe votar")
    elif edad < 18 and edad >= 16:
        return print("Puede votar, pero no es obligatorio")
    else:
        return print("No puede votar")
    
puede_votar(20)
puede_votar(17)
puede_votar(15)
