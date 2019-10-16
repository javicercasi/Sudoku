import unittest

from ingreso import Interfaz

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




if __name__ == '__main__':
    unittest.main()