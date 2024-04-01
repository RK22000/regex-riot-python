from src.regex_riot_rk22000.example import add_one
import unittest

class Test1(unittest.TestCase):
    
    def test_t1(self):
        self.assertEqual(6, add_one(5))


if __name__=='__main__':
    unittest.main()