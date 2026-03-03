#Async-01 — Simulá un sistema que "descarga" 3 archivos de forma concurrente. Cada descarga tarda un tiempo distinto (asyncio.sleep con valores distintos). Mostrá en consola cuándo empieza y termina cada una, y el tiempo total. El objetivo es demostrar que corren juntas, no una por una.

import asyncio
import time

async def descargar_archivo(nombre, tiempo_descarga):
    print(f"Empezando a descargar {nombre}...")
    await asyncio.sleep(tiempo_descarga)
    print(f"Terminó de descargar {nombre}.")

async def main():
    start_time = time.time()
    
    # Crear tareas para descargar los archivos
    tarea1 = asyncio.create_task(descargar_archivo("Archivo 1", 3))
    tarea2 = asyncio.create_task(descargar_archivo("Archivo 2", 5))
    tarea3 = asyncio.create_task(descargar_archivo("Archivo 3", 2))
    
    # Esperar a que todas las tareas terminen
    await asyncio.gather(tarea1, tarea2, tarea3)
    
    end_time = time.time()
    print(f"Tiempo total de descarga: {end_time - start_time:.2f} segundos.")

asyncio.run(main())