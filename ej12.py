"""Ejercicio 12: Cuenta de servicio con planes."""


class LineaTelefonica:
    def __init__(self, cliente, gb_incluidos):
        self.cliente = cliente
        self.gb_incluidos = gb_incluidos
        self.gb_consumidos = 0

    def gb_disponibles(self):
        return self.gb_incluidos - self.gb_consumidos

    def registrar_consumo(self, gb):
        if gb <= 0:
            print("El consumo debe ser mayor que cero.")
        elif gb > self.gb_disponibles():
            print("No se registró el consumo: el paquete contratado se agotaría.")
        else:
            self.gb_consumidos += gb
            print(f"Se registraron {gb} GB de consumo.")
            if self.gb_disponibles() == 0:
                print("AVISO: el paquete contratado se agotó.")

    def __str__(self):
        return (
            f"Línea de {self.cliente}\n"
            f"Plan contratado: {self.gb_incluidos} GB\n"
            f"Consumidos: {self.gb_consumidos} GB\n"
            f"Disponibles: {self.gb_disponibles()} GB"
        )


linea = LineaTelefonica("Camila Ortiz", 10)
print(linea)
print()

linea.registrar_consumo(4)
print(linea)
print()

linea.registrar_consumo(6)
print(linea)
print()

linea.registrar_consumo(1)
print(linea)
