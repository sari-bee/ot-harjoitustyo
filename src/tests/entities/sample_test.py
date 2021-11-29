import unittest
from entities.sample import Sample


class TestSample(unittest.TestCase):
    def setUp(self):
        self.sample = Sample("123", "hei", 4, 0, 0, 0, 0, 4)

    def test_init_reaction_correct(self):
        self.assertEqual(self.sample.b_cell, 4)

    def test_init_sample_id_correct(self):
        self.assertEqual(self.sample.sample_id, "123")

    def test_init_comment_correct(self):
        self.assertEqual(self.sample.comment, "hei")

    def test_run_checks_works_valid_results(self):
        result = self.sample.run_checks()
        self.assertEqual(result, "Potilaan veriryhmä on A RhD neg")

    def test_run_checks_works_invalid_results(self):
        sample = Sample("123", "hei", 4, 1, 4, 0, 0, 4)
        result = sample.run_checks()
        self.assertEqual(result, "Potilaan veriryhmä ei ole selvä. Havaitut ongelmat ovat \n- Heikko B-antigeeni\nTee jatkotutkimuksia. \n Anna potilaalle tarvittaessa O RhD neg punasoluja, RhD neg trombosyyttejä ja AB plasmaa.")
