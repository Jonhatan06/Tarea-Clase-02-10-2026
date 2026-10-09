"""Ejercicio 4: Libro de una biblioteca."""


class Libro:
    def __init__(self, titulo, autor, disponible):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def __str__(self):
        if self.disponible:
            estado = "Disponible"
        else:
            estado = "Prestado"

        return (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Estado: {estado}"
        )


libros = []
cantidad_libros = int(input("¿Cuántos libros desea registrar? (mínimo 2): "))

while cantidad_libros < 2:
    cantidad_libros = int(input("Ingrese una cantidad de 2 o más libros: "))

for numero in range(1, cantidad_libros + 1):
    print(f"\nDatos del libro {numero}")
    titulo = input("Título: ")
    autor = input("Autor: ")
    estado = input("Estado (disponible/prestado): ").lower()

    while estado != "disponible" and estado != "prestado":
        estado = input("Escriba disponible o prestado: ").lower()

    disponible = estado == "disponible"
    libros.append(Libro(titulo, autor, disponible))

print("\nLIBROS REGISTRADOS")
for libro in libros:
    print(libro)
    print()
