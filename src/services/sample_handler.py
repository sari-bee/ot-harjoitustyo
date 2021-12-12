import os
from datetime import datetime
from repositories.sample_repository import SampleRepository
from entities.sample import Sample
from services.listing_service import ListingService


class SampleHandler:

    def __init__(self):
        dirname = os.path.dirname(__file__)
        self.sample_repository = SampleRepository(
            os.path.join(dirname, "../..", "data", "samples.csv"))

    @classmethod
    def check_input(cls, anti_a: str, anti_b: str, anti_d: str, control: str, a1_cell: str, b_cell: str):
        valid_reactions = ["0", "1", "2", "3", "4", "DP"]
        if anti_a not in valid_reactions:
            return False
        if anti_b not in valid_reactions:
            return False
        if anti_d not in valid_reactions:
            return False
        if control not in valid_reactions:
            return False
        if a1_cell not in valid_reactions:
            return False
        if b_cell not in valid_reactions:
            return False
        return True

    @classmethod
    def convert_reactions(cls, reaction: str):
        if reaction == "DP":
            reaction_strength = 5
        else:
            reaction_strength = int(reaction)
        return reaction_strength

    def add_sample_data(self, sample_id: str, comment: str, anti_a: str, anti_b: str, anti_d: str, control: str, a1_cell: str, b1_cell: str):
        anti_a_reaction = SampleHandler.convert_reactions(anti_a)
        anti_b_reaction = SampleHandler.convert_reactions(anti_b)
        anti_d_reaction = SampleHandler.convert_reactions(anti_d)
        control_reaction = SampleHandler.convert_reactions(control)
        a1cell_reaction = SampleHandler.convert_reactions(a1_cell)
        b1cell_reaction = SampleHandler.convert_reactions(b1_cell)
        timestamp = datetime.now()
        sample = Sample(sample_id, comment, anti_a_reaction, anti_b_reaction,
                        anti_d_reaction, control_reaction, a1cell_reaction, b1cell_reaction, timestamp)
        return self.sample_repository.add_sample(sample)

    def get_all_samples(self, sample_index: int):
        samples = self.sample_repository.read()
        if len(samples) == 0:
            return "Ei tallennettuja näytteitä."
        return ListingService.list_samples(samples, sample_index)

    def get_number_of_samples(self):
        samples = self.sample_repository.read()
        return len(samples)

    def get_sample_by_id(self, sample_id: str):
        sample = self.sample_repository.get_sample_by_id(sample_id)
        if sample is None:
            return "Näytetunnisteella ei löydy näytettä"
        return ListingService.get_one_sample(sample)

    def get_samples_by_several_ids(self, sample_ids: list, sample_index: int):
        samples = self.sample_repository.read()
        wanted_samples = []
        for sample in samples:
            if sample.sample_id in sample_ids:
                wanted_samples.append(sample)
        return ListingService.list_samples(wanted_samples, sample_index)

    def get_results(self, sample_id: str):
        sample = self.sample_repository.get_sample_by_id(sample_id)
        return sample.run_checks()
