"""Ejercicio 2: Producto de almacén."""


class Producto:
    def __init__(self, nombre, precio_unitario, cantidad_stock):
        self.nombre = nombre
        self.precio_unitario = precio_unitario
        self.cantidad_stock = cantidad_stock

    def valor_total_stock(self):
        return self.precio_unitario * self.cantidad_stock

    def __str__(self):
        return (
            f"Producto: {self.nombre}\n"
            f"Precio unitario: {self.precio_unitario:,.0f} Gs.\n"
            f"Cantidad en stock: {self.cantidad_stock}\n"
            f"Valor total en stock: {self.valor_total_stock():,.0f} Gs."
        )


arroz = Producto("Arroz de 1 kg", 8500, 25)
aceite = Producto("Aceite de 900 ml", 14500, 18)
yerba = Producto("Yerba mate de 1 kg", 21000, 12)

print(arroz)
print()
print(aceite)
print()
print(yerba)
