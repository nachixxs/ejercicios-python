# DC-01 — Modelá un Producto con dataclass: nombre: str, precio: float, stock: int, categoria: str. Agregale un método aplicar_descuento(porcentaje: float) -> None que modifique el precio, y una propiedad en_stock -> bool que devuelva si stock > 0. Todo tipado.
from dataclasses import dataclass, field
from typing import List

@dataclass
class Producto:
    nombre: str
    precio: float
    categoria: str
    stock: int = 0

    def aplicar_descuento(self, porcentaje: float) -> None:
        descuento = self.precio * (porcentaje / 100)
        self.precio -= descuento

    @property
    def en_stock(self) -> bool:
        return self.stock > 0

p = Producto("Remera", 1000.0, "ropa", 5)
print(p.en_stock)
p.aplicar_descuento(20)
print(p.precio)
