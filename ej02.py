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


productos = []
cantidad_productos = int(input("¿Cuántos productos desea registrar? (2 o 3): "))

while cantidad_productos < 2 or cantidad_productos > 3:
    cantidad_productos = int(input("Ingrese solamente 2 o 3 productos: "))

for numero in range(1, cantidad_productos + 1):
    print(f"\nDatos del producto {numero}")
    nombre = input("Nombre: ")
    precio_unitario = int(input("Precio unitario en guaraníes, sin puntos: "))
    cantidad_stock = int(input("Cantidad en stock: "))
    productos.append(Producto(nombre, precio_unitario, cantidad_stock))

print("\nPRODUCTOS REGISTRADOS")
for producto in productos:
    print(producto)
    print()
