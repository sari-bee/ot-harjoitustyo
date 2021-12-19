import unittest
import os
from pathlib import Path
from services.sample_handler import SampleHandler
from services.listing_service import ListingService
from config import SAMPLES_FILEPATH


class TestSampleHandler(unittest.TestCase):
    def setUp(self):
        Path(SAMPLES_FILEPATH).touch()
        with open(SAMPLES_FILEPATH, "w") as file:
            file.write("")
        self.sample_handler = SampleHandler()

    def test_check_input_works_with_invalid_reactions_antiA_anti_B_antiD(self):
        self.assertEqual(SampleHandler.check_input(
            "6", "8", "qwerty", "0", "0", "0"), "- Anti-A \n- Anti-B \n- Anti-D \n")

    def test_check_input_works_with_invalid_reactions_control_A1cell_Bcell(self):
        self.assertEqual(SampleHandler.check_input(
            "4", "4", "0", "moi", "7", "9"), "- Kontrolli \n- A1-solu \n- B-solu \n")

    def test_check_input_works_with_valid_reactions(self):
        self.assertTrue(SampleHandler.check_input(
            "4", "4", "0", "0", "0", "0"))

    def test_convert_reactions_works_with_DP(self):
        reaction = SampleHandler.convert_reactions("DP")
        self.assertEqual(reaction, 5)

    def test_adding_sample_works(self):
        self.assertTrue(self.sample_handler.add_sample_data(
            "123", "hei", "4", "0", "0", "0", "0", "4"))

    def test_adding_duplicates_fails(self):
        self.sample_handler.add_sample_data(
            "123", "hei", "4", "0", "0", "0", "0", "4")
        self.assertFalse(self.sample_handler.add_sample_data(
            "123", "hei", 4, 0, 0, 0, 0, 4))

    def test_get_all_samples_works(self):
        self.sample_handler.add_sample_data(
            "123", "hei", "4", "0", "0", "0", "0", "4")
        self.sample_handler.add_sample_data(
            "456", "hei", "4", "0", "2", "0", "0", "4")
        parts = self.sample_handler.get_all_samples(0).split("(")
        self.assertEqual(parts[0], "Näyte 456 ")

    def test_get_samples_by_several_ids_works(self):
        self.sample_handler.add_sample_data(
            "123", "hei", "4", "0", "0", "0", "0", "4")
        self.sample_handler.add_sample_data(
            "456", "hei", "4", "0", "0", "0", "0", "4")
        self.sample_handler.add_sample_data(
            "789", "-", "4", "3", "0", "0", "0", "4")
        parts = self.sample_handler.get_samples_by_several_ids(
            ["123", "456"], 0).split("(")
        self.assertEqual(parts[0], "Näyte 456 ")

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
        self.sample_handler.add_sample_data(
            "456", "moi", "4", "4", "0", "0", "0", "4")
        self.assertEqual(self.sample_handler.get_number_of_samples(), 2)

    def test_get_results_works(self):
        self.sample_handler.add_sample_data(
            "123", "hei", "4", "0", "0", "0", "0", "4")
        result = self.sample_handler.get_results("123").split("\n")
        self.assertEqual(str(result[0]),
                         "Potilaan veriryhmä on A RhD neg")
