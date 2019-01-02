import unittest
from lab3.app import *


class TestApp(unittest.TestCase):
    """
    Test the app.py
    """

    def test_logout(self):
        """
        Test logout functionality
        """
        with app.test_request_context():
            result = logout()
            json = result.get_json()
            self.assertEqual(json["success"], True)

    def test_login(self):
        """
        Test logout functionality
        """
        with app.test_request_context():
            result = logout()
            json = result.get_json()

    def test_fresh_login(self):
        """
        Test logout functionality
        """
        with app.test_request_context():
            result = logout()
            json = result.get_json()


if __name__ == '__main__':
    unittest.main()
