import unittest
from entities.sample import Sample


class TestSample(unittest.TestCase):
    def setUp(self):
        self.sample = Sample(123)

    def test_init_reactions_correct(self):
        self.assertEqual(str(self.sample),
                         "A -1, B -1, D -1, A1-solu: -1, B-solu: -1")

    def test_input_reactions_correct(self):
        self.sample.input_reactions("4", "0", "0", "0", "0", "4")
        self.assertEqual(str(self.sample),
                         "A 4, B 0, D 0, A1-solu: 0, B-solu: 4")

    def test_validate_correct_reaction(self):
        self.assertEqual(self.sample.validate_reaction("4"), 4)

    def test_validate_DP_reaction(self):
        self.assertEqual(self.sample.validate_reaction("DP"), 5)

    def test_validate_invalid_reaction(self):
        self.assertEqual(self.sample.validate_reaction("8"), -1)

    def test_run_checks_works_valid_results(self):
        self.sample.anti_a = 4
        self.sample.anti_b = 0
        self.sample.anti_d = 4
        self.sample.control = 0
        self.sample.a_cell = 0
        self.sample.b_cell = 4
        result = self.sample.run_checks()
        self.assertEqual(result, "Potilaan veriryhmä on A RhD pos")

    def test_run_checks_works_invalid_results(self):
        self.sample.anti_a = 4
        self.sample.anti_b = 1
        self.sample.anti_d = 4
        self.sample.control = 0
        self.sample.a_cell = 0
        self.sample.b_cell = 4
        result = self.sample.run_checks()
        self.assertEqual(result, "Potilaan veriryhmä ei ole selvä. Havaitut ongelmat ovat \n- Heikko B-antigeeni\nTee jatkotutkimuksia. \n Anna potilaalle tarvittaessa O RhD neg punasoluja, RhD neg trombosyyttejä ja AB plasmaa.")

    def test_adding_comment_works(self):
        self.sample.input_comment("heippa")
        self.assertEqual(self.sample.comment, "heippa")
