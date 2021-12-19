import unittest
import os
from pathlib import Path
from repositories.sample_repository import SampleRepository
from entities.sample import Sample
from config import SAMPLES_FILEPATH


class TestSampleRepository(unittest.TestCase):
    def setUp(self):
        path = SAMPLES_FILEPATH
        Path(path).touch()
        with open(path, "w") as file:
            file.write("")
        self.sample_repository = SampleRepository(path)

    def test_adding_several_samples_works(self):
        sample = Sample("123", "hei",
                        4, 0, 0, 0, 0, 4, "2021-12-04")
        self.sample_repository.add_sample(sample)
        sample2 = Sample("456", "hei",
                         4, 0, 0, 0, 0, 4, "2021-12-04")
        self.sample_repository.add_sample(sample2)
        self.assertTrue(len(self.sample_repository.read()) == 2)

    def test_adding_sample_fails_when_sample_is_duplicate(self):
        sample = Sample("123", "hei",
                        4, 0, 0, 0, 0, 4, "2021-12-04")
        self.sample_repository.add_sample(sample)
        sample2 = Sample("123", "hei",
                         4, 0, 0, 0, 0, 4, "2021-12-04")
        self.assertFalse(self.sample_repository.add_sample(sample2))

    def test_get_sample_works(self):
        sample = Sample("123", "hei",
                        4, 0, 0, 0, 0, 4, "2021-12-04")
        self.sample_repository.add_sample(sample)
        retrieved_sample = self.sample_repository.get_sample_by_id(
            "123")
        self.assertEqual(retrieved_sample.comment, "hei")

    def test_get_sample_returns_none_when_sample_not_found(self):
        sample = Sample("123", "hei",
                        4, 0, 0, 0, 0, 4, "2021-12-04")
        self.sample_repository.add_sample(sample)
        self.assertEqual(self.sample_repository.get_sample_by_id(
            "456"), None)
