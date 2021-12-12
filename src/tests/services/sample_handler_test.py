import unittest
import os
from pathlib import Path
from services.sample_handler import SampleHandler
from services.listing_service import ListingService


class TestSampleHandler(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        path = os.path.join(dirname, "..", "test_samples.csv")
        Path(path).touch()
        with open(path, "w") as file:
            file.write("")
        self.sample_handler = SampleHandler()
        self.sample_handler.sample_repository.path = path

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

    def test_convert_reactions_works_with_DP(self):
        reaction = SampleHandler.convert_reactions("DP")
        self.assertEqual(reaction, 5)

    def test_check_input_works_with_invalid_reactions_antiA(self):
        self.assertEqual(SampleHandler.check_input(
            "6", "4", "0", "0", "0", "0"), "- Anti-A \n")

    def test_check_input_works_with_invalid_reactions_antiB(self):
        self.assertEqual(SampleHandler.check_input(
            "4", "8", "0", "0", "0", "0"), "- Anti-B \n")

    def test_check_input_works_with_invalid_reactions_antiD(self):
        self.assertEqual(SampleHandler.check_input(
            "4", "4", "hei", "0", "0", "0"), "- Anti-D \n")

    def test_check_input_works_with_invalid_reactions_control(self):
        self.assertEqual(SampleHandler.check_input(
            "4", "4", "0", "moi", "0", "0"), "- Kontrolli \n")

    def test_check_input_works_with_invalid_reactions_A1cell(self):
        self.assertEqual(SampleHandler.check_input(
            "4", "4", "0", "0", "7", "0"), "- A1-solu \n")

    def test_check_input_works_with_invalid_reactions_Bcell(self):
        self.assertEqual(SampleHandler.check_input(
            "4", "4", "0", "0", "0", "7"), "- B-solu \n")

    def test_check_input_works_with_valid_reactions(self):
        self.assertTrue(SampleHandler.check_input(
            "4", "4", "0", "0", "0", "0"))

    def test_get_all_samples_works(self):
        self.sample_handler.add_sample_data(
            "123", "hei", "4", "0", "0", "0", "0", "4")
        parts = self.sample_handler.get_all_samples(0).split("(")
        self.assertEqual(parts[0], "Näyte 123 ")

    def test_get_all_samples_works_with_empty_file(self):
        self.assertEqual(self.sample_handler.get_all_samples(
            0), "Ei tallennettuja näytteitä.")

    def test_get_sample_by_id_works(self):
        self.sample_handler.add_sample_data(
            "123", "hei", "4", "0", "0", "0", "0", "4")
        parts = self.sample_handler.get_sample_by_id("123").split("(")
        self.assertEqual(parts[0], "Näyte 123 ")

    def test_get_sample_by_id_when_id_not_found(self):
        self.sample_handler.add_sample_data(
            "123", "hei", "4", "0", "0", "0", "0", "4")
        self.assertEqual(self.sample_handler.get_sample_by_id(
            "456"), "Näytetunnisteella ei löydy näytettä")

    def test_get_number_of_samples_works(self):
        self.sample_handler.add_sample_data(
            "123", "hei", "4", "0", "0", "0", "0", "4")
        self.assertEqual(self.sample_handler.get_number_of_samples(), 1)
