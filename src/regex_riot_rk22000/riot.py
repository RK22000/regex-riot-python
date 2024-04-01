"""
This is the primary module in the regex-riot library. Import everything from
this module.

"""

class RiotString:
    def __init__(self, re:str) -> None:
        self._a = re
        self._b = ""

    @property
    def a(self):
        return self._a
    @property
    def b(self):
        return self._b

    def __str__(self) -> str:
        return self.a + self.b

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, str) or isinstance(__value, RiotString):
            return str(self)==str(__value)

DIGIT       = RiotString(r'\d')
NON_DIGIT   = RiotString(r'\D')
ANYTHING    = RiotString(r'.')
ALPHANUM    = RiotString(r'\w')
NON_ALPHANUM= RiotString(r'\W')
SPACE       = RiotString(r'\s')
NON_SPACE   = RiotString(r'\S')
BOUNDARY    = RiotString(r'\b')
NON_BOUNDARY= RiotString(r'\B')