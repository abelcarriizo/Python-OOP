#Abel Carrizo
class Book:
    def __init__(self, name='', authorName='', memberLegajo=''):
        self._name = name.upper()
        self._authorName = authorName.upper()
        self._memberLegajo = memberLegajo
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new:str):
        self._name = new.upper()
        
    @property
    def authorName(self):
        return self._authorName
    
    @authorName.setter
    def authorName(self, new:str):
        self._authorName = new.upper()
        
    @property
    def memberLegajo(self):
        return self._memberLegajo
    
    @memberLegajo.setter
    def memberLegajo(self, new:int):
        self._memberLegajo = new