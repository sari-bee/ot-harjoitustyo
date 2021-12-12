import unittest
from entities.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Testi Testinen", ["123", "456"])

    def test_username_correct(self):
        self.assertTrue(self.user.username, "Testi Testinen")

    def test_init_sample_ids_correct(self):
        self.assertTrue(self.user.sample_ids[0], "123")

    def test_add_sample_id_works(self):
        self.user.add_sample_id("789")
        self.assertTrue(self.user.sample_ids[2], "789")
