from sudo import Sudoku
from api import api
import sys
import math


class Interfaz():

    def ingreso_numero(self, valor, tamano):
        if(valor > 0 and valor <= tamano):
            return True
        else:
            return False

    def ingreso_coordenadas(self, fila, columna, tamano):
        if(fila > 0 and fila <= tamano and columna > 0 and columna <= tamano):
            return True
        else:
            return False

    def dimension(self, tamano):
        return (tamano == 4 or tamano == 9)

    def ingresar_dimension(self):
        self.tamano = 0
        while self.dimension(self.tamano) is False:
            try:
                self.tamano = int(input("Ingrese el tamano sudoku (4 o 9): "))
                if (self.dimension(self.tamano)):
                    return self.tamano
                print("Ingresaste un tamano no permitido, intentalo de nuevo")
            except ValueError:
                print("Ingresaste un tamano no permitido, intentalo de nuevo")

    def ingresar_valor(self, tamano):
        valor = 0
        fila = 0
        columna = 0
        while self.ingreso_numero(valor, tamano) is False or self.ingreso_coordenadas(fila,
                                                                                       columna,
                                                                                       tamano) is False:
            try:
                fila = int(input("\n\nFila: "))
                columna = int(input("Columna: "))
                valor = int(input("Valor de la casilla: "))
            except ValueError:
                pass
            if (self.ingreso_numero(valor, tamano) and self.ingreso_coordenadas(fila,
                                                                                 columna,
                                                                                 tamano)):
                return fila - 1, columna - 1, valor

            print("Ingresaste un valor no permitido, intentalo de nuevo")

    def play(self):
        
        print("\n\n         BIENVENIDO AL SUDOKU        \n\n")
        jugar = Sudoku(api(self.ingresar_dimension()),self.tamano)      #El resultado de la api se lo envia a la clase Sudoku
        
        while not jugar.fin_juego():
            
            print(jugar.tablero())      # mostrar tablero
            x, y, n = self.ingresar_valor(self.tamano)      #Le envia el valor del tamano al metodo ingresar_valor
            jugar.escribir(x, y, n)

        if jugar.fin_juego is True:
           print("             Has ganado!!!! Fin del juego             \n")
            


if __name__ == "__main__":
    I = Interfaz()
    I.play()
