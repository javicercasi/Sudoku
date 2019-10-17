from sudoku import Sudoku
from api import api
#import sys
#import math


class UserInput():

    def ingreso_numero(self, number, tamaño):
        if(number > 0 and number <= tamaño):
            return True
        else:
            return False

    def ingreso_coordenadas(self, fila, columna, tamaño):
        if(fila > 0 and fila <= tamaño and columna > 0 and columna <= tamaño):
            return True
        else:
            return False

    

    def dimension(self, tamaño):
        return (tamaño == 4 or tamaño == 9)
    
    def ingresar_dimension(self):
        self.tamaño = 0
        while self.dimension(self.tamaño) is False:
            try:
                self.tamaño = int(input("Ingrese el tamaño del sudoku (4 o 9): "))
                if (self.dimension(self.tamaño)):
                    return self.tamaño
                print("Ingresaste un tamaño no permitido, intentalo de nuevo")
            except ValueError:
                print("Ingresaste un tamaño no permitido, intentalo de nuevo")
    
    def ingresar_valor(self, tamaño):
        number = 0
        fila = 0
        columna = 0
        while self.ingreso_numero(number, tamaño) is False or self.ingreso_coordenadas(fila,
                                                                                    columna,
                                                                                    tamaño) is False:
            try:
                fila = int(input("\n\nFila: "))
                columna = int(input("Columna: "))
                number = int(input("Valor: "))
            except ValueError:
                pass
            if (self.ingreso_numero(number, tamaño) and self.ingreso_coordenadas(fila,
                                                                                columna,
                                                                                tamaño)):
                return fila - 1, columna - 1, number
            
            print("Ingresaste un valor no permitido, intentalo de nuevo")

    
    def play(self):
        print ("......SUDOKU......\n")
        print("Intente llenar el tablero sin repetir valores en filas, columnas y bloques \n")
        jugar = Sudoku(api(self.ingresar_dimension()))
        #self.ingresar_dimension()
        while not jugar.juego_terminado():
            # mostrar tablero
            jugar.tabla()
            # jugar.write(*self.ingresar_valor(self.tamaño))
            x, y, n = self.ingresar_valor(self.tamaño)
            jugar.write(x, y, n)


if __name__ == "__main__":
    u = UserInput()
    u.play()