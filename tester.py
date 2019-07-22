import unittest
from password import Password, User

class Testing (unittest.TestCase):
    def setUp(self):
        self.new_person = Password("Oscar", "1234")
        self.new_user = User ("Cheru", "123")