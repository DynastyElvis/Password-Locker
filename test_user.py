import unittest # Importing the unittest module
from user import User # Importing the user class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    
    self.new_user = User("username","password") # create user object
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
        '''
        test_save_multiple_user to check if we can save multiple user
        objects to our user_list
        '''
    def test_save_multiple_user(self):
        self.new_user.save_user()
        test_user = User("username","password")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
if __name__ == '__main__':
    unittest.main()
    