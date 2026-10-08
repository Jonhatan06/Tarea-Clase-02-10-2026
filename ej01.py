"""Ejercicio 1: Ficha de cliente."""


class Cliente:
    def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

    def __str__(self):
        return (
            f"Ficha del cliente\n"
            f"Nombre: {self.nombre}\n"
            f"Cédula: {self.cedula}\n"
            f"Teléfono: {self.telefono}"
        )


cliente_1 = Cliente("María González", "4.567.890", "0981 123 456")
cliente_2 = Cliente("Carlos Benítez", "5.432.109", "0971 654 321")

print(cliente_1)
print()
print(cliente_2)
