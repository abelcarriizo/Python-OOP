import unittest
from person import Person
from repository import Repository
from service import Service

class TestPersonaService(unittest.TestCase):
    #Test comprobacion creacion del objeto
    def testPerson(self):
        person = Person(123, 'Abel', 'Carrizo', 'acarrizo@email.com')
        self.assertEqual(person.dni, 123)

    #Test repositorio inicial
    def testRepositorio(self):
        repository = Repository()
        self.assertEqual(len(repository.people), 0)

    #Test Servicio
    #Añadir un valor al repositorio
    def testService1(self):
        service = Service()
        person = Person(123, 'Abel', 'Carrizo', 'acarrizo@email.com')
        service.add(person)
        self.assertEqual(len(service.repository.people), 1)

    #Añadir mas de un valor al repositorio
    def testService2(self):
        service = Service()
        person1 = Person(123, 'Abel', 'Carrizo', 'acarrizo@email.com')
        service.add(person1)

        person2 = Person(345, 'Juan', 'Gomez', 'jgomez@email.com')
        service.add(person2)
        
        person3 = Person(678, 'Gomez', 'Juan', 'jgomez@email.com')
        service.add(person3)

        self.assertEqual(len(service.repository.people), 3)

    #Error al añadir un mismo valor
    def testService3(self):
        service = Service()
        person1 = Person(123, 'Abel', 'Carrizo', 'acarrizo@email.com')
        service.add(person1)

        person2 = Person(123, 'Juan', 'Gomez', 'jgomez@email.com')

        self.assertRaises(Exception, service.add(person2))

    #Actualizar un valor
    def testService4(self):
        service = Service()
        person1 = Person(123, 'Abel', 'Carrizo', 'acarrizo@email.com')
        service.add(person1)

        person2 = Person(123, 'Juan', 'Gomez', 'jgomez@email.com')
        service.update(person2, 123)

        self.assertNotEqual(service.repository.people, person2)

    #Borrar un valor
    def testService5(self):
        service = Service()
        person1 = Person(123, 'Abel', 'Carrizo', 'acarrizo@email.com')
        service.add(person1)

        service.delete(123)
        self.assertEqual(len(service.repository.people), 0)

    #Ver todo
    def testService6(self):
        service = Service()
        person1 = Person(123, 'Abel', 'Carrizo', 'acarrizo@email.com')
        service.add(person1)

        person2 = Person(456, 'Juan', 'Gomez', 'jgomez@email.com')
        service.add(person2)
        
        self.assertEqual(len(service.findAll()), 2)

if __name__=='__main__':
    unittest.main()