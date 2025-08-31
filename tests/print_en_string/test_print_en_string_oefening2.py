import unittest
from test_helpers import *

class TestStringOutputOefening2(unittest.TestCase):
    def test_print_en_string_oefening2(self):
        module_name = "oefeningen.print_en_string.oefening2"

        variables = ["naam"]

        test(module_name,"Hallo {naam}!",required_variables=variables)

        test(module_name,"Hallo John!", required_variables=variables, set_variables={"naam":"John"})
