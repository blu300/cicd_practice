import sys
import unittest
from pathlib import Path

module_dir = Path(__file__).resolve().parent
print(module_dir)
sys.path.append(module_dir)

from src.app import test_app


class BaseCase(unittest.TestCase):
    def setUp(self):
        # this statement will be executed before testing
        print("Running Test:")
    
    def tearDown(self):
        # this statement will be executed after testing
        print('''Test Complete
              ''' )