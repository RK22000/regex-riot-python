"""
This is the primary module in the regex-riot library. Import everything from
this module.

"""

import re

class RiotString:
    """
    This is the object that will hold and mutate regular expressions. 
    RiotStrings can be composed together to build more complicated regular 
    expressions. 
    
    For instance the expression `\d+\.\d+` can be built using RiotStrings as 
    `one_or_more(DIGIT).then(DOT).then(one_or_more(DIGIT))`. Although this is 
    not as consice as writing the regex itself, with the help of autocomplete it 
    will be easier to write write regex as a chain of function calls that read
    that read out to english like text.
    
    """

    def __init__(self, re, unit=False) -> None:
        self._a = str(re)
        self._b = ""
        self._unit = unit

    @property
    def a(self):
        return self._a
    @property
    def b(self):
        return self._b
    @property
    def unit(self):
        return self._unit

    def __str__(self) -> str:
        return self.a + self.b
    
    def then(self, rs):
        return RiotString(str(self)+str(rs))
    def one_or_more(self):
        'Hello'
        if self.unit:
            return RiotString(f"{self.a}+")
        else:
            return RiotString(f"({self.a})+")
    
    def compile(self) -> re.Pattern:
        return re.compile(str(self))

one_or_more = RiotString.one_or_more


DIGIT       = RiotString(r'\d', unit=True)
NON_DIGIT   = RiotString(r'\D', unit=True)
ANYTHING    = RiotString(r'.', unit=True)
ALPHANUM    = RiotString(r'\w', unit=True)
NON_ALPHANUM= RiotString(r'\W', unit=True)
SPACE       = RiotString(r'\s', unit=True)
NON_SPACE   = RiotString(r'\S', unit=True)
BOUNDARY    = RiotString(r'\b', unit=True)
NON_BOUNDARY= RiotString(r'\B', unit=True)
DOT         = RiotString(r'\.', unit=True)