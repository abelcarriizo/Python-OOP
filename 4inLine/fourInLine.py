#Abel Carrizo
ficha1 = 'X'
ficha2 = 'O'
jugador1 = 1
jugador2 = 2 

class FourinLine:
    def __init__(self):
        self.filas = 8
        self.columnas = 8
        self.tablero = list()
        self.vacio = ' '
        self.linea = 4
        self.ficha = ficha1
        self.jugador = jugador1
        self.ganador = None  
        
    """ TABLERO """
    
    #Creacion del tablero 
    def crearTablero(self):
        self.tablero = [[self.vacio for columna in range(self.columnas)] for fila in range(self.filas)]
        return self.tablero
    
    """ JUGABILIDAD """
    
    #Dejar caer Ficha
    def añadirFicha(self, columna:int):
        fila = self.chequeoColumna(columna)
        if fila == -1:
            return 'Columna llena'
        self.tablero[fila][columna] = self.ficha
        if self.condicionGanador(self.ficha):
            self.ganador = self.jugador
        self.cambioJugador()

        
    #Compruba si la columna de la ultima fila tiene una ficha
    def chequeoColumna(self, columna:int):
        indice = len(self.tablero) - 1
        while indice >= 0:
            if self.tablero[indice][columna] == self.vacio:
                return indice
            indice -= 1
        return -1
        
    #Cambio Jugador
    def cambioJugador(self):
        if self.jugador == jugador1:
            self.jugador = jugador2
        else:
            self.jugador = jugador1
        self.cambioFicha()        
            
    #CambioFicha
    def cambioFicha(self):
        if self.jugador == jugador2:
            self.ficha = ficha2
        else:
            self.ficha = ficha1
        
    """ CONDICION PARA GANAR """

    def condicionGanador(self, ficha):
        #Chequeo posiciones HORIZONTALES para ganar la partida
        for c in range(self.columnas - 3):
            for r in range(self.filas):
                if self.tablero[r][c] == ficha and self.tablero[r][c+1] == ficha and self.tablero[r][c+2] == ficha and self.tablero[r][c+3] == ficha:
                    return True
       
        #Chequeo posiciones VERTICALES para ganar la partida
        for c in range(self.columnas):
            for r in range(self.filas - 3):
                if self.tablero[r][c] == ficha and self.tablero[r+1][c] == ficha and self.tablero[r+2][c] == ficha and self.tablero[r+3][c] == ficha:
                    return True
                    
        #Chequeo posiciones Positivas de DIAGONALES para ganar la partida  
        for c in range(self.columnas - 3):
            for r in range(self.filas - 3):
                if self.tablero[r][c] == ficha and self.tablero[r+1][c+1] == ficha and self.tablero[r+2][c+2] == ficha and self.tablero[r+3][c+3] == ficha:
                    return True
        
        #Chequeo posiciones Negativas de DIAGONALES para ganar la partida  
        for c in range(self.columnas - 3):
            for r in range(3, self.filas): #El 3 indica apartir de que fila seria posible
                if self.tablero[r][c] == ficha and self.tablero[r-1][c+1] == ficha and self.tablero[r-2][c+2] == ficha and self.tablero[r-3][c+3] == ficha:
                    return True
                
        return False
    
    """ METODOS DE IMPRESION POR PANTALLA """  
    
    def imprimirTablero(self):
        #Inicio
        print("|", end="")
        for f in range(0, len(self.tablero[0])):
            print(f, end="|")
        print("")
        
        #Datos
        for fila in self.tablero:
            print('|', end='')
            for valor in fila:
                print(valor, end='')
                print('|', end='')
            print('') 
        
        #Fin
        print('+', end='')
        for x in range(1, len(self.tablero[0]) + 1):
            print('-', end='+')
        print('')
    
    def imprimirTurno(self):
        print(f'Jugador 1: {ficha1} | Jugador 2: {ficha2}')
        if self.jugador == jugador1:
            print(f'Turno del jugador 1: ({ficha1})')
        else:
            print(f'Turno del jugador 2: ({ficha2})')
    
    def imprimirGanador(self):
        print(f'JUGADOR {self.ganador} HA GANADO')