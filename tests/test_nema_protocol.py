"""
This is a test to match and parse data in the nema protocol used by the `ZED-F9P gps module`_

.. _ZED-F9P gps module: https://www.mouser.com/pdfDocs/u-blox_ZED-F9P-04B_ID.pdf#page=19&zoom=100,78,132

"""

from src.RegexRiot import *
import unittest


text = """$GAGSV,1,1,02,03,79,346,20,08,28,312,34,7*7A
$GAGSV,1,1,03,02,40,207,,24,28,045,,25,77,095,,0*42
$GBGSV,1,1,00,0*77
$GQGSV,1,1,00,0*64
$GNGLL,3720.23679,N,12152.93810,W,234352.00,A,A*6D
$GNRMC,234353.00,A,3720.23627,N,12152.93749,W,2.133,133.32,121024,,,A,V*1E
$GNVTG,133.32,T,,M,2.133,N,3.950,K,A*2F
$GNGGA,234353.00,3720.23627,N,12152.93749,W,1,07,3.98,-1.1,M,-29.9,M,,*56
$GNGSA,A,3,07,20,30,,,,,,,,,,5.32,3.98,3.53,1*04
$GNGSA,A,3,80,71,72,,,,,,,,,,5.32,3.98,3.53,2*0A
$GNGSA,A,3,08,,,,,,,,,,,,5.32,3.98,3.53,3*08
$GNGSA,A,3,,,,,,,,,,,,,5.32,3.98,3.53,4*07
$GNGSA,A,3,,,,,,,,,,,,,5.32,3.98,3.53,5*06
$GPGSV,2,1,07,07,66,325,16,09,76,117,13,14,18,215,16,16,14,042,19,1*68
$GPGSV,2,2,07,20,22,303,37,27,24,070,10,30,41,284,25,1*5F
$GPGSV,1,1,03,04,41,123,,05,05,327,,08,31,107,,0*5D
"""
decimal_number = one_or_more(DIGIT).then(DOT).then(one_or_more(DIGIT))
patern = riot("\$")\
    .then( ANYTHING.times(2).then("RMC") )\
    .then(',').then(as_group(decimal_number))\
    .then(",").then(riot("A", "V").as_group())\
    .then(',').then(as_group(decimal_number))\
    .then(",").then(riot("N", "S").as_group())\
    .then(',').then(as_group(decimal_number))\
    .then(",").then(riot("E", "W").as_group())\
    .then(',').then(as_group(decimal_number))\
    .then(',').then(as_group(decimal_number))\
    .then(',').then(DIGIT.times(6))\
    .then(one_or_more(ANYTHING)).then("\*").then(HEXADECIMAL.times(2))\
    .compile()
"""pattern to parse an RMC message in NEMA protocol"""

class NEMAProtocol(unittest.TestCase):
    def test_find_correct_line(self):
        line = "$GNRMC,234353.00,A,3720.23627,N,12152.93749,W,2.133,133.32,121024,,,A,V*1E"
        self.assertEqual(
            patern.search(text).group(),
            line
        )
    def test_parse_time(self):
        time = "234353.00"
        self.assertEqual(
            patern.search(text).group(1),
            time
        )
    def test_parse_status(self):
        status = "A"
        self.assertEqual(
            patern.search(text).group(2),
            status
        )
    def test_parse_latitude(self):
        lat = "3720.23627"
        self.assertEqual(
            patern.search(text).group(3),
            lat
        )
        
        