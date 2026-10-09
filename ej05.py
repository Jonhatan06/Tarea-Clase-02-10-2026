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


vehiculos = []
cantidad_vehiculos = int(input("¿Cuántos vehículos desea registrar? (mínimo 2): "))

while cantidad_vehiculos < 2:
    cantidad_vehiculos = int(input("Ingrese una cantidad de 2 o más vehículos: "))

for numero in range(1, cantidad_vehiculos + 1):
    print(f"\nDatos del vehículo {numero}")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
    anio = int(input("Año: "))
    precio = int(input("Precio en guaraníes, sin puntos: "))
    vehiculos.append(Vehiculo(marca, modelo, anio, precio))

print("\nVEHÍCULOS PARA PUBLICAR")
for vehiculo in vehiculos:
    print(vehiculo)
