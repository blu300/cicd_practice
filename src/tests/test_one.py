import sys, os, unittest
# sys.path.insert(0, os.path.dirname(__file__))
from src.factorial import sum_factorial

try:
    1/2
except Exception as e:
    sys.exit(e)

class TestFactorial(unittest.TestCase):
    
    def test_three(self):
        self.assertEqual(sum_factorial(3), 4)


if __name__ == '__main__':
    unittest.main()