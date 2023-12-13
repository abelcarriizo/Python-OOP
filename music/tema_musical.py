#Abel Carrizo
class TemaMusical:
    def __init__(self, codigo=None, nombre=None, duracion=None, interprete=None):
        self._codigo = codigo
        self._nombre = nombre
        self._duracion = duracion
        self._interprete = interprete
        
    def __str__(self):
        return f'codigo: {self._codigo}\n\tnombre: {self._nombre}' + f'\n\tduracion: {self._duracion}\n\tinterprete: {self._interprete}\n'
    
    def input(self, valor=None):
        try:
            if valor != True:
                self.codigo = input('Ingrese codigo: \n> ')
            self.nombre = input('Ingrese nombre de la cancion: \n> ')
            self.duracion = int(input('Ingrese duracion del tema: \n> '))
            self.interprete = input('Ingrese nombre del interprete: \n> ')
        except ValueError as e:
            print(f'Ocurrio un error: {e}')
    
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, nuevo):
        if nuevo == '':
            raise EmptyError
        self._codigo = nuevo

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo):
        if nuevo == '':
            raise EmptyError
        self._nombre = nuevo
        
    @property
    def duracion(self):
        return self._duracion

    @duracion.setter
    def duracion(self, nuevo):
        if nuevo == -1:
            raise ValueError
        self._duracion = nuevo
        
    @property
    def interprete(self):
        return self._interprete

    @interprete.setter
    def interprete(self, nuevo):
        if nuevo == '':
            raise EmptyError
        self._interprete = nuevo
    

class EmptyError(Exception):
    pass

if __name__=='__main__':
    musica = TemaMusical('akdsjfñalk', 'El favor', 300, 'Las pastillas')
    print(musica)
    musica.input()