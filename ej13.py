"""Ejercicio 13: Habitación de un hotel."""


class Habitacion:
    def __init__(self, numero, tipo, tarifa_por_noche):
        self.numero = numero
        self.tipo = tipo
        self.tarifa_por_noche = tarifa_por_noche
        self.ocupada = False

    def ocupar(self):
        if self.ocupada:
            print(f"La habitación {self.numero} ya se encuentra ocupada.")
        else:
            self.ocupada = True
            print(f"La habitación {self.numero} fue ocupada.")

    def liberar(self):
        if self.ocupada:
            self.ocupada = False
            print(f"La habitación {self.numero} fue liberada.")
        else:
            print(f"La habitación {self.numero} ya se encuentra libre.")

    def calcular_costo_estadia(self, cantidad_noches):
        if cantidad_noches > 0:
            return self.tarifa_por_noche * cantidad_noches
        return 0

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Libre"
        return (
            f"Habitación {self.numero}\n"
            f"Tipo: {self.tipo}\n"
            f"Tarifa por noche: {self.tarifa_por_noche:,.0f} Gs.\n"
            f"Estado: {estado}"
        )


habitacion = Habitacion(204, "Doble", 420000)
print(habitacion)
print()

habitacion.ocupar()
print(habitacion)
print()

noches = 3
costo = habitacion.calcular_costo_estadia(noches)
print(f"Costo de la estadía por {noches} noches: {costo:,.0f} Gs.")
print()

habitacion.liberar()
print(habitacion)
