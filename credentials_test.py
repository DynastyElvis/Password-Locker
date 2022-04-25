import unittest
from credentials import Credential

class TestCredential(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behaviours
    """
    def setUp(self):
        """
        set up method to run before each test cases
        """
        self.new_credential = Credential("yvette","twitter","umutesiwaseyvette","yvette")

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run
        """
        Credential.credential_list = []
    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credential.view_password,"yvette")
        self.assertEqual(self.new_credential.account,"twitter")
        self.assertEqual(self.new_credential.login,"umutesiwaseyvette")
        self.assertEqual(self.new_credential.password,"yvette")
    def test_save_credential(self):
        """_summary_
        test_save_credential test case to test if the credential object is saved into
        the credential list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)
        """
    def tes