import unittest
from test_helpers import *

class TestStringOutputOefening6(unittest.TestCase):
    def test_print_en_string_oefening6(self):
        
        module_name = "oefeningen.print_en_string.oefening6"

        test(module_name,'Ik hou zo van George.',["George"])
        test(module_name,'Ik hou zo van Shiro.',["Shiro"])