import re
import _operations
import logging

logger = logging.getLogger("RegexRiot")

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

    def __init__(self, a, b, combinator, unit) -> None:
        """Create a RiotString from a given expression. Use this to create a 
        building block from which you will build up to what ever complicated 
        regex you actually want. 
        Something like
        ``RiotString("Annie are you okay ").then("are you okay ").times(2).then("Annie")``
        to make the regex ``"Annie are you okay (are you okay ){2}Annie``
        
        """
        self._a = str(a)
        self._b = str(b)
        self._combinator = combinator
        self._unit = unit

    def __str__(self) -> str:
        return self._combinator(self._a, self._b)
    def __repr__(self) -> str:
        return f'<RiotString: "{str(self)}">'
    
    def then(self, rs):
        """
        The current RiotString followed by the next RiotString. 
        Use like so
        
        ``RiotString('a').then(RiotString('b')) => RiotString('ab')``

        Parameters
        ----------
        rs: The next RiotString or string

        """
        return RiotString(self,rs, _operations.then, False)

    def one_or_more(self):
        """
        The current RiotString repeated one or more times.
        Use like so

        ``one_or_more(RiotString('a')) => RiotString('a+')``
        or
        ``RiotString('a').one_or_more() => RiotString('a+')``

        """
        regex = _operations.one_or_more(str(self), self._unit)
        return RiotString(regex, "", lambda a,b: a, True)
    
    def times(self, n):
        """
        The current RiotString repeated n times.
        Use like so

        ``RiotString('a').times(5) => RiotString('a{5}')``

        """
        regex = _operations.times(str(self), n, self._unit)
        return RiotString(regex, "", lambda a,b:a, self._unit)
    def compile(self) -> re.Pattern:
        """Return the compiled regex. This is the result of ``re.compile("pattern")``"""
        return re.compile(str(self))

one_or_more = RiotString.one_or_more

class RiotSet(RiotString):
    def __init__(self, *args, to=None, inverted=False) -> None:
        if len(args) == 0:
            raise Exception("Can't create an empty set")
        if len(args) == 1:
            assert to is not None, f"Got a range start {args[0]} but no range end"
            self.elements = [f'{args[0]}-{to}']
        else:
            assert to is None, f"Got a range end {to} for multiple possible starts"
            if args[0] == '^':
                logger.warning("'^' was first element in set. Moving it to be last")
                args = args[1:]+args[:1]
            self.elements = [str(i) for i in args]
        a = f"[{'^' if inverted else ''}{''.join(self.elements)}]"
        super().__init__(a, "", lambda a,b: a, True)
    def invert(self):
        revert = str(self)[1] == '^'
        return RiotSet(self.elements, inverted = False if revert else True)

invert = RiotSet.invert

def riot(seed, *args, to=None):
    """
    Simplified interface for RiotString
    """
    if not args and to is None:
        return RiotString(seed, "", lambda a,b: a, len(seed)==1)
    if not to is None:
        assert not args, f"Got extra argument for range start {args}"
        return RiotSet(seed, to=to)
    else:
        return RiotSet(seed, *args)

