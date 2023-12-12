from person import Person

class Repository:
    def __init__ (self):
        self.people = dict()

    def add(self, person: Person()):
        if person.dni in self.people:
            raise KeyError('Clave Existente')
        self.people[person.dni] = person

    def update(self, newPerson: Person, dni: int):
        if dni not in self.people:
            raise KeyError('Clave inexistente')
        self.people[dni] = newPerson
        return self.people[dni]

    def delete(self, dni: int):
        if dni not in self.people:
            raise KeyError('Clave inexistente')
        del self.people[dni]

    def findAll(self):
        return list(self.people.values())
    
    def findLast(self):
        list(self.people.values())[-1]

    def findDNI(self, dni: int):
        if dni not in self.people:
            raise KeyError('Clave Inexistente')
        return self.people[dni]

    def writeFile(self):
        with open ('persona.txt', 'w') as file:
            for person in self.peoples.values():
                file.write(f'{person.dni}, {person.name}, {person.lastname}, {person.email};\n')

    def readFile(self):
        with open('persona.txt', 'r') as file:
            for line in file:
                print(line)

if __name__ == '__main__':
    repository = Repository()
    print(repository)
