"""Ejercicio 11: Estudiante y sus materias."""


class Estudiante:
    def __init__(self, nombre, nota_minima=7):
        self.nombre = nombre
        self.nota_minima = nota_minima
        self.notas = {}

    def registrar_nota(self, materia, nota):
        if 0 <= nota <= 10:
            self.notas[materia] = nota
            print(f"Nota de {materia} registrada: {nota}.")
        else:
            print("La nota debe estar entre 0 y 10.")

    def calcular_promedio(self):
        if len(self.notas) == 0:
            return 0

        suma_notas = 0
        for nota in self.notas.values():
            suma_notas += nota
        return suma_notas / len(self.notas)

    def esta_aprobado(self):
        return self.calcular_promedio() >= self.nota_minima

    def __str__(self):
        boletin = f"Boletín de {self.nombre}\n"
        for materia, nota in self.notas.items():
            boletin += f"- {materia}: {nota}\n"

        condicion = "Aprobado" if self.esta_aprobado() else "No aprobado"
        boletin += f"Promedio: {self.calcular_promedio():.2f}\n"
        boletin += f"Condición final: {condicion}"
        return boletin


nombre = input("Nombre del estudiante: ")
estudiante = Estudiante(nombre)

print("Escriba las materias y sus notas. Para finalizar, escriba fin como materia.")
materia = input("Materia: ")

while materia.lower() != "fin":
    nota = int(input("Nota de 0 a 10: "))
    estudiante.registrar_nota(materia, nota)
    materia = input("Materia: ")

print()
print(estudiante)
