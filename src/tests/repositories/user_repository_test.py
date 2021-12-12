import unittest
import os
from pathlib import Path
from repositories.user_repository import UserRepository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, "..", "test_users.csv")
        Path(path).touch()
        with open(path, "w") as file:
            file.write("")
        self.user_repository = UserRepository(path)
        self.user = User("Testi Testinen", [])
        self.user_repository.add_user(self.user)

    def test_add_user_works(self):
        user_two = User("Tiina Testi", [])
        self.assertTrue(self.user_repository.add_user(user_two))

    def test_add_user_fails_with_duplicates(self):
        user_two = User("Testi Testinen", [])
        self.assertFalse(self.user_repository.add_user(user_two))

    def test_find_user_works(self):
        self.assertEqual(self.user_repository.find_user(
            "Testi Testinen").username, "Testi Testinen")

    def test_add_sample_and_get_samples_works(self):
        user = self.user_repository.find_user("Testi Testinen")
        self.user_repository.add_sample(user, "123")
        self.assertTrue(self.user_repository.get_sample_ids_by_user(
            user), ["123"])

    def test_get_usernames_works(self):
        user = User("Tiina Testi", [])
        self.user_repository.add_user(user)
        self.assertTrue(self.user_repository.get_usernames(),
                        ["Testi Testinen", "Tiina Testi"])
