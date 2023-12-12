class Person:
    def __init__(self, dni=None, name='', lastname='', email=''):
        self.dni = dni
        self.lastname = lastname
        self.name = name
        self.email = email

    def __repr__(self):
        return f'{self.dni}, {self.name}, {self.lastname}, {self.email}'

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, newValue):
        self.__dni = newValue

    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, newValue):
        self.__lastname = newValue

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newValue):
        self.__name = newValue

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, newValue):
        self.__email = newValue
        
if __name__ == '__main__':
    person1 = Person(123, 'Abel', 'Carrizo', 'acarrizo@email.com')
    print(person1)