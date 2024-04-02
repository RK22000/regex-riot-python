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
    
    For instance the expression ``\d+\.\d+`` can be built using RiotStrings as 
    ``one_or_more(DIGIT).then(DOT).then(one_or_more(DIGIT))``. Although this is 
    not as consice as writing the regex itself, with the help of autocomplete it 
    will be easier to write write regex as a chain of function calls that read
    that read out to english like text.
    
    """

    def __init__(self, re, unit=False) -> None:
        """Create a RiotString from a given expression. Use this to create a 
        building block from which you will build up to what ever complicated 
        regex you actually want. 
        Something like
        `RiotString("Annie are you okay ").then("are you okay ").times(2).then("Annie")`
        to make the regex `"Annie are you okay (are you okay ){2}Annie`
        
        """
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
        """
        The current RiotString followed by the next RiotString. 
        Use like so
        
        ``RiotString('a').then(RiotString('b')) => RiotString('ab')``

        Parameters
        ----------
        rs: The next RiotString or string



        """
        return RiotString(str(self)+str(rs))
    def one_or_more(self):
        """
        The current RiotString repeated one or more times.
        Use like so

        ``one_or_more(RiotString('a')) => RiotString('a+')``
        or
        ``RiotString('a').one_or_more() => RiotString('a+')``

        """
        if self.unit:
            return RiotString(f"{self.a}+")
        else:
            return RiotString(f"({self.a})+")
    
    def compile(self) -> re.Pattern:
        """Return the compiled regex. This is the result of ``re.compile("pattern")``"""
        return re.compile(str(self))

# one_or_more = RiotString.one_or_more


DIGIT       = RiotString(r'\d', unit=True)
'RiotString for a digit. ``\d``'
NON_DIGIT   = RiotString(r'\D', unit=True)
'RiotString for non digit. ``\D``'
ANYTHING    = RiotString(r'.', unit=True)
'RiotString to match any digit. ``.``'
ALPHANUM    = RiotString(r'\w', unit=True)
'RiotString to match any alphanumeric character. ``\w``'
NON_ALPHANUM= RiotString(r'\W', unit=True)
'RiotString to match any non-alphanumeric character. ``\W``'
SPACE       = RiotString(r'\s', unit=True)
'RiotString to match any space character. ``\s``'
NON_SPACE   = RiotString(r'\S', unit=True)
'RiotString to match any non-space character. ``\S``'
BOUNDARY    = RiotString(r'\b', unit=True)
'RiotString to match a character at a boundary position. ``\b``'
NON_BOUNDARY= RiotString(r'\B', unit=True)
'RiotString to match a character not at a boundary position. ``\B``'
DOT         = RiotString(r'\.', unit=True)
'RiotString to match a dot. ``\.``'