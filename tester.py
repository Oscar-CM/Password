import unittest
from password import Password, User

class Testing (unittest.TestCase):
    def setUp(self):
        self.new_person = Password("Oscar", "1234")
        self.new_user = User ("Cheru", "123")

    def test_init(self):
        '''
        Testing both of by classes initializations
        '''
        self.assertEqual(self.new_person.userName,"Oscar")
        self.assertEqual(self.new_person.password,"1234")
        self.assertEqual(self.new_user.name, "Cheru")
        self.assertEqual(self.new_user.Password, "123")

        ''' Testing the password class'''

     def test_savePassword(self):
        self.new_person.savePassword()
        self.assertEqual(len(Password.my_list),1)

    def test_deletePassword(self):
        self.new_person.savePassword()
        self.new_person.deletePassword()
        self.assertEqual(len(Password.my_list),0)


        '''
        Testing the User class
        '''
    def test_saveUser(self):
        self.new_user.saveUser()
        self.assertEqual(len(User.user_list),1)
