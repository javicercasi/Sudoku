import sys
import math

class Sudoku():

    def __init__(self, tabla, tamano):
        self.tamano = tamano 
        self.is_playing = True
        self.matriz = [ [ 0 for __ in range(self.tamano) ] for _ in range(self.tamano) ]
        self.fijos = [ [ 0 for __ in range(self.tamano) ] for _ in range(self.tamano) ]
        self.string_converter(tabla)

    def string_converter(self,tabla):
        #Este metodo chequeara las posiciones de los valores fijos
        for i in range (self.tamano):
            for j in range (self.tamano):
                self.matriz[i][j]=tabla[i][j]
                self.fijos[i][j]=tabla[i][j] 

#Chequearemos que si el valor de mi matriz es distinto de x, es porque 
# Posee un valor fijo de fabrica, me devuelve un true 
    def valores_fijos(self,m,n):
        #print(self.fijos[m][n])
        return self.fijos[m][n] == "x"

    def repeticion_fila_columna(self,fila,columna,valor):
        #Chequearemos las columnas, dejando cada fila fija
        
        for i in range(self.tamano):
            if self.matriz[i][columna]== valor:
                return (False)

            #Chequearemos las filas, dejando cada columna fija
            if self.matriz[fila][i]== valor:
                return False
            
        return True

    def repeticion_zona(self, fila, columna, valor):
        if (fila < int(math.sqrt(self.tamano ))):
            fila = 0

        elif (fila >= int(math.sqrt(self.tamano)) and fila < int(math.sqrt(self.tamano)*2)):
            fila = int(math.sqrt(self.tamano))
        else:
            fila = int(math.sqrt(self.tamano )*2)
        
        if (columna < int(math.sqrt(self.tamano ))):
            columna = 0
        elif (columna >= int(math.sqrt(self.tamano)) and columna < int(math.sqrt(self.tamano )*2)):
            columna = int(math.sqrt(self.tamano))
        else:
            columna = int(math.sqrt(self.tamano )*2)

        for i in range(int(math.sqrt(self.tamano))):
            for j in range(int(math.sqrt(self.tamano))):
                if (self.matriz[fila + i][columna + j] == valor):
                    return False
         
        return True

    def general(self, fila, columna, valor):
        paso = 0

        if self.valores_fijos(fila, columna) is False:
            paso += 0
        else:
            paso += 1

        if self.repeticion_fila_columna(fila, columna,valor) is False:
            paso += 0
        else:
            paso += 1
 
        if self.repeticion_zona(fila, columna, valor) is False:
            paso += 0
        else:
            paso += 1
        if paso == 3:
            return True
        else:
            return False
        
    
    def escribir(self,fila,columna,valor):

        if self.general(fila,columna,str(valor)):
            self.matriz[fila][columna] = str(valor)
            
        return (self.matriz[fila][columna])

    def fin_juego(self):
        print("\n")
        for i in range(self.tamano ):
                if ("x" in self.matriz[i]):
                    return False
        return True

    def tablero (self):
        a = ''
        for fila in self.matriz:
            a += ' | '.join(fila)
            a += '\n'
        return a