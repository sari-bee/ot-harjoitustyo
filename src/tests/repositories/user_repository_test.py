import unittest
from pathlib import Path
from repositories.user_repository import UserRepository
from entities.user import User
from config import USERS_FILEPATH


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        path = USERS_FILEPATH
        Path(path).touch()
        with open(path, "w") as file:
            file.write("")
        self.user_repository = UserRepository(path)
        self.user = User("Testi Testinen", [])
        self.user_repository.add_user(self.user)

    def test_add_user_and_find_user_works(self):
        user_two = User("Tiina Testi", [])
        self.user_repository.add_user(user_two)
        self.assertEqual(self.user_repository.find_user(
            "Tiina Testi").username, "Tiina Testi")

    def test_add_user_fails_with_duplicates(self):
        user_two = User("Testi Testinen", [])
        self.assertFalse(self.user_repository.add_user(user_two))

    def test_find_user_fails(self):
        self.assertEqual(self.user_repository.find_user("Tiina Testi"), None)

    def test_add_sample_and_get_samples_works(self):
        user_two = User("Tiina Testi", [])
        self.user_repository.add_user(user_two)
        user = self.user_repository.find_user("Tiina Testi")
        self.user_repository.add_sample(user, "123")
        self.user_repository.add_sample(user, "456")
        self.assertEqual(self.user_repository.get_sample_ids_by_user(
            user), ["123", "456"])

    def test_get_samples_for_nonexistent_user(self):
        user = User("Tiina Testi", [])
        self.assertEqual(
            self.user_repository.get_sample_ids_by_user(user), None)

    def test_get_usernames_works(self):
        user = User("Tiina Testi", [])
        self.user_repository.add_user(user)
        self.assertEqual(self.user_repository.get_usernames(),
                         ["Testi Testinen", "Tiina Testi"])
