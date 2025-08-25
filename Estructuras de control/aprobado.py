def nota():
    calificacion = int(input("Introduce tu calificación (0-10): "))
    
    if calificacion < 0 or calificacion > 10:
        print("Calificación inválida. Debe estar entre 0 y 10.")
    elif calificacion >= 6:
        print("Aprobado")
    else:
        print("Reprobado")

nota()