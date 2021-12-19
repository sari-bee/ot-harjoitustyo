import unittest
from entities.sample import Sample


class TestSample(unittest.TestCase):
    def setUp(self):
        self.sample = Sample("123", "hei",
                             4, 0, 0, 0, 0, 4, "2021-12-04 20:00:00.00")

    def test_getters(self):
        self.assertEqual(
            f"{self.sample.sample_id}, {self.sample.comment}, {self.sample.b_cell}", "123, hei, 4")

    def test_run_checks_works_valid_results(self):
        result = self.sample.run_checks().split("\n")
        self.assertEqual(result[0], "Potilaan veriryhmä on A RhD neg")

    def test_run_checks_works_invalid_results(self):
        sample = Sample("123", "hei",
                        4, 1, 4, 0, 0, 4, "2021-12-04  20:00:00.00")
        result = sample.run_checks().split("\n")
        self.assertEqual(
            result[0], "Potilaan veriryhmä ei ole selvä. Havaitut ongelmat ovat:")
