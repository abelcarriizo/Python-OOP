import unittest
from romanNumbers.converter import decimaltoRoman

class TestDecimalToRoman(unittest.TestCase):

    def testDecimal1 (self):
        self.assertEqual(decimaltoRoman(1),'I')

    def testDecimal4 (self):
        self.assertEqual(decimaltoRoman(4),'IV')

    def testDecimal5 (self):
        self.assertEqual(decimaltoRoman(5),'V')

    def testDecimal9 (self):
        self.assertEqual(decimaltoRoman(9),'IX')

    def testDecimal10 (self):
        self.assertEqual(decimaltoRoman(10),'X')
        
if __name__ == '__main__':
    unittest.main()