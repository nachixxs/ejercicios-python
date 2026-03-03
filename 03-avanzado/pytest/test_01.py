import pytest

def calcular_descuento(precio: float, porcentaje: float) -> float:
    return precio * (1 - porcentaje / 100)

@pytest.mark.parametrize("precio, porcentaje, resultado_esperado", [
    (100, 20, 80.0),
    (50, 10, 45.0),
    (200, 50, 100.0),
    (150, 0, 150.0),
    (80, 100, 0.0)
])
def test_calcular_descuento_parametrizado(precio, porcentaje, resultado_esperado):
    assert calcular_descuento(precio, porcentaje) == resultado_esperado