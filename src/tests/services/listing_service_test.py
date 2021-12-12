import unittest
from services.listing_service import ListingService
from entities.sample import Sample


class TestListingService(unittest.TestCase):

    def setUp(self):
        sample_one = Sample("123", "hei", 4, 0, 0, 0, 0,
                            4, "2021-12-05 20:00:00.00")
        sample_two = Sample("456", "moi", 4, 0, 4, 0, 0,
                            4, "2021-12-05 20:05:00.00")
        samples = [sample_one, sample_two]

    def revert_reactions_works():
        self.assertEqual(ListingService.revert_reactions(4), "4")

    def revert_reactions_works_with_DP():
        self.assertEqual(ListingService.revert_reactions(5), "DP")

    def list_samples_works():
        self.assertEqual(ListingService.list_samples(self.samples), "Näyte 123 (tallennettu 2021-12-05 20:00:00): Anti-A 4, Anti-B 0, Anti-D 0, Kontrolli 0, A1-solu 0, B-solu 0. \n Tulkinta: Potilaan veriryhmä on A RhD neg \n Kommentti: hei \n \n Näyte 123 (tallennettu 2021-12-05 20:05:00): Anti-A 4, Anti-B 0, Anti-D 4, Kontrolli 0, A1-solu 0, B-solu 0. \n Tulkinta: Potilaan veriryhmä on A RhD pos \n Kommentti: moi \n \n")

    def get_one_sample_works():
        self.assertEqual(ListingService.get_one_sample(
            sample_one), "Näyte 123 (tallennettu 2021-12-05 20:00:00): Anti-A 4, Anti-B 0, Anti-D 0, Kontrolli 0, A1-solu 0, B-solu 0. \n Tulkinta: Potilaan veriryhmä on A RhD neg \n Kommentti: hei")
