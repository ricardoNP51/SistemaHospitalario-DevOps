import unittest
from hospital.login import validar_campos_login


class LoginTests(unittest.TestCase):
    def test_acepta_campos_completos(self):
        self.assertTrue(validar_campos_login("estudiante", "valor-ficticio"))

    def test_rechaza_usuario_vacio(self):
        self.assertFalse(validar_campos_login("  ", "valor-ficticio"))

    def test_rechaza_clave_vacia(self):
        self.assertFalse(validar_campos_login("estudiante", " "))
