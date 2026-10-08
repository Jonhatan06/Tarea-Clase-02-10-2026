"""Ejercicio 5: Vehículo de una agencia."""


class Vehiculo:
    def __init__(self, marca, modelo, anio, precio):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.precio = precio

    def descripcion_comercial(self):
        precio_formateado = f"{self.precio:,.0f}".replace(",", ".")
        return f"{self.marca} {self.modelo} {self.anio} - {precio_formateado} Gs."

    def __str__(self):
        return f"Vehículo publicado: {self.descripcion_comercial()}"


vehiculo_1 = Vehiculo("Toyota", "Corolla", 2020, 95000000)
vehiculo_2 = Vehiculo("Kia", "Sportage", 2022, 165000000)

print(vehiculo_1)
print(vehiculo_2)
