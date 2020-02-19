import unittest
from datetime import datetime
from models import *


class City(BaseModel):
    '''
    Test the city model class
    '''

    def setUp(self):
        self.model = City()
        self.model.save()

    def test_var_initialization(self):
        self.assertTrue(hasattr(self.model, "name"))
        self.assertTrue(hasattr(self.model, "state_id"))
        self.assertEqual(self.model.name, "")
        self.assertEqual(self.model.state_id, "")
