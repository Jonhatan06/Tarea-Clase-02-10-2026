"""Ejercicio 10: Carrito de compras de un e-commerce."""


class Producto:
    def __init__(self, nombre, precio_unitario):
        self.nombre = nombre
        self.precio_unitario = precio_unitario

    def __str__(self):
        return f"{self.nombre}: {self.precio_unitario:,.0f} Gs."


class Item:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self):
        return self.producto.precio_unitario * self.cantidad

    def __str__(self):
        return (
            f"{self.producto.nombre} x {self.cantidad} = "
            f"{self.subtotal():,.0f} Gs."
        )


class Carrito:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []

    def agregar_item(self, item):
        if item.cantidad > 0:
            self.items.append(item)
            print(f"Se agregó {item.cantidad} unidad(es) de {item.producto.nombre}.")
        else:
            print("La cantidad del ítem debe ser positiva.")

    def calcular_total(self):
        total = 0
        for item in self.items:
            total += item.subtotal()
        return total

    def __str__(self):
        detalle = f"Detalle de compra de {self.cliente}:\n"
        for item in self.items:
            detalle += f"- {item}\n"
        detalle += f"Total general: {self.calcular_total():,.0f} Gs."
        return detalle


cliente = input("Nombre del cliente: ")
carrito = Carrito(cliente)
cantidad_items = int(input("¿Cuántos productos desea agregar al carrito? "))

while cantidad_items < 1:
    cantidad_items = int(input("Ingrese por lo menos un producto: "))

for numero in range(1, cantidad_items + 1):
    print(f"\nDatos del producto {numero}")
    nombre = input("Nombre del producto: ")
    precio_unitario = int(input("Precio unitario en guaraníes, sin puntos: "))
    cantidad = int(input("Cantidad: "))
    producto = Producto(nombre, precio_unitario)
    carrito.agregar_item(Item(producto, cantidad))

print()
print(carrito)
