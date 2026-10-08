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


libro_1 = Libro("Yo, el Supremo", "Augusto Roa Bastos", True)
libro_2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", False)

print(libro_1)
print()
print(libro_2)
