import unittest

from project.services import create_user, get_last_user


class CreateUserTests(unittest.TestCase):
    def test_user_is_created_successfully(self):
        name = 'Test User'
        create_user(name=name)

        user = get_last_user()

        self.assertIsNotNone(user)
        self.assertEqual(name, user.name)
