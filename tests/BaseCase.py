import unittest

import sys
from pathlib import Path
module_dir = Path(__file__).resolve().parent
print(module_dir)
sys.path.append(module_dir)

from src.app import test_app

class BaseCase(unittest.TestCase):
    def setUp(self):
        # this statement will be executed before testing
        self.app = test_app.test_client()
    #    self.db = db.get_db() # get db by example
    
    def tearDown(self):
        # this statement will be executed after testing
        # Delete Database collections after the test is complete
        # for collection in self.db.list_collection_names()
        # self.db.drop_collection(collection)
        pass