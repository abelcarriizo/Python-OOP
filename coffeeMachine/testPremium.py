import unittest
from PremiumCoffeeMachine import MaquinaCafePremium

class TestMaquinaCafePremium(unittest.TestCase):    
    def testInicial(self):
        cafePremium = MaquinaCafePremium()
        self.assertEqual(cafePremium.reservas['cafe'], 0)
        self.assertEqual(cafePremium.reservas['leche'], 0)
        self.assertEqual(cafePremium.reservas['agua'], 0)
        self.assertEqual(cafePremium.reservas['azucar'], 0)  
        
    #Almacena una vez
    def testAlmacenar1(self): 
        cafePremium = MaquinaCafePremium()
        cafePremium.almacenar(10, 20, 30, 40)
        self.assertEqual(cafePremium.reservas['cafe'], 10)
        self.assertEqual(cafePremium.reservas['leche'], 20)
        self.assertEqual(cafePremium.reservas['agua'], 30)
        self.assertEqual(cafePremium.reservas['azucar'], 40)
     
    #Almacena dos veces   
    def testAlmacenar2(self):
        cafePremium = MaquinaCafePremium()
        cafePremium.almacenar(10, 20, 30, 40)
        cafePremium.almacenar(40, 30, 20, 10)
        self.assertEqual(cafePremium.reservas['cafe'], 50)
        self.assertEqual(cafePremium.reservas['leche'], 50)
        self.assertEqual(cafePremium.reservas['agua'], 50)
        self.assertEqual(cafePremium.reservas['azucar'], 50)
        
    """
    ---------------------CAPUCCINO--------------------------
    Ingredientes:
        Cafe: 10, Leche: 90, Azucar: 3
    """
    #Este test se aplica tambien para cafe con leche   
    def testCapuccino(self):
        cafePremium = MaquinaCafePremium()
        cafePremium.almacenar(100, 200, 80, 40)
        cafePremium.prepararCapuccino()
        self.assertEqual(cafePremium.reservas['cafe'], 90)
        self.assertEqual(cafePremium.reservas['leche'], 110)
        self.assertEqual(cafePremium.reservas['azucar'], 37)
    
    #Error todos los ingredientes
    def testErrorIngredientesTodosCapuccino(self):
        cafePremium = MaquinaCafePremium()
        with self.assertRaises(ValueError):
            cafePremium.prepararCapuccino()
            
    #Error por falta de cafe
    def testErrorIngredientesCafeCapuccino(self):
        cafePremium = MaquinaCafePremium()
        cafePremium.almacenar(5, 200, 300, 500)
        with self.assertRaises(ValueError):
            cafePremium.prepararCapuccino()
    
    #Error por falta de leche
    def testErrorIngredientesLecheCapuccino(self):
        cafePremium = MaquinaCafePremium()
        cafePremium.almacenar(100, 3, 300, 500)
        with self.assertRaises(ValueError):
            cafePremium.prepararCapuccino()
    
    #Error por falta de azucar
    def testErrorIngredientesAzucarCapuccino(self):
        cafePremium = MaquinaCafePremium()
        cafePremium.almacenar(5, 200, 300, 1)
        with self.assertRaises(ValueError):
            cafePremium.prepararCapuccino()
        
    """
    ---------------------AMERICANO--------------------------
    Ingredientes:
        Cafe: 20, Agua: 80, Azucar: 3
    """ 
    
    def testCafeAmericano(self):
        cafePremium = MaquinaCafePremium()
        cafePremium.almacenar(100, 200, 80, 40)
        cafePremium.prepararCafeAmericano()
        self.assertEqual(cafePremium.reservas['cafe'], 80)
        self.assertEqual(cafePremium.reservas['agua'], 0)
        self.assertEqual(cafePremium.reservas['azucar'], 37)
    
    #Error todos los ingredientes
    def testErrorIngredientesTodosAmericano(self):
        cafePremium = MaquinaCafePremium()
        with self.assertRaises(ValueError):
            cafePremium.prepararCafeAmericano()
            
    #Error por falta de cafe
    def testErrorIngredientesCafeAmericano(self):
        cafePremium = MaquinaCafePremium()
        cafePremium.almacenar(5, 200, 300, 500)
        with self.assertRaises(ValueError):
            cafePremium.prepararCafeAmericano()
    
    #Error por falta de agua
    def testErrorIngredientesLecheAmericano(self):
        cafePremium = MaquinaCafePremium()
        cafePremium.almacenar(100, 300, 3, 500)
        with self.assertRaises(ValueError):
            cafePremium.prepararCafeAmericano()
    
    #Error por falta de azucar
    def testErrorIngredientesAzucarAmericano(self):
        cafePremium = MaquinaCafePremium()
        cafePremium.almacenar(100, 200, 300, 1)
        with self.assertRaises(ValueError):
            cafePremium.prepararCafeAmericano()
                  
    """
    ---------------------CORTADO--------------------------
    Ingredientes:
        Cafe: 20, Leche: 10, Agua: 70, Azucar: 3
    """
    def testCafeCortado(self):
        cafePremium = MaquinaCafePremium()
        cafePremium.almacenar(100, 200, 80, 40)
        cafePremium.prepararCafeCortado()
        self.assertEqual(cafePremium.reservas['cafe'], 80)
        self.assertEqual(cafePremium.reservas['leche'], 190)
        self.assertEqual(cafePremium.reservas['agua'], 10)
        self.assertEqual(cafePremium.reservas['azucar'], 37)
        
    def testErrorIngredientesTodosCortado(self):
        cafePremium = MaquinaCafePremium()
        with self.assertRaises(ValueError):
            cafePremium.prepararCafeCortado()
            
    #Error por falta de cafe
    def testErrorIngredientesCafeCortado(self):
        cafePremium = MaquinaCafePremium()
        cafePremium.almacenar(5, 200, 300, 500)
        with self.assertRaises(ValueError):
            cafePremium.prepararCafeCortado()
            
    #Error por falta de leche
    def testErrorIngredientesLecheCortado(self):
        cafePremium = MaquinaCafePremium()
        cafePremium.almacenar(100, 3, 300, 500)
        with self.assertRaises(ValueError):
            cafePremium.prepararCafeCortado()
    
    #Error por falta de agua
    def testErrorIngredientesLecheCortado(self):
        cafePremium = MaquinaCafePremium()
        cafePremium.almacenar(100, 300, 3, 500)
        with self.assertRaises(ValueError):
            cafePremium.prepararCafeCortado()

    #Error por falta de azucar
    def testErrorIngredientesAzucarCortado(self):
        cafePremium = MaquinaCafePremium()
        cafePremium.almacenar(100, 200, 300, 1)
        with self.assertRaises(ValueError):
            cafePremium.prepararCafeCortado()
    
if __name__=='__main__':
    unittest.main()