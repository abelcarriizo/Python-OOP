#Abel Carrizo
from fourInLine import FourinLine

def jugar():
    print(' 4  E N  L I N E A '.center(50, '-'))
    juego = FourinLine()
    juego.crearTablero()
    try:
        while True:
            juego.imprimirTablero()
            juego.imprimirTurno()
            opcion = int(input('Indicar columna en donde ingresara la ficha: '))
            juego.añadirFicha(opcion)
            if juego.ganador != None:
                juego.imprimirTablero()
                juego.imprimirGanador()
                return volverJugar()
    except Exception as e:
        print(f'Ocurrio un error: {e}')   

def volverJugar():
    eleccion = input("¿Quieres seguir jugando? [s/n] ").lower()
    if eleccion == "s":
        jugar()
    elif eleccion == "n":
        print('OK')
        return False

if __name__=='__main__':
    jugar()