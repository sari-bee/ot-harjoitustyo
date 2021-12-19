import unittest
from services.listing_service import ListingService
from entities.sample import Sample


class TestListingService(unittest.TestCase):

    def setUp(self):
        self.sample_one = Sample("123", "hei", 4, 0, 0, 0, 0,
                                 4, "2021-12-05 20:00:00.00")
        self.sample_two = Sample("456", "moi", 4, 0, 4, 0, 0,
                                 4, "2021-12-05 20:05:00.00")
        self.samples = [self.sample_one, self.sample_two]

    def test_revert_reactions_works(self):
        self.assertEqual(ListingService.revert_reactions(4), "4")

    def test_revert_reactions_works_with_DP(self):
        self.assertEqual(ListingService.revert_reactions(5), "DP")

    def test_list_samples_works(self):
        result = ListingService.list_samples(self.samples, 0).split("\n")
        self.assertEqual(f"{result[0]}{result[5]}", "Näyte 456 (tallennettu 2021-12-05 20:05:00): Anti-A 4, Anti-B 0, Anti-D 4, Kontrolli 0, A1-solu 0, B-solu 4.Näyte 123 (tallennettu 2021-12-05 20:00:00): Anti-A 4, Anti-B 0, Anti-D 0, Kontrolli 0, A1-solu 0, B-solu 4.")

    def test_get_one_sample_works(self):
        result = ListingService.get_one_sample(self.sample_one).split("\n")
        self.assertEqual(
            result[0], "Näyte 123 (tallennettu 2021-12-05 20:00:00): Anti-A 4, Anti-B 0, Anti-D 0, Kontrolli 0, A1-solu 0, B-solu 4.")
