import unittest
from entities.user import User


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("Testi Testinen", ["123", "456"])

    def test_getters(self):
        self.assertTrue(
            f"{self.user.username}, {self.user.sample_ids[0]}", "Testi Testinen, 123")

    def test_add_sample_id_works(self):
        self.user.add_sample_id("789")
        self.assertTrue(self.user.sample_ids[2], "789")
