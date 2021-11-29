import unittest
from services.sample_handler import SampleHandler


class TestSampleHandler(unittest.TestCase):
    def setUp(self):
        self.sample_handler = SampleHandler()

    def test_get_sample_data_works(self):
        self.sample_handler.add_sample_data(
            "123", "hei", "4", "0", "0", "0", "0", "4")
        data = self.sample_handler.get_sample_data("123")
        self.assertEqual(data[1], "hei")

    def test_adding_sample_works(self):
        self.assertTrue(self.sample_handler.add_sample_data(
            "123", "hei", "4", "0", "0", "0", "0", "4"))

    def test_adding_duplicates_fails(self):
        self.sample_handler.add_sample_data(
            "123", "hei", "4", "0", "0", "0", "0", "4")
        self.assertFalse(self.sample_handler.add_sample_data(
            "123", "hei", 4, 0, 0, 0, 0, 4))

    def test_get_results_works(self):
        self.sample_handler.add_sample_data(
            "123", "hei", "4", "0", "0", "0", "0", "4")
        self.assertEqual(self.sample_handler.get_results("123"),
                         "Potilaan veriryhmä on A RhD neg")

    def test_validate_correct_reaction(self):
        self.assertEqual(self.sample_handler.validate_reaction("4"), 4)

    def test_validate_DP_reaction(self):
        self.assertEqual(self.sample_handler.validate_reaction("DP"), 5)

    def test_validate_invalid_reaction(self):
        self.assertEqual(self.sample_handler.validate_reaction("8"), -1)
