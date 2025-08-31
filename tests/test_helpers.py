from types import ModuleType
from io import StringIO
from unittest.mock import patch
import importlib
import sys
import os

def test(module_name,expected,inputs=[],required_variables=[],set_variables={},strict=True):
    expected = expected.replace("{","{oefening.")
    with patch("builtins.input", side_effect=inputs):
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            if module_name in sys.modules:
                del sys.modules[module_name]
            oefening = importlib.import_module(module_name)

            for required_variable in required_variables:
                assert_has_variable(oefening,required_variable)
            
            if len(set_variables) == 0:
                output = mock_stdout.getvalue().strip()
                expected = expected.format(**locals())
                assert_eq_custom(output,expected)
    
    if len(set_variables) > 0:
        module_path = os.path.join(*module_name.split(".")) + ".py"
        with open(module_path, "r", encoding="utf-8") as f:
            code = f.read()

        modified_code = codeVariablesModified(code,set_variables,strict)
        with patch("builtins.input", side_effects=inputs):
            with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
                exec(modified_code)
                actual_output = mock_stdout.getvalue().strip()
                expected = expected.format(**locals())
                assert_eq_custom(actual_output, expected)
    


def codeVariablesModified(code,variables,strict):
    modified = []
    for key,value in variables.items():
        found = False        
        for line in code.splitlines():
            line_nospace = line.strip().replace(" ","")
            if line_nospace.startswith(f"{key}="):
                found = True
                if isinstance(value,str):
                    value = f'"{value}"'
                    l = f'{key} = {value}'
                modified.append(f'{key} = {value}')
            else:
                modified.append(line)
        if strict and not found:
            raise AssertionError(f"Variabele {key} werd niet gevonden.")
        code = "\n".join(modified)
        modified = []
    return code

def assert_eq_custom(actual, expected):
    """
    Checks equality and raises an AssertionError with a student-friendly message.
    """
    if actual != expected:
        raise AssertionError(f"Verwachte uitvoer: '{expected}', jouw uitvoer: '{actual}'")


def assert_true_custom(condition, message):
    """
    Checks if condition is True; raises AssertionError with message if not.
    """
    if not condition:
        raise AssertionError(message)

def assert_has_variable(module, variable):
    is_true = False
    moduleName = ""
    if isinstance(module,dict):
        is_true = variable in module
        moduleName = module["__file__"]
    elif isinstance(module, ModuleType):
        is_true = hasattr(module, variable)
        moduleName = module.__name__
    else:
        raise NotImplementedError()
    assert_true_custom(is_true, f"De variabele '{variable}' ontbreekt in {moduleName}.py")