import unittest
from palindromes import palindromes

class TestPalindromos(unittest.TestCase):
    def test1(self):
        self.assertEqual(palindromes('ana'), True)
    def test2(self):
        self.assertEqual(palindromes('nicolas'), False)  
    def test3(self):
        self.assertEqual(palindromes('sometemos'), True)
    def test4(self):
        self.assertEqual(palindromes('abel'), False)     

if __name__ == '__main__':
    unittest.main()