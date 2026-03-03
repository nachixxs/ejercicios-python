from dataclasses import dataclass, field
from typing import List

@dataclass
class Tarea:
    titulo: str
    prioridad: int
    fecha_creacion: str
    completada: bool = False

def tareas_pendientes(tareas: List['Tarea']) -> List['Tarea']:
    return sorted([tarea for tarea in tareas if not tarea.completada], key=lambda x: x.prioridad)
    

tareas = [
    Tarea("Comprar leche", 2, "2024-06-01", False),
    Tarea("Hacer ejercicio", 1, "2024-06-02", False),
    Tarea("Lavar ropa", 3, "2024-06-03", True),
    Tarea("Estudiar Python", 1, "2024-06-04", False)
]

pendientes = tareas_pendientes(tareas)
for tarea in pendientes:
    print(f"{tarea.titulo} - Prioridad: {tarea.prioridad} - Fecha: {tarea.fecha_creacion}")

