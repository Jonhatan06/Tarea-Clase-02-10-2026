"""Ejercicio 6: Caja registradora de una cuenta corriente."""


class CuentaCorriente:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def acreditar_saldo(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Se acreditaron {monto:,.0f} Gs. a la cuenta.")
        else:
            print("El monto a acreditar debe ser positivo.")

    def registrar_consumo(self, monto):
        if monto <= 0:
            print("El monto del consumo debe ser positivo.")
        elif monto > self.saldo:
            print("Compra rechazada: saldo insuficiente.")
        else:
            self.saldo -= monto
            print(f"Consumo de {monto:,.0f} Gs. registrado.")

    def __str__(self):
        return f"Cuenta de {self.titular}: saldo disponible {self.saldo:,.0f} Gs."


cuenta = CuentaCorriente("Ana Martínez")
print(cuenta)

cuenta.acreditar_saldo(100000)
print(cuenta)

cuenta.registrar_consumo(35000)
print(cuenta)

cuenta.registrar_consumo(80000)
print(cuenta)

cuenta.acreditar_saldo(50000)
print(cuenta)
