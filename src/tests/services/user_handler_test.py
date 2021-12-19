import unittest
import os
from pathlib import Path
from services.user_handler import UserHandler
from config import USERS_FILEPATH


class TestUserHandler(unittest.TestCase):
    def setUp(self):
        Path(USERS_FILEPATH).touch()
        with open(USERS_FILEPATH, "w") as file:
            file.write("")
        self.user_handler = UserHandler()

    def test_add_new_user_works(self):
        self.assertEqual(self.user_handler.add_new_user(
            "Tiina Testi").username, "Tiina Testi")

    def test_add_new_user_fails_with_duplicates(self):
        self.user_handler.add_new_user("Testi Testinen")
        self.assertEqual(self.user_handler.add_new_user(
            "Testi Testinen"), None)

    def test_find_user_by_username_works(self):
        self.user_handler.add_new_user("Testi Testinen")
        self.assertEqual(self.user_handler.find_user_by_username(
            "Testi Testinen").username, "Testi Testinen")

    def test_add_sample_and_get_samples_by_user_works(self):
        self.user_handler.add_new_user("Testi Testinen")
        user = self.user_handler.find_user_by_username("Testi Testinen")
        self.user_handler.add_sample_to_user(user, "123")
        self.assertEqual(self.user_handler.get_samples_by_user(user), ["123"])

    def test_get_number_of_samples_works(self):
        self.user_handler.add_new_user("Testi Testinen")
        user = self.user_handler.find_user_by_username("Testi Testinen")
        self.user_handler.add_sample_to_user(user, "123")
        self.user_handler.add_sample_to_user(user, "456")
        self.assertEqual(self.user_handler.get_number_of_samples(user), 2)

    def test_get_all_users_works(self):
        self.user_handler.add_new_user("Testi Testinen")
        self.user_handler.add_new_user("Tiina Testi")
        self.assertEqual(self.user_handler.get_all_users(),
                         ['Testi Testinen', 'Tiina Testi'])

    def test_get_all_users_with_no_users(self):
        self.assertEqual(self.user_handler.get_all_users(),
                         "Ei vielä käyttäjiä.")
