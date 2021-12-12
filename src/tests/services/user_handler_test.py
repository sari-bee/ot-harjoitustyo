import unittest
import os
from pathlib import Path
from services.user_handler import UserHandler


class TestUserHandler(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, "..", "test_users.csv")
        Path(path).touch()
        with open(path, "w") as file:
            file.write("")
        self.user_handler = UserHandler()
        self.user_handler.user_repository.path = path
        self.user_handler.add_new_user("Testi Testinen")

    def test_add_new_user_works(self):
        self.assertEqual(self.user_handler.add_new_user(
            "Tiina Testi").username, "Tiina Testi")

    def test_add_new_user_fails_with_duplicates(self):
        self.assertEqual(self.user_handler.add_new_user(
            "Testi Testinen"), None)

    def test_find_user_by_username_works(self):
        self.assertEqual(self.user_handler.find_user_by_username(
            "Testi Testinen").username, "Testi Testinen")

    def test_add_sample_and_get_samples_by_user_works(self):
        user = self.user_handler.find_user_by_username("Testi Testinen")
        self.user_handler.add_sample_to_user(user, "123")
        self.assertEqual(self.user_handler.get_samples_by_user(user), ["123"])

    def test_get_number_of_samples_works(self):
        user = self.user_handler.find_user_by_username("Testi Testinen")
        self.user_handler.add_sample_to_user(user, "123")
        self.assertEqual(self.user_handler.get_number_of_samples(user), 1)
