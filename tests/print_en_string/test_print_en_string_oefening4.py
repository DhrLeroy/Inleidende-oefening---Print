import unittest
from test_helpers import *

class TestStringOutputOefening4(unittest.TestCase):
    def test_print_en_string_oefening4(self):
        
        module_name = "oefeningen.print_en_string.oefening4"

        variables = ["quote"]

        test(module_name,'Mijn favoriete quote: "{quote}"',required_variables=variables)

        test(module_name,'Mijn favoriete quote: "For Frodo."', required_variables=variables, set_variables={"quote":"For Frodo."})