import unittest
from datetime import datetime
from hospital.agenda import Agenda


class AgendaTests(unittest.TestCase):
    def setUp(self):
        self.agenda = Agenda()
        self.hora = datetime(2026, 9, 15, 9)

    def test_reserva_valida(self):
        cita = self.agenda.reservar("P001", "M001", self.hora)
        self.assertEqual(self.agenda.citas, (cita,))

    def test_medico_no_puede_tener_dos_citas_simultaneas(self):
        self.agenda.reservar("P001", "M001", self.hora)
        with self.assertRaises(ValueError):
            self.agenda.reservar("P002", "M001", self.hora)

    def test_paciente_no_puede_tener_dos_citas_simultaneas(self):
        self.agenda.reservar("P001", "M001", self.hora)
        with self.assertRaises(ValueError):
            self.agenda.reservar("P001", "M002", self.hora)

    def test_rechaza_identificador_vacio(self):
        with self.assertRaises(ValueError):
            self.agenda.reservar(" ", "M001", self.hora)

    def test_rechaza_fecha_invalida(self):
        with self.assertRaises(ValueError):
            self.agenda.reservar("P001", "M001", "mañana")

    def test_permite_otro_horario(self):
        self.agenda.reservar("P001", "M001", self.hora)
        self.agenda.reservar("P001", "M001", datetime(2026, 9, 15, 10))
        self.assertEqual(len(self.agenda.citas), 2)
