import unittest
from test_helpers import *

class TestStringOutputOefening5(unittest.TestCase):
    def test_print_en_string_oefening5(self):
        
        module_name = "oefeningen.print_en_string.oefening5"

        test(module_name,'Ik zei tegen hem: "Ik bel je \'s avonds"')