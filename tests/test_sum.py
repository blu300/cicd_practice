import unittest
import sys
from pathlib import Path

module_dir = Path(__file__).resolve().parent
print(module_dir)
sys.path.append(module_dir)

from src.app.routes import sum
from tests.BaseCase import BaseCase

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1,2,3,4,5]
        result = sum(data)
        self.assertEqual(result, 15)
    
    def test_fail_with_single_value(self):
        data = [1]
        result = sum(data)
        self.assertEqual(result, 1)

    def test_lisf_float(self):
        data = [1.2, 2.4, 2.7, 0.5, 1.8]
        result = sum(data)
        self.assertEqual(result, 8.6)

    def test_list_with_negative_value(self):
        data = [1, 2, 3, 4, -5]
        result = sum(data)
        self.assertEqual(result, 5)
    
    def test_with_tupple(self):
        data = (1, 2, 3, 4, 5)
        result = sum(data)
        self.assertEqual(result, 15)
    
    # def test_fail_with_string(self):
    #     data = [1, 2, '3', '4', '5']
    #     result = sum(data)
    #     print(result[0])
    #     self.assertRaises(TypeError, lambda: self.testListNone[:1])
