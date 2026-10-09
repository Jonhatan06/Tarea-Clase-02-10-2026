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


numero = input("Número de habitación: ")
tipo = input("Tipo de habitación: ")
tarifa_por_noche = int(input("Tarifa por noche en guaraníes, sin puntos: "))
habitacion = Habitacion(numero, tipo, tarifa_por_noche)

opcion = ""
while opcion != "5":
    print("\n1. Ocupar habitación")
    print("2. Liberar habitación")
    print("3. Calcular costo de estadía")
    print("4. Mostrar estado de la habitación")
    print("5. Finalizar")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        habitacion.ocupar()
        print(habitacion)
    elif opcion == "2":
        habitacion.liberar()
        print(habitacion)
    elif opcion == "3":
        cantidad_noches = int(input("Cantidad de noches: "))
        costo = habitacion.calcular_costo_estadia(cantidad_noches)
        print(f"Costo de la estadía: {costo:,.0f} Gs.")
    elif opcion == "4":
        print(habitacion)
    elif opcion == "5":
        print("Gestión de habitación finalizada.")
    else:
        print("Opción no válida.")
