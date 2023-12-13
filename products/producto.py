#Abel Carrizo
class Producto:
    def __init__(self, descripcion='', precio='', tipo=''):
        self._descripcion = descripcion
        self._precio = precio
        self._tipo = tipo
        
    @property
    def descripcion(self):
        return self._descripcion
    
    @descripcion.setter
    def descripcion(self, new:str):
        self._descripcion = new
        
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, new:int):
        self._precio = new
    
    @property
    def tipo(self):
        return self._tipo
    
    @tipo.setter
    def tipo(self, new:str):
        self._tipo = new