def promedio_notas():
    alumnos = { "Juan": [10], "Ana": [9], "Luis": [8] }
    todas_las_notas = []  # Lista para guardar todas las notas

    for notas in alumnos.values():
        todas_las_notas.extend(notas)  # Agrega las notas de cada alumno a la lista

    if todas_las_notas:  # Verifica que haya al menos una nota
        promedio = sum(todas_las_notas) / len(todas_las_notas)
        print("Promedio de notas:", promedio)
    else:
        print("No hay notas para calcular el promedio.")

promedio_notas()