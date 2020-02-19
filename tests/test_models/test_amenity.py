import unittest
from datetime import datetime
from models import *


class Test_AmenityModel(unittest.TestCase):
    '''
    Testing the amenity model class(task)
    '''

    def setUp(self):
        self.model = Amenity()
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertEqual(self.model.name, "")


if __name__ == "__main__":
    unittest.main()
