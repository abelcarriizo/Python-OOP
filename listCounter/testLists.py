#Abel Carrizo
import unittest
from lists import searchNumbers

class TestLists(unittest.TestCase):
    def testlist(self):
        self.assertEqual(searchNumbers([1,5,3,2,5,9]), {1:1, 2:1, 3:1, 5:2, 9:1 })

if __name__ == '__main__':
    unittest.main()