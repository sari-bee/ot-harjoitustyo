from repositories.sample_repository import SampleRepository
from entities.sample import Sample


class SampleHandler:

    def __init__(self):
        self.sample_repository = SampleRepository()

    def add_sample_data(self, sample_id: str, comment: str, anti_a: str, anti_b: str, anti_d: str, control: str, a1_cell: str, b1_cell: str):
        anti_a_reaction = self.validate_reaction(anti_a)
        anti_b_reaction = self.validate_reaction(anti_b)
        anti_d_reaction = self.validate_reaction(anti_d)
        control_reaction = self.validate_reaction(control)
        a1cell_reaction = self.validate_reaction(a1_cell)
        b1cell_reaction = self.validate_reaction(b1_cell)
        sample = Sample(sample_id, comment, anti_a_reaction, anti_b_reaction,
                        anti_d_reaction, control_reaction, a1cell_reaction, b1cell_reaction)
        return self.sample_repository.add_sample(sample)

    def get_sample_data(self, sample_id: str):
        sample = self.sample_repository.get_sample(sample_id)
        data = [sample.sample_id, sample.comment, sample.anti_a, sample.anti_b,
                sample.anti_d, sample.control, sample.a1_cell, sample.b_cell]
        return data

    def get_results(self, sample_id: str):
        sample = self.sample_repository.get_sample(sample_id)
        return sample.run_checks()

    def validate_reaction(self, reaction: str):
        valid_reactions = ["0", "1", "2", "3", "4", "DP"]
        reaction_strength = -1
        if reaction not in valid_reactions:
            return reaction_strength
        if reaction == "DP":
            reaction_strength = 5
        else:
            reaction_strength = int(reaction)
        return reaction_strength
