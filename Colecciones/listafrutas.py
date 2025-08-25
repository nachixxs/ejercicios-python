# Problema: Modificar una lista de frutas agregando un nuevo elemento ("Papaya") y eliminando otro ("Melón").
# Este código muestra cómo agregar y quitar elementos de una lista en Python.

def listafruta(
    frutas: list[str] = [
        "Manzana",
        "Pera",
        "Naranja",
        "Plátano",
        "Fresa",
        "Kiwi",
        "Mango",
        "Piña",
        "Melón",
        "Sandía"
    ]
):
    frutas.append("Papaya")
    frutas.remove("Melón")
    return frutas

print(listafruta())