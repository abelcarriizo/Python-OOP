from hangman import Hangman

def main():
    print('\nA H O R C A D O\n'.center(50, '-'))
    game = Hangman()
    while not game.is_over:
        print(f'Pistas: {game.board}')
        print(f'Letras usadas: {game.used_letters}')
        print(f'Vidas: {game.lifes_left}')
        
        letter = input('Ingrese una letra de la A a la Z: ')
        game.play(letter)

    if game.win:
        print('\nUsted gano!')
        print(f'PALABRA: {game.board}\n')
    else:
        print(f'Lo lamento, la palabra era: {game.secret_word}')


if __name__ == '__main__':
    main()
