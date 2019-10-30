import unittest
from parameterized import parameterized

from sudo import Sudoku


class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.game = Sudoku(["53xx7xxxx",
                            "6xx195xxx",
                            "x98xxxx6x",
                            "8xxx6xxx3",
                            "4xx8x3xx1",
                            "7xxx2xxx6",
                            "x6xxxx28x",
                            "xxx419xx5",
                            "xxxx8xx79"], 9)
        self.assertTrue(self.game.is_playing)

        self.game_4 = Sudoku (["432x",
                               "x1x3",
                               "xxxx",
                               "143x"], 4)


    def test_error_escribir_en_fijo_9x9(self):

        self.assertFalse(self.game.valores_fijos(0, 0))


    @parameterized.expand([
        (0,0),
        (1,1),
        (3,0)
    ])
    def test_control_fijos_4x4_ocupado(self,fila,columna):
        self.assertFalse(self.game_4.valores_fijos(fila,columna))
    
    @parameterized.expand([
        (0,3),
        (1,0),
        (2,0)
    ])
    def test_control_fijos_4x4_disponible(self,fila,columna):
        self.assertTrue(self.game_4.valores_fijos(fila,columna))

    @parameterized.expand([
        (0,0),
        (1,0),
        (5,0)
    ])
    def test_control_fijos_9x9_ocupado(self,fila,columna):
        self.assertFalse(self.game.valores_fijos(fila,columna))

    @parameterized.expand([
        (0,2),
        (0,8),
        (8,5)
    ])
    def test_control_fijos_9x9_disponible(self,fila,columna):
        self.assertTrue(self.game.valores_fijos(fila,columna))

    @parameterized.expand([
        (8, 6, '8'),
        (2, 0, '7'),
        (2, 8, '9'),
        (8, 3, '1'),
        (7, 7, '6')
    ])
    def test_filacolumna_repetida_9x9(self, fila, columna, valor):

        self.assertFalse(self.game.repeticion_fila_columna(fila, columna, valor))

    @parameterized.expand([
        (8, 6, '1'),
        (2, 0, '2'),
        (2, 8, '4'),
        (8, 3, '2'),
        (7, 7, '3')
    ])

    def test_filacolumna_disponible_9x9(self, fila, columna, valor):

        self.assertTrue(self.game.repeticion_fila_columna(fila, columna, valor))


    @parameterized.expand([
        (1,0,'1'),
        (1,0,'4'),
        (2,1,'3')
    ])
    def test_filacolumna_repetida_4x4(self,fila,columna,valor):
        self.assertEqual(self.game_4.repeticion_fila_columna(fila,columna,valor), False)

    @parameterized.expand([
        (2,3,'4'),
        (3,3,'2'),
        (2,0,'2'),
        (1,2,'4'),
        (2,1,'2'),
        (0,3,'1')
    ])
    def test_filacolumna_disponible_4x4(self,fila,columna,valor):
        self.assertTrue(self.game_4.repeticion_fila_columna(fila,columna,valor))
    
    @parameterized.expand([
        (8, 4, '7'),
        (0, 5, '1'),
        (2, 5, '9'),
        (8, 5, '3'),
        (3, 5, '5'),
        (7, 5, '6'),
        (4, 5, '7'),
        (8, 6, '2'),
        (0, 6, '2'),
        (4, 6, '3'),
        (2, 6, '9'),
        (6, 6, '5'),
        (3, 6, '8'),
        (3, 0, '2'),
        (5, 0, '3'),
        (7, 0, '5'),
        (8, 0, '6'),
        (0, 0, '7'),
        (1, 0, '8'),
        (6, 1, '1'),
        (1, 1, '6'),
        (0, 1, '3'),
        (2, 1, '6'),
        (3, 1, '7'),
        (7, 1, '5'),
        (0, 2, '7'),
        (2, 2, '3'),
        (3, 2, '4'),
        (1, 2, '5'),
        (4, 2, '1'),
        (6, 2, '8'),
        (4, 3, '1'),
        (8, 3, '9'),
        (6, 3, '8'),
        (0, 3, '5'),
        (3, 3, '6'),
        (1, 3, '7'),
        (1, 4, '1'),
        (5, 4, '2'),
        (4, 4, '4'),
        (6, 4, '6'),
        (1, 7, '7'),
        (7, 7, '1'),
        (6, 7, '2'),
        (5, 7, '6'),
        (2, 7, '7'),
        (2, 8, '5'),
        (3, 8, '1'),
        (4, 8, '2'),
        (1, 8, '3'),
        (5, 8, '5'),
        (0, 8, '6'),
    ])
    def test_error_repeticion_zona_filacolumna_9x9(self,fila,columna,valor):
    
        self.assertFalse(self.game.general(fila,columna,valor))

    @parameterized.expand([
        (1,7,'4'),    
        (0,7,'1'),
        (1,1,'4'),   
        (2,4,'4'),    
        (8,3,'3'), 
        (4,1,'2'),    
        (4,4,'5'),    
        (4,7,'2'),   
        (7,1,'2'), 
        (7,7,'3') 
    ])

    def test_ingreso_correcto_9x9(self,fila,columna,valor):

        self.assertTrue(self.game.general(fila, columna, valor))

    @parameterized.expand([
        (0,1,'7'),
        (0,4,'1'),
        (1,0,'6'),
        (8,8,'3'),
        (8,7,'1'),
        (8,4,'7'),
        (5,8,'2'),
        (5,0,'4'),
        (7,5,'8'),
        (0,0,'8')
        ])

    def test_escribir_en_valor_fijo_9x9(self,fila,columna,valor):

        self.assertFalse(self.game.general(fila,columna,valor))

    @parameterized.expand([
        (1,1,'5'),
        (8,0,'6'),
        (8,6,'5')
    ])
    def test_repeticion_zona_9x9(self,fila,columna,valor):
        self.assertFalse(self.game.repeticion_zona(fila,columna,valor))

    @parameterized.expand([
        (1,1,'2'),
        (8,0,'1'),
        (8,6,'4')
    ])
    def test_disponible_zona_9x9(self,fila,columna,valor):
        self.assertTrue(self.game.repeticion_zona(fila,columna,valor))


    def test_valor_disponible_9x9(self):

        self.assertTrue(self.game.valores_fijos(1, 1))
        self.assertTrue(self.game.repeticion_fila_columna(0, 8, '4'))
        self.assertTrue(self.game.repeticion_zona(8, 1, '1'))
        self.assertEqual(self.game.escribir(8, 1, '1'),'1')

    def test_valor_disponible_zona_9x9(self):

        self.assertTrue(self.game.repeticion_zona(3, 7, '7'))

    def test_sobreescribir_espacio_disponible_9x9(self):
        self.assertEqual(self.game.escribir(0, 7, '4'), '4')

    def test_sobreescribir_espacio_disponible_2_9x9(self):
        self.assertTrue(self.game.general(0, 7, '2'))
        self.assertEqual(self.game.escribir(0, 7, '2'), '2')

    def test_ingreso_incorrecto_por_repeticion_9x9(self):
        self.assertTrue(self.game.escribir(8, 0, '3'), 'x')

    def test_game_over_9x9(self):

        self.game = Sudoku(["261375894",
                            "537894162",
                            "948216357",
                            "694751238",
                            "825943671",
                            "713628945",
                            "356482719",
                            "489167523",
                            ], 9)

        self.assertEqual(self.game.fin_juego(), True)

    def test_game_over_9x9(self):

        self.game = Sudoku(["533175384", "612195537", "298376369", "882668363",
                            "481863981", "71732x356", "169836281", "916419925",
                            "816288179"], 9)

        self.assertEqual(self.game.fin_juego(), False)

    def test_error_escribir_en_fijo_4x4(self):

        self.assertFalse(self.game_4.valores_fijos(0, 0))

    def test_test_ingreso_correcto_4x4(self):


        self.assertTrue(self.game_4.general(0, 3, '1'))
        self.assertEqual(self.game_4.escribir(0, 3, '1'), '1')

    @parameterized.expand([
        (0, 3, '1'),
        (1, 0, '2'),
        (2, 0, '3'),
        (2, 1, '2'),
        (3, 3, '2')
    ])
    def test_ingreso_correcto_4x4(self, fila, columna, valor):


        self.assertTrue(self.game_4.general(fila, columna, valor))
        self.assertEqual(self.game_4.escribir(fila, columna, valor), valor)


    def test_fin_tablero_4x4_incompleto(self):
        self.game_4 = Sudoku (["4321",
                               "2143",
                               "3x14",
                               "1432"], 4)
        self.assertFalse(self.game_4.fin_juego())

    def test_fin_tablero_4x4_completo(self):
        self.game_4 = Sudoku (["4321",
                               "2143",
                               "3214",
                               "1432"], 4)
        self.assertTrue(self.game_4.fin_juego()) 

       




if __name__ == '__main__':
    unittest.main()
