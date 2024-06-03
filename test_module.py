import unittest
import my_validtor


class TestModule(unittest.TestCase):

    def test_validate_email(self):
        self.assertTrue(my_validtor.validate_email("A31924@sfc.potteries.ac.uk"))

    def test_length_check(self):
        self.assertTrue(my_validtor.length_check("password", 8, 2))

    def test_password_validator(self):
        self.assertTrue(my_validtor.password_validator("Password1@", 8))