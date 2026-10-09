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


clientes = []
cantidad_clientes = int(input("¿Cuántos clientes desea registrar? (mínimo 2): "))

while cantidad_clientes < 2:
    cantidad_clientes = int(input("Ingrese una cantidad de 2 o más clientes: "))

for numero in range(1, cantidad_clientes + 1):
    print(f"\nDatos del cliente {numero}")
    nombre = input("Nombre: ")
    cedula = input("Cédula: ")
    telefono = input("Teléfono: ")
    clientes.append(Cliente(nombre, cedula, telefono))

print("\nFICHAS DE CLIENTES")
for cliente in clientes:
    print(cliente)
    print()
