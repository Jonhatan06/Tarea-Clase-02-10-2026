"""Ejercicio 9: Turnos de un consultorio."""


class Turno:
    def __init__(self, paciente, hora):
        self.paciente = paciente
        self.hora = hora
        self.estado = "Pendiente"

    def marcar_atendido(self):
        self.estado = "Atendido"
        print(f"Turno de {self.paciente} marcado como atendido.")

    def __str__(self):
        return f"{self.hora} - {self.paciente} ({self.estado})"


class Agenda:
    def __init__(self, fecha):
        self.fecha = fecha
        self.turnos = []

    def agendar_turno(self, turno):
        self.turnos.append(turno)
        print(f"Turno agendado para {turno.paciente} a las {turno.hora}.")

    def listar_pendientes(self):
        pendientes = []
        for turno in self.turnos:
            if turno.estado == "Pendiente":
                pendientes.append(turno)
        return pendientes

    def mostrar_turnos(self):
        contenido = f"Turnos de la agenda del {self.fecha}:\n"
        for posicion in range(len(self.turnos)):
            contenido += f"{posicion + 1}. {self.turnos[posicion]}\n"
        return contenido.rstrip()

    def __str__(self):
        contenido = f"Turnos pendientes del {self.fecha}:\n"
        pendientes = self.listar_pendientes()

        if len(pendientes) == 0:
            contenido += "No hay turnos pendientes."
        else:
            for turno in pendientes:
                contenido += f"- {turno}\n"
        return contenido.rstrip()


fecha = input("Fecha de la agenda: ")
agenda = Agenda(fecha)

opcion = ""
while opcion != "5":
    print("\n1. Agendar turno")
    print("2. Marcar turno como atendido")
    print("3. Mostrar todos los turnos")
    print("4. Mostrar turnos pendientes")
    print("5. Finalizar")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        paciente = input("Nombre del paciente: ")
        hora = input("Hora del turno: ")
        agenda.agendar_turno(Turno(paciente, hora))
    elif opcion == "2":
        if len(agenda.turnos) == 0:
            print("No hay turnos agendados.")
        else:
            print(agenda.mostrar_turnos())
            numero_turno = int(input("Número del turno atendido: "))
            if 1 <= numero_turno <= len(agenda.turnos):
                agenda.turnos[numero_turno - 1].marcar_atendido()
            else:
                print("Número de turno no válido.")
    elif opcion == "3":
        print(agenda.mostrar_turnos())
    elif opcion == "4":
        print(agenda)
    elif opcion == "5":
        print("Agenda finalizada.")
    else:
        print("Opción no válida.")
