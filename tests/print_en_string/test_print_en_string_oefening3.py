import unittest
from test_helpers import *

class TestStringOutputOefening3(unittest.TestCase):
    def test_print_en_string_oefening3(self):
        
        module_name = "oefeningen.print_en_string.oefening3"

        variables = ["naam","game"]

        test(module_name,"{naam} speelt graag {game}!",required_variables=variables)

        test(module_name,"John speelt graag The Last of Us!", required_variables=variables, set_variables={"naam":"John","game":"The Last of Us"})
