class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, monto):
        self.saldo += monto
        return f"Depósito exitoso. Saldo actual: ${self.saldo}"
    
    def retirar(self, monto):
        if monto > self.saldo:
            return "Fondos insuficientes"
        self.saldo -= monto
        return f"Retiro exitoso. Saldo actual: ${self.saldo}"
    
    def consultar_saldo(self):
        return f"Titular: {self.titular} | Saldo: ${self.saldo}"
    

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo_inicial=0, tasa_interes=5):
        super().__init__(titular, saldo_inicial)
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        interes = self.saldo * (self.tasa_interes / 100)
        self.saldo += interes
        return f"Interés aplicado: ${interes}. Saldo actual: ${self.saldo}"
    
    def consultar_saldo(self):
        return f"Cuenta de Ahorro - Titular: {self.titular} | Saldo: ${self.saldo} | Tasa de Interés: {self.tasa_interes}%"
    

ahorro = CuentaAhorro("Nacho", 1000, 10)
print(ahorro.consultar_saldo())

print(ahorro.depositar(500))

print(ahorro.retirar(200))

print(ahorro.aplicar_interes())

print(ahorro.consultar_saldo())

print(ahorro.aplicar_interes())

ahorro2 = CuentaAhorro("Ana", 2000)

print(ahorro2.aplicar_interes())


print(ahorro2.consultar_saldo())
