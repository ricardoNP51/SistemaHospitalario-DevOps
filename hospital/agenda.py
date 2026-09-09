"""Agenda en memoria con identificadores ficticios."""
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class Cita:
    paciente_id: str
    medico_id: str
    inicio: datetime


class Agenda:
    def __init__(self):
        self._citas = []

    @property
    def citas(self):
        return tuple(self._citas)

    def reservar(self, paciente_id, medico_id, inicio):
        if not paciente_id.strip() or not medico_id.strip():
            raise ValueError("Paciente y médico son obligatorios")
        if not isinstance(inicio, datetime):
            raise ValueError("La fecha debe ser datetime")
        paciente_id, medico_id = paciente_id.strip(), medico_id.strip()
        for cita in self._citas:
            if cita.inicio == inicio and (
                cita.medico_id == medico_id or cita.paciente_id == paciente_id
            ):
                raise ValueError("El horario ya está ocupado")
        cita = Cita(paciente_id, medico_id, inicio)
        self._citas.append(cita)
        return cita
