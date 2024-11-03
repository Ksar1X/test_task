import unittest

class LoginPageTest(unittest.TestCase):
    def __init__(self, email, password):
        self.email = email
        self.password = password