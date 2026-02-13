# Crear una función que indique si una persona ha aprobado o no un examen según su calificación.

def nota():
    calificacion = int(input("Introduce tu calificación (0-10): "))
    
    if calificacion < 0 or calificacion > 10:
        return "Calificación inválida. Debe estar entre 0 y 10."
    elif calificacion >= 6:
        return "Aprobado"
    else:
        return "Desaprobado"

print(nota())
