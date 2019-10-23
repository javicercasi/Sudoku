import unittest
from parameterized import parameterized

from sudo import Sudoku


class TestSudoku(unittest.TestCase):
    def setUp(self):
        self.game=Sudoku([  "53xx7xxxx",
                            "6xx195xxx",
                            "x98xxxx6x",
                            "8xxx6xxx3",
                            "4xx8x3xx1",
                            "7xxx2xxx6",
                            "x6xxxx28x",
                            "xxx419xx5",
                            "xxxx8xx79"],9)
        self.assertTrue(self.game.is_playing)

    def test_error_escribir_en_fijo_9x9(self):

        self.assertFalse(self.game.valores_fijos(0,0))

    def test_error_repeticion_zona_filacolumna_9x9(self):
    
        self.assertFalse(self.game.repeticion_fila_columna(0,2,'7'))
        self.assertFalse(self.game.repeticion_zona(8,6,'2'))

    @parameterized.expand([
        (8,6,'8'),
        (2,0,'7')
    ])
    def test_error_fila_repetida_9x9(self,fila,columna,valor):
    
        self.assertFalse(self.game.general(fila,columna,valor))

    def test_escribir_en_valor_fijo_9x9(self):
        
        self.assertFalse(self.game.general(0,0,'8'))
        
    def test_valor_disponible_9x9(self):

        self.assertTrue(self.game.valores_fijos(1,1))
        self.assertTrue(self.game.repeticion_fila_columna(0,8,'4'))
        self.assertTrue(self.game.repeticion_zona(8,1,'1'))

    def test_valor_disponible_zona_9x9(self):
    
        self.assertTrue(self.game.repeticion_zona(3,7,'7'))

    def test_ingreso_correcto_9x9(self):
        
        self.assertTrue(self.game.general(0,7,'1'))
        self.assertEqual(self.game.escribir(0,7,'1'),'1')

    def test_sobreescribir_espacio_disponible_9x9(self):
        self.assertEqual(self.game.escribir(0,7,'4'),'4')

    def test_sobreescribir_espacio_disponible_2_9x9(self):
        self.assertTrue(self.game.general(0,7,'2'))
        self.assertEqual(self.game.escribir(0,7,'2'),'2')


    def test_ingreso_incorrecto_por_repeticion_9x9(self):
        self.assertTrue(self.game.escribir(8,0,'3'),'x')

    def test_game_over_9x9(self):
        
        self.game = Sudoku(["533175384", "612195537", "298376369", "882668363",
                 "481863981", "717328356", "169836281", "916419925",
                 "816288179"],9)

        self.assertEqual(self.game.fin_juego(), True)

    def test_game_over_9x9(self):
        
        self.game = Sudoku(["533175384", "612195537", "298376369", "882668363",
                 "481863981", "71732x356", "169836281", "916419925",
                 "816288179"],9)

        self.assertEqual(self.game.fin_juego(), False)
'''
    def test_error_escribir_en_fijo_4x4(self):
        
        self.game=Sudoku(  ["432x",
                            "x1x3",
                            "xxxx",
                            "143x"],4)

        self.assertFalse(self.game.valores_fijos(0,0))

    def test_test_ingreso_correcto_4x4(self):
        
        self.assertTrue(self.game.general(0,3,'3'))
        self.assertEqual(self.game.escribir(0,7,'3'),'3')
        
        self.game=Sudoku(  ["432x",
                            "x1x3",
                            "xxxx",
                            "143x"],4)

        self.assertFalse(self.game.valores_fijos(0,0))

    '''

    



    
        
  
  
if __name__ == '__main__':
    unittest.main()
