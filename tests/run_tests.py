import unittest
import os
import sys
from collections import defaultdict
import importlib

# -------------------------------
# Student-friendly test result
# -------------------------------
class FilteredResult(unittest.TextTestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.grouped_results = defaultdict(list)
        self.successes = []

    def addSuccess(self, test):
        self.successes.append(test)
        category = self._get_category(test)
        self.grouped_results[category].append((test, "PASS"))
        # Do not call super().addSuccess → suppress default output

    def addFailure(self, test, err):
        category = self._get_category(test)
        msg = ""
        if isinstance(err[1], AssertionError) and err[1].args:
            msg = err[1].args[-1]  # only use your custom message
        self.grouped_results[category].append((test, "FAIL", msg))
        # Do not call super().addFailure → suppress default output

    def addError(self, test, err):
        category = self._get_category(test)
        msg = "Onverwachte fout!"
        self.grouped_results[category].append((test, "ERROR", msg))
        # Do not call super().addError → suppress default output

    def _get_category(self, test):
        module_name = test.__class__.__module__  # e.g., tests.test_print_en_string_oefening1
        # remove 'tests.' prefix
        if module_name.startswith("tests."):
            module_name = module_name[6:]  # remove 'tests.'
        # remove 'test_' prefix
        if module_name.startswith("test_"):
            module_name = module_name[5:]
        # remove trailing '_oefeningX' if present
        module_name = "_".join(module_name.split("_")[:-1])
        return module_name if module_name else "Overige"


    def display_summary(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\n" + "="*60)
        print(" RESULTATEN ".center(60, "="))
        print("="*60 + "\n")
        for category, results in self.grouped_results.items():
            print(f"=== {category.replace('_',' ').title()} ===")
            for item in results:
                test, status, *msg = item
                message = msg[0] if msg else ""
                if status == "PASS":
                    print(f"  ✅ {test._testMethodName}")
                elif status == "FAIL":
                    print(f"  ❌ {test._testMethodName}")
                    if message:
                        print(f"      {message}")
                elif status == "ERROR":
                    print(f"  💥 {test._testMethodName}")
                    if message:
                        print(f"      {message}")
            print("")
        print("="*60)
        total = sum(len(v) for v in self.grouped_results.values())
        fails = sum(1 for r in self.grouped_results.values() for t,s,*m in r if s=="FAIL" or s=="ERROR")
        print(f"Totaal tests: {total}")
        print(f"Geslaagd: {len(self.successes)}")
        print(f"Mislukt: {fails}")
        print("="*60 + "\n")

# -------------------------------
# Custom test runner
# -------------------------------
class StudentFriendlyRunner(unittest.TextTestRunner):
    resultclass = FilteredResult

# -------------------------------
# Run tests manually
# -------------------------------
if __name__ == "__main__":
    # Add project root to sys.path
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.insert(0, project_root)

    tests_dir = os.path.dirname(os.path.abspath(__file__))

    # Discover tests
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=tests_dir, pattern="test_*.py",)

    # Run tests
    runner = StudentFriendlyRunner(verbosity=0)
    result = runner.run(suite)
    result.display_summary()
