import unittest
from unittest.mock import patch, MagicMock
import unittest.mock
from ingreso import Interfaz
from parameterized import parameterized

class TestIngreso(unittest.TestCase):

    def setUp(self):
        self.valor = Interfaz()
        self.tamano = 9
        self.tamano_4 =4

    def test_numero_mayor(self):
        self.assertEqual(self.valor.ingreso_numero(10, self.tamano), False)

    def test_numero_menor(self):
        self.assertEqual(self.valor.ingreso_numero(0, self.tamano), False)

    def test_numero_en_rango(self):
        self.assertEqual(self.valor.ingreso_numero(5, self.tamano), True)

    def test_posicion_1(self):
        self.assertEqual(self.valor.ingreso_coordenadas(5, 6, self.tamano), True)
    
    def test_posicion_2(self):
        self.assertEqual(self.valor.ingreso_coordenadas(1, 11, self.tamano), False)
    
    def test_posicion_3(self):
        self.assertEqual(self.valor.ingreso_coordenadas(14, 8, self.tamano), False)

    def test_posicion_3(self):
        self.assertEqual(self.valor.ingreso_coordenadas(2, 4, self.tamano), True)
    
    def test_dimension_correcta(self):
        self.assertTrue(self.valor.dimension(4))

    def test_dimension_incorrecta(self):
        self.assertFalse(self.valor.dimension(25))

    def test_dimension_incorrecta_2(self):
        self.assertFalse(self.valor.dimension('asdasd'))

    def test_dimension_incorrecta_3(self):
        self.assertFalse(self.valor.dimension('0'))

    def escribir_valor_incorrecto_9x9(self):
        self.assertEqual(self.valor.ingreso_numero('x', self.tamano), False)

    def test_posicion_4x4(self):
        
        self.assertEqual(self.valor.ingreso_coordenadas(4, 3, self.tamano_4), True)

    def test_posicion_4x4(self):
        self.assertEqual(self.valor.ingreso_coordenadas(2, 4, self.tamano_4), True)

    @parameterized.expand([
        (1, ),
        (2, ),
        (3, ),
        (4, ),
        (5, ),
        (6, ),
        (7, ),
        (8, ),
        (9, )   ])
    def test_ingreso_numero_correcto(self, valor):
        self.assertTrue(self.valor.ingreso_numero(valor,self.tamano))
    
if __name__ == '__main__':
    unittest.main()