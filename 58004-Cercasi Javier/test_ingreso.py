import unittest
from unittest.mock import patch, MagicMock
import unittest.mock
from ingreso import Interfaz
from parameterized import parameterized

class TestIngreso(unittest.TestCase):

    def setUp(self):
        self.valor = Interfaz()
        self.tamaño = 9

    def test_numero_mayor(self):
        self.assertEqual(self.valor.ingreso_numero(10, self.tamaño), False)

    def test_numero_menor(self):
        self.assertEqual(self.valor.ingreso_numero(0, self.tamaño), False)

    def test_numero_en_rango(self):
        self.assertEqual(self.valor.ingreso_numero(5, self.tamaño), True)

    def test_posicion_1(self):
        self.assertEqual(self.valor.ingreso_coordenadas(5, 6, self.tamaño), True)
    
    def test_posicion_2(self):
        self.assertEqual(self.valor.ingreso_coordenadas(1, 11, self.tamaño), False)
    
    def test_posicion_3(self):
        self.assertEqual(self.valor.ingreso_coordenadas(14, 8, self.tamaño), False)

    def test_posicion_3(self):
        self.assertEqual(self.valor.ingreso_coordenadas(2, 4, self.tamaño), True)
    
    def test_dimension_correcta(self):
        self.assertTrue(self.valor.dimension(4))

    def test_dimension_incorrecta(self):
        self.assertFalse(self.valor.dimension(25))

    def test_dimension_incorrecta_2(self):
        self.assertFalse(self.valor.dimension('asdasd'))

    def test_dimension_incorrecta_3(self):
        self.assertFalse(self.valor.dimension('0'))

    def escribir_valor_incorrecto_9x9(self):
        self.assertEqual(self.valor.ingreso_numero('x', self.tamaño), False)

    def test_posicion_4x4(self):
        self.tamaño=4
        self.assertEqual(self.valor.ingreso_coordenadas(4, 3, self.tamaño), True)

    def test_posicion_4x4(self):
        self.tamaño=4
        self.assertEqual(self.valor.ingreso_coordenadas(2, 4, self.tamaño), True)

    


if __name__ == '__main__':
    unittest.main()