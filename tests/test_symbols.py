from src.regex_riot_rk22000.riot import *
import unittest

class LiteralsStringValueTests(unittest.TestCase):
    
    def test_digit(self):
        self.assertEqual(DIGIT, r'\d')
        self.assertEqual(NON_DIGIT, r'\D')
    
    def test_anything(self):
        self.assertEqual(ANYTHING, r'.')
    
    def test_alphanum(self):
        self.assertEqual(ALPHANUM, r'\w')
        self.assertEqual(NON_ALPHANUM, r'\W')
        
    def test_space(self):
        self.assertEqual(SPACE, r'\s')
        self.assertEqual(NON_SPACE, r'\S')
    
    def test_boundary(self):
        self.assertEqual(BOUNDARY, r'\b')
        self.assertEqual(NON_BOUNDARY, r'\B')
    
    def test_custom_string(self):
        words = ['hello','there', ',', ' ', 'general', 'kenobi']
        for w in words:
            self.assertEqual(RiotString(w), w)
