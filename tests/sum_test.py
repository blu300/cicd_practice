import unittest
import sys

# sys.path.append("C:\\Users\\Benjamin\\Documents\\Learning\\cicd")
sys.path.append("..\\")
# print(sys.path)

from src.app.routes import sum

class TestSum(unittest.TestCase):
    def test_list_int(self):
        data = [1,2,3,4,5]
        result = sum(data)
        self.assertEqual(result, 15)