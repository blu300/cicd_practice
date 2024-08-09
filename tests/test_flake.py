import sys, unittest
from pathlib import Path


module_dir = Path(__file__).resolve().parent
print(module_dir)
sys.path.append(module_dir)
from src.app.routes import test_app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = test_app
        self.client = self.app.test_client()
        self.app.testing = True

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello world', response.data)  # Adjust according to your homepage content

    def test_404_error(self):
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
