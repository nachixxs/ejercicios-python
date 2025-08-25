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