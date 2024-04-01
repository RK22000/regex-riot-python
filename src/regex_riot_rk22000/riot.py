"""
This is the primary module in the regex-riot library. Import everything from
this module.

"""

import re

class RiotString:
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
        if self.unit:
            return RiotString(f"{self.a}+")
        else:
            return RiotString(f"({self.a})+")
    
    def compile(self) -> re.Pattern:
        return re.compile(str(self))



    # def __eq__(self, __value: object) -> bool:
    #     if isinstance(__value, str) or isinstance(__value, RiotString):
    #         return str(self)==str(__value)

def one_or_more(rs:RiotString):
    return rs.one_or_more()


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