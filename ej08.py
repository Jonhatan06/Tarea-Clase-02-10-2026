"""Ejercicio 8: Reproductor de lista de canciones."""


class Cancion:
    def __init__(self, titulo, artista, duracion):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion

    def duracion_formateada(self):
        minutos = self.duracion // 60
        segundos = self.duracion % 60
        return f"{minutos}:{segundos:02d}"

    def __str__(self):
        return f"{self.titulo} - {self.artista} ({self.duracion_formateada()})"


class ListaReproduccion:
    def __init__(self, nombre):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion):
        self.canciones.append(cancion)
        print(f"Se agregó: {cancion.titulo}.")

    def duracion_total(self):
        total = 0
        for cancion in self.canciones:
            total += cancion.duracion
        return total

    def __str__(self):
        contenido = f"Lista de reproducción: {self.nombre}\n"
        for cancion in self.canciones:
            contenido += f"- {cancion}\n"

        minutos = self.duracion_total() // 60
        segundos = self.duracion_total() % 60
        contenido += f"Duración total: {minutos}:{segundos:02d}"
        return contenido


nombre_lista = input("Nombre de la lista de reproducción: ")
lista = ListaReproduccion(nombre_lista)
agregar_otra = "si"

while agregar_otra == "si":
    print("\nDatos de la canción")
    titulo = input("Título: ")
    artista = input("Artista: ")
    duracion = int(input("Duración en segundos: "))
    lista.agregar_cancion(Cancion(titulo, artista, duracion))
    agregar_otra = input("¿Desea agregar otra canción? (si/no): ").lower()

print()
print(lista)
