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

    def __str__(self):
        contenido = f"Turnos pendientes del {self.fecha}:\n"
        pendientes = self.listar_pendientes()

        if len(pendientes) == 0:
            contenido += "No hay turnos pendientes."
        else:
            for turno in pendientes:
                contenido += f"- {turno}\n"
        return contenido.rstrip()


agenda = Agenda("08/10/2026")
turno_1 = Turno("Sofía López", "08:00")
turno_2 = Turno("Miguel Duarte", "09:00")
turno_3 = Turno("Paula Acosta", "10:00")

agenda.agendar_turno(turno_1)
agenda.agendar_turno(turno_2)
agenda.agendar_turno(turno_3)
print()

turno_1.marcar_atendido()
turno_3.marcar_atendido()
print()
print(agenda)
