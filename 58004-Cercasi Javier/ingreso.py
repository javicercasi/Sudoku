from sudo import Sudoku
#from API import API
#import sys
#import math


class UserInput():

    def ingreso_numero(self, number, tamano):
        if(number > 0 and number <= tamano):
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
        number = 0
        fila = 0
        columna = 0
        while self.ingreso_numero(number, tamano) is False or self.ingreso_coordenadas(fila,
                                                                                       columna,
                                                                                       tamano) is False:
            try:
                fila = int(input("\n\nFila: "))
                columna = int(input("Columna: "))
                number = int(input("Valor de la casilla: "))
            except ValueError:
                pass
            if (self.ingreso_numero(number, tamano) and self.ingreso_coordenadas(fila,
                                                                                 columna,
                                                                                 tamano)):
                return fila - 1, columna - 1, number

            print("Ingresaste un valor no permitido, intentalo de nuevo")

    def play(self):
        jugar = Sudoku(["53xx7xxxx",
                        "6xx195xxx",
                        "x98xxxx6x",
                        "8xxx6xxx3",
                        "4xx8x3xx1",
                        "7xxx2xxx6",
                        "x6xxxx28x",
                        "xxx419xx5",
                        "xxxx8xx79"])
        self.ingresar_dimension()
        # crear sudoku...
        while not jugar.fin_juego():
            # mostrar tablero
            jugar.tablero()
            x, y, n = self.ingresar_valor(self.tamano)
            jugar.escribir(x, y, n)
            # jugar.
            # poner en el sudoku...


if __name__ == "__main__":
    u = UserInput()
    u.play()
