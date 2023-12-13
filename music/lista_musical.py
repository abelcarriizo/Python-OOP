#Abel Carrizo
from tema_musical import TemaMusical

class ListaMusical:
    def __init__(self):
        self.temas = dict() #Almacena informacion de la musica
    
    #Almacena la musica en temas  
    def add(self, valor):
        if valor.codigo in self.temas:
            raise KeyError
        self.temas[valor.codigo] = valor
    
    #Actualiza la musica a partir del objeto        
    def update(self, objeto, codigo):
        if codigo not in self.temas:
            raise KeyError()
        self.temas[codigo] = objeto
        
    def delete(self, codigo):
        if codigo not in self.temas:
            raise KeyError
        del self.temas[codigo]
    
    def find_by_id(self, codigo):
        if codigo not in self.temas:
            raise KeyError    
        return self.temas[codigo]
    
    def find_all(self):
        temas = list()
        for key in self.temas:
            temas.append(self.temas[key])
        return temas
        
    