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


empleado_1 = Empleado("Lucía Fernández", "Asistente administrativa", 3500000)
empleado_2 = Empleado("Diego Rojas", "Analista de sistemas", 6200000)

print(empleado_1)
print()
print(empleado_2)
