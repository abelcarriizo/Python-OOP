#Abel Carrizo
class Member:
    def __init__(self, name='', surname='', age='', phone=''):
        self._name = name.upper()
        self._surname = surname.upper()
        self._age = age
        self._phone = phone
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new:str):
        self._name = new.upper()
        
    @property
    def surname(self):
        return self._surname
    
    @surname.setter
    def surname(self, new:str):
        self._surname = new.upper()
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new:int):
        self._age = new
        
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, new:int):
        self._phone = new