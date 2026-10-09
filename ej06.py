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


titular = input("Nombre del titular de la cuenta: ")
saldo_inicial = int(input("Saldo inicial en guaraníes, sin puntos: "))
cuenta = CuentaCorriente(titular, saldo_inicial)

opcion = ""
while opcion != "4":
    print("\n1. Acreditar saldo")
    print("2. Registrar consumo")
    print("3. Mostrar estado de la cuenta")
    print("4. Finalizar")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        monto = int(input("Monto a acreditar, sin puntos: "))
        cuenta.acreditar_saldo(monto)
        print(cuenta)
    elif opcion == "2":
        monto = int(input("Monto del consumo, sin puntos: "))
        cuenta.registrar_consumo(monto)
        print(cuenta)
    elif opcion == "3":
        print(cuenta)
    elif opcion == "4":
        print("Operaciones finalizadas.")
    else:
        print("Opción no válida.")
