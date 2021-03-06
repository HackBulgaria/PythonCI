import unittest

from project.bootstrap import bootstrap
from project.services import create_user, get_last_user


class DatabaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        bootstrap()


class CreateUserTests(DatabaseTestCase):
    def test_user_is_created_successfully(self):
        name = 'Test User'
        create_user(name=name)

        user = get_last_user()

        self.assertIsNotNone(user)
        self.assertEqual(name, user.name)
