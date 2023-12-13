#Abel Carrizo
import unittest
from fourInLine import FourinLine

class TestFourLine(unittest.TestCase):
    def testInicial(self):
        juego = FourinLine()
        self.assertEqual(juego.tablero ,[])
        
    #Verifica el tamaño del tablero inicial
    def testCrearTablero1(self):
        juego = FourinLine()
        juego.crearTablero()
        self.assertEqual(len(juego.tablero), 8)
        for x in range(8):
            self.assertEqual(len(juego.tablero[x]), 8)
     
    #Verifica si las columnas del tablero inicial estan vacias
    def testCrearTablero2(self):
        juego = FourinLine()
        juego.crearTablero()
        valores = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        for x in range(8):
            self.assertEqual(juego.tablero[x], valores)
            
    #Verifica ubicacion de la ficha X
    def testAñadirFichaX(self):
        juego = FourinLine()
        juego.crearTablero()
        juego.añadirFicha(1)
        self.assertEqual(juego.tablero[7][1], 'X')
    
    #Verifica ubicacion de la ficha O
    def testAñadirFichaO(self):
        juego = FourinLine()
        juego.crearTablero()
        juego.añadirFicha(1)
        juego.añadirFicha(1)
        self.assertEqual(juego.tablero[6][1], 'O')
        
    #Verifica si el ganador es el Jugador 2 de forma horizontal
    def testAñadirGanadorHorizontal1(self):
        juego = FourinLine()
        juego.crearTablero()
        #primer columna
        juego.añadirFicha(0)
        juego.añadirFicha(0)
        #segunda columna
        juego.añadirFicha(1)
        juego.añadirFicha(1)
        #tercera columna
        juego.añadirFicha(2)
        juego.añadirFicha(2)
        #cuarta columna
        juego.añadirFicha(3)
        self.assertEqual(juego.ganador, 1)
    
    #Verifica si el ganador es el Jugador 2 de forma horizontal
    def testAñadirGanadorHorizontal2(self):
        juego = FourinLine()
        juego.crearTablero()
        #primer columna
        juego.añadirFicha(0)
        juego.añadirFicha(0)
        #segunda columna
        juego.añadirFicha(1)
        juego.añadirFicha(1)
        #tercera columna
        juego.añadirFicha(2)
        juego.añadirFicha(2)
        #primera columna
        juego.añadirFicha(0)
        #cuarta columna
        juego.añadirFicha(3)
        #primera columna
        juego.añadirFicha(0)
        #cuarta columna
        juego.añadirFicha(3)
        self.assertEqual(juego.ganador, 2)
        
    #Verifica si el ganador es el Jugador 1 de forma vertical
    def testAñadirGanadorVertical1(self):
        juego = FourinLine()
        juego.crearTablero()
        #primer fila
        juego.añadirFicha(0)
        juego.añadirFicha(1)
        #segunda fila
        juego.añadirFicha(0)
        juego.añadirFicha(1)
        #tercera fila
        juego.añadirFicha(0)
        juego.añadirFicha(1)
        #cuarta fila
        juego.añadirFicha(0)
        self.assertEqual(juego.ganador, 1)
        
    #Verifica si el ganador es el Jugador 2 de forma vertical
    def testAñadirGanadorVertical2(self):
        juego = FourinLine()
        juego.crearTablero()
        #primer fila
        juego.añadirFicha(0)
        juego.añadirFicha(1)
        #segunda fila
        juego.añadirFicha(0)
        juego.añadirFicha(1)
        #tercera fila
        juego.añadirFicha(0)
        juego.añadirFicha(1)
        #primera fila
        juego.añadirFicha(2)
        #cuartafila
        juego.añadirFicha(1)
        self.assertEqual(juego.ganador, 2)
        
    #Verifica si el ganador es el Jugador 1 de forma diagonal
    def testGanadorDiagonal1(self):
        juego = FourinLine()
        juego.crearTablero()
        #primer columna y segunda columna
        juego.añadirFicha(0)
        juego.añadirFicha(1)
        #segunda columna y tercer columna
        juego.añadirFicha(1)
        juego.añadirFicha(2)
        #primer columna y tercer culumna
        juego.añadirFicha(0)
        juego.añadirFicha(2)
        #tercer columna
        juego.añadirFicha(2)
        #cuarta columna
        juego.añadirFicha(3)
        juego.añadirFicha(3)
        juego.añadirFicha(3)
        juego.añadirFicha(3)
        self.assertEqual(juego.tablero[7][0], 'X')
        self.assertEqual(juego.tablero[6][1], 'X')
        self.assertEqual(juego.tablero[5][2], 'X')
        self.assertEqual(juego.tablero[4][3], 'X')


if __name__=='__main__':
    unittest.main()
