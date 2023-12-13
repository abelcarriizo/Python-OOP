#Abel Carrizo
from repositorios import Repositorios as repo

class ProductoService:
    
    def add_producto(self, producto):
        lastKey = 0
        for indice in repo.productosList:
            lastKey = indice
        lastKey += 1
        repo.productosList[lastKey] = producto.__dict__
        return lastKey
    
    def delete_producto(self, key):
        if key not in repo.productosList:
            raise ValueError
        else: del repo.productosList[key]
            
    def update_producto(self, key, producto):
        if key not in repo.productosList:
            raise ValueError
        repo.productosList[key] = producto.__dict__
        
        