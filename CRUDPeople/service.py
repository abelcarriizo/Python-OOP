from repository import Repository
from person import Person

class Service:
    def __init__(self) -> None:
        self.repository = Repository()

    def add(self, person: Person):
        try:
            return self.repository.add(person)
        except Exception as e:
            print(e)

    def update(self, newPerson: Person, dni):
        try:
            return self.repository.update(newPerson, dni)
        except Exception as e:
            print(e)

    def delete(self, dni: int):
        try:
            person = self.repository.findDNI(dni)
            self.repository.delete(person.dni)
            return person
        except Exception as e:
            print(e)
    
    def findAll(self):
        return self.repository.findAll()
    
    def findLast(self):
        return self.repositoriy.findLast()

    def findDNI(self):
        try:
            return self.repository.findDNI()
        except KeyError as e:
            print(e)
    
if __name__ == '__main__':
    pass