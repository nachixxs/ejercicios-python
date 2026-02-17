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
    

cuenta1 = CuentaBancaria("Nacho")
print(cuenta1.consultar_saldo())  

print(cuenta1.depositar(1000))    

print(cuenta1.depositar(500))     

print(cuenta1.retirar(300))       

print(cuenta1.retirar(2000))      

print(cuenta1.consultar_saldo())  

cuenta2 = CuentaBancaria("Ana", 5000)
print(cuenta2.consultar_saldo())  