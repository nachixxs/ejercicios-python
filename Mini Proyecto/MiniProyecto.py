# Mini-proyecto: Gestión de tareas simples

# Lista para guardar las tareas
tareas = []

def mostrar_menu():
    print("\n--- GESTIÓN DE TAREAS ---")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Eliminar tarea")
    print("4. Salir")

def agregar_tarea():
    tarea = input("Escribe la tarea: ")
    tareas.append(tarea)
    print(f"Tarea '{tarea}' agregada.")

def ver_tareas():
    if len(tareas) == 0:
        print("No hay tareas.")
    else:
        print("Tareas actuales:")
        for i, tarea in enumerate(tareas, start=1):
            print(f"{i}. {tarea}")

def eliminar_tarea():
    ver_tareas()
    if len(tareas) > 0:
        try:
            indice = int(input("Número de la tarea a eliminar: "))
            tarea_eliminada = tareas.pop(indice - 1)
            print(f"Tarea '{tarea_eliminada}' eliminada.")
        except (ValueError, IndexError):
            print("Número inválido.")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input("Elige una opción (1-4): ")

    if opcion == "1":
        agregar_tarea()
    elif opcion == "2":
        ver_tareas()
    elif opcion == "3":
        eliminar_tarea()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")
