import unittest
from SimpleCoffeeMachine import MaquinaCafeSimple

class TestMaquinaCafeSimple(unittest.TestCase):    
    def testInicial(self):
        cafeSimple = MaquinaCafeSimple()
        self.assertEqual(cafeSimple.reservas['cafe'], 0)
        self.assertEqual(cafeSimple.reservas['agua'], 0)
        self.assertEqual(cafeSimple.reservas['azucar'], 0)
        
    #Almacena una vez
    def testAlmacenar1(self): 
        cafeSimple = MaquinaCafeSimple()
        cafeSimple.almacenar(10, 20, 30)
        self.assertEqual(cafeSimple.reservas['cafe'], 10)
        self.assertEqual(cafeSimple.reservas['agua'], 20)
        self.assertEqual(cafeSimple.reservas['azucar'], 30)
     
    #Almacena dos veces   
    def testAlmacenar2(self):
        cafeSimple = MaquinaCafeSimple()
        cafeSimple.almacenar(10, 20, 30)
        cafeSimple.almacenar(30, 20, 10)
        self.assertEqual(cafeSimple.reservas['cafe'], 40)
        self.assertEqual(cafeSimple.reservas['agua'], 40)
        self.assertEqual(cafeSimple.reservas['azucar'], 40)
     
    """
    ----------------PREPARACION CAFE-------------------
    Ingredientes que utiliza la maquina de cafe simple:
        cafe = 5
        agua = 10
        azucar = 3
    """   
    
    def testConAzucar(self):
        cafeSimple = MaquinaCafeSimple()
        cafeSimple.almacenar(10, 20, 30)
        cafeSimple.conAzucar()
        self.assertEqual(cafeSimple.reservas['cafe'], 5)
        self.assertEqual(cafeSimple.reservas['agua'], 10)
        self.assertEqual(cafeSimple.reservas['azucar'], 27)
    
    def testSinAzucar(self):
        cafeSimple = MaquinaCafeSimple()
        cafeSimple.almacenar(10, 20, 2)
        cafeSimple.sinAzucar()
        self.assertEqual(cafeSimple.reservas['cafe'], 5)
        self.assertEqual(cafeSimple.reservas['agua'], 10)
        self.assertEqual(cafeSimple.reservas['azucar'], 2)
        
    #Error por falta de todos los recursos
    def testErrorIngredientesTodos(self):
        cafeSimple = MaquinaCafeSimple()
        with self.assertRaises(ValueError):
            cafeSimple.conAzucar()
            
    #Error por falta de cafe
    def testErrorIngredientesCafe(self):
        cafeSimple = MaquinaCafeSimple()
        cafeSimple.almacenar(4, 20, 30)
        with self.assertRaises(ValueError):
            cafeSimple.conAzucar()
    
    #Error por falta de agua
    def testErrorIngredientesAgua(self):
        cafeSimple = MaquinaCafeSimple()
        cafeSimple.almacenar(10, 4, 30)
        with self.assertRaises(ValueError):
            cafeSimple.conAzucar()
    
    #Error por falta de azucar
    def testErrorIngredientesAzucar(self):
        cafeSimple = MaquinaCafeSimple()
        cafeSimple.almacenar(10, 20, 2)
        with self.assertRaises(ValueError):
            cafeSimple.conAzucar()  

if __name__=='__main__':
    unittest.main()