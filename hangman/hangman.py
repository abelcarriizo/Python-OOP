import random

#Genera la palabra secreta
def choice():
    words = ['PERRO', 'GATO', 'ABUELO', 'HOMOSENSUAL', 'HOLA', 'PAPA', 'MESSI', 'BITCOIN']
    return random.choice(words)

class Hangman:
    def __init__(self):
        self.secret_word = choice() #Llama a la funcion 'choice' para establecer valor
        self.board = self.setBoard() #Llama al metodo 'setBoard' para generar el tablero
        self.letter = list()
        self.used_letters = list()
        self.lifes_left = 6
        self.win = False
        self.is_over = False
    
    #Genera el tablero
    def setBoard(self):
        board = ''
        for x in range(len(self.secret_word)):
            board += '_ '
        return board
        
    #Encargado de la jugabilidad
    def play(self, letter:str):
        self.letterCheck(letter)
        
        #Busca las posiciones de la palabra
        letter = letter.upper()
        count = -1
        positions = list()
        for x in self.secret_word:
            count += 1
            if x == letter:
                positions.append(count)
        
        #Genera un tablero temporal para agregar la letra en el tablero
        boardTemp = list()
        for y in self.board:
            if y != ' ':
                boardTemp.append(y)
                
        #Agrega la letra en el tablero temporal
        for z in positions:
            boardTemp[z] = letter
        
        #Asigna los valores del tablero temporal en el verdadero tablero        
        self.board = ' '.join(boardTemp) 
        
        word = ''.join(boardTemp)
        self.checkWin(word) 
    
    #Verifica las letras usadas          
    def letterCheck(self, letter:str):
        if letter not in self.used_letters:
            self.used_letters.append(letter)
            if letter not in self.secret_word:
                if self.lifes_left != 0: 
                    self.lifes_left -= 1 
                    if self.lifes_left == 0:
                        self.is_over = True
                else: self.is_over = True
      
     #Verifica si la partida termino       
    def checkWin(self, word):  
        if word == self.secret_word:
            self.win = True
            self.is_over = True
    
if __name__=='__main__':
    pass