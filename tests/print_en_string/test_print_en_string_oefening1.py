import unittest
from io import StringIO
from unittest.mock import patch
import importlib
import sys
from test_helpers import *

class TestStringOutputOefening1(unittest.TestCase):
    def test_print_en_string_oefening1(self):
        module_name = "oefeningen.print_en_string.oefening1"

        test(module_name,"Hello world!")
            