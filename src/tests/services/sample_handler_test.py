import unittest
from services.sample_handler import SampleHandler


class TestSampleHandler(unittest.TestCase):
    def setUp(self):
        self.sample_handler = SampleHandler()

    def test_sample_id_add_and_get(self):
        self.sample_handler.add_sample_id("123")
        self.assertEqual(self.sample_handler.get_sample_id(), "123")

    def test_comment_add_and_get(self):
        self.sample_handler.add_comment("heippa")
        self.assertEqual(self.sample_handler.get_comment(), "heippa")

    def test_add_reactions_works(self):
        self.assertTrue(self.sample_handler.add_reactions(
            "4", "4", "4", "0", "0", "0"))

    def test_get_results(self):
        self.sample_handler.add_reactions("4", "4", "4", "0", "0", "0")
        self.assertEqual(self.sample_handler.get_results(),
                         "Potilaan veriryhmä on AB RhD pos")
