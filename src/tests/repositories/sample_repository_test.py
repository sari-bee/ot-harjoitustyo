import unittest
from repositories.sample_repository import SampleRepository
from entities.sample import Sample


class TestSample(unittest.TestCase):
    def setUp(self):
        self.sample_repository = SampleRepository()

    def test_init_creates_empty_list(self):
        self.assertTrue(len(self.sample_repository.samples) == 0)

    def test_adding_several_samples_to_list_works(self):
        sample = Sample("123", "hei", 4, 0, 0, 0, 0, 4)
        self.sample_repository.add_sample(sample)
        sample2 = Sample("456", "hei", 4, 0, 0, 0, 0, 4)
        self.sample_repository.add_sample(sample2)
        self.assertTrue(len(self.sample_repository.samples) == 2)

    def test_adding_sample_to_list_fails_when_sample_is_duplicate(self):
        sample = Sample("123", "hei", 4, 0, 0, 0, 0, 4)
        self.sample_repository.add_sample(sample)
        sample2 = Sample("123", "hei", 4, 0, 0, 0, 0, 4)
        self.assertFalse(self.sample_repository.add_sample(sample2))

    def test_get_sample_works(self):
        sample = Sample("123", "hei", 4, 0, 0, 0, 0, 4)
        self.sample_repository.add_sample(sample)
        retrieved_sample = self.sample_repository.get_sample("123")
        self.assertEqual(retrieved_sample.comment, "hei")

    def test_get_sample_returns_none_when_sample_not_found(self):
        sample = Sample("123", "hei", 4, 0, 0, 0, 0, 4)
        self.sample_repository.add_sample(sample)
        self.assertEqual(self.sample_repository.get_sample("456"), None)
