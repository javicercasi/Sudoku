import copy

class Sudoku():

    def __init__(self, tabla):
        self.is_playing = True
        self.matriz = [ [ 0 for __ in range(9) ] for _ in range(9) ]
        self.fijos = [ [ 0 for __ in range(9) ] for _ in range(9) ]
        self.string_converter(tabla)

    def string_converter(self,tabla):
        #Este metodo chequeara las posiciones de los valores fijos
        large=len(tabla)
        for i in range (len(tabla)):
            for j in range (9):
                self.matriz[i][j]=tabla[i][j]
                self.fijos[i][j]=tabla[i][j] 

#Chequearemos que si el valor de mi matriz es distinto de x, es porque 
# Posee un valor fijo de fabrica, me devuelve un true 
    def valores_fijos(self,m,n):
        #print(self.fijos[m][n])
        return self.fijos[m][n] == "x"

    def repeticion_fila_columna(self,fila,columna,valor):
        #Chequearemos las columnas, dejando cada fila fija
        
        for i in range(9):
            if self.matriz[i][columna]== valor:
                return (False)

            #Chequearemos las filas, dejando cada columna fija
            if self.matriz[fila][i]== valor:
                return False
            
        return True

    def repeticion_zona(self, fila, columna, valor):
        if (fila < 3):
            fila = 0
        elif (fila >= 3 and fila < 6):
            fila = 3
        else:
            fila = 6
        
        if (columna < 3):
            columna = 0
        elif (columna >= 3 and columna < 6):
            columna = 3
        else:
            columna = 6

        for i in range(3):
            for j in range(3):
                if (self.matriz[fila + i][columna + j] == valor):
                    return False
         
        return True

    def general(self, fila, columna, valor):
        paso = 0

        if self.valores_fijos(fila, columna) is False:
            print("Valor fijado de fabrica")
        else:
            paso += 1

        if self.repeticion_fila_columna(fila, columna,valor) is False:
            print("Valor repetido en fila y/o columna")
        else:
            paso += 1
 
        if self.repeticion_zona(fila, columna, valor) is False:
            print("Valor repetido en el bloque")
        else:
            paso += 1
        if paso == 3:
            return True
        else:
            return False
        
    
    def escribir(self,fila,columna,valor):

        if self.general(fila,columna,str(valor)) is True:
            self.matriz[fila][columna] = valor
            
        return (self.matriz[fila][columna])

    def fin_juego(self):
        for i in range(9):
                if ("x" in self.matriz[i]):
                    return False
            
        return True

    def tablero (self):
        for i in self.matriz:
            for j in i:
                print(j,end=' ')
            print(" ")
