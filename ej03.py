"""Ejercicio 3: Empleado y su sueldo."""


class Empleado:
    def __init__(self, nombre, cargo, salario_mensual):
        self.nombre = nombre
        self.cargo = cargo
        self.salario_mensual = salario_mensual

    def salario_anual(self):
        return self.salario_mensual * 12

    def __str__(self):
        return (
            f"Empleado: {self.nombre}\n"
            f"Cargo: {self.cargo}\n"
            f"Salario mensual: {self.salario_mensual:,.0f} Gs.\n"
            f"Salario anual: {self.salario_anual():,.0f} Gs."
        )


empleados = []
cantidad_empleados = int(input("¿Cuántos empleados desea registrar? "))

while cantidad_empleados < 1:
    cantidad_empleados = int(input("Ingrese por lo menos un empleado: "))

for numero in range(1, cantidad_empleados + 1):
    print(f"\nDatos del empleado {numero}")
    nombre = input("Nombre: ")
    cargo = input("Cargo: ")
    salario_mensual = int(input("Salario mensual en guaraníes, sin puntos: "))
    empleados.append(Empleado(nombre, cargo, salario_mensual))

print("\nEMPLEADOS REGISTRADOS")
for empleado in empleados:
    print(empleado)
    print()
