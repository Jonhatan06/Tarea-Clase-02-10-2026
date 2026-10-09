"""Ejercicio 7: Control de stock con alertas."""


class Producto:
    def __init__(self, nombre, stock_inicial, stock_minimo):
        self.nombre = nombre
        self.stock = stock_inicial
        self.stock_minimo = stock_minimo

    def ingresar_mercaderia(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad
            print(f"Ingresaron {cantidad} unidades de {self.nombre}.")
        else:
            print("La cantidad a ingresar debe ser positiva.")
        self.mostrar_alerta()

    def registrar_venta(self, cantidad):
        if cantidad <= 0:
            print("La cantidad vendida debe ser positiva.")
        elif cantidad > self.stock:
            print(f"Venta rechazada: no hay suficientes unidades de {self.nombre}.")
        else:
            self.stock -= cantidad
            print(f"Venta registrada: {cantidad} unidades de {self.nombre}.")
        self.mostrar_alerta()

    def mostrar_alerta(self):
        if self.stock < self.stock_minimo:
            print(f"ALERTA: el stock de {self.nombre} está por debajo del mínimo.")

    def __str__(self):
        return (
            f"Producto: {self.nombre} | Stock actual: {self.stock} | "
            f"Stock mínimo: {self.stock_minimo}"
        )


nombre = input("Nombre del producto: ")
stock_inicial = int(input("Stock inicial: "))
stock_minimo = int(input("Stock mínimo: "))
producto = Producto(nombre, stock_inicial, stock_minimo)

opcion = ""
while opcion != "4":
    print("\n1. Ingresar mercadería")
    print("2. Registrar venta")
    print("3. Mostrar stock")
    print("4. Finalizar")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        cantidad = int(input("Cantidad que ingresa: "))
        producto.ingresar_mercaderia(cantidad)
        print(producto)
    elif opcion == "2":
        cantidad = int(input("Cantidad vendida: "))
        producto.registrar_venta(cantidad)
        print(producto)
    elif opcion == "3":
        print(producto)
    elif opcion == "4":
        print("Control de stock finalizado.")
    else:
        print("Opción no válida.")
