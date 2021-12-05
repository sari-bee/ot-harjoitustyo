import os
from datetime import datetime
from repositories.sample_repository import SampleRepository
from entities.sample import Sample


class SampleHandler:

    def __init__(self):
        dirname = os.path.dirname(__file__)
        self.sample_repository = SampleRepository(
            os.path.join(dirname, "../..", "data", "samples.csv"))

    def check_input(self, anti_a: str, anti_b: str, anti_d: str, control: str, a1_cell: str, b_cell: str):
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

    def convert_reactions(self, reaction: str):
        if reaction == "DP":
            reaction_strength = 5
        else:
            reaction_strength = int(reaction)
        return reaction_strength

    def revert_reactions(self, reaction_strength: int):
        if reaction_strength == 5:
            reaction = "DP"
        else:
            reaction = str(reaction_strength)
        return reaction

    def add_sample_data(self, sample_id: str, comment: str, anti_a: str, anti_b: str, anti_d: str, control: str, a1_cell: str, b1_cell: str):
        anti_a_reaction = self.convert_reactions(anti_a)
        anti_b_reaction = self.convert_reactions(anti_b)
        anti_d_reaction = self.convert_reactions(anti_d)
        control_reaction = self.convert_reactions(control)
        a1cell_reaction = self.convert_reactions(a1_cell)
        b1cell_reaction = self.convert_reactions(b1_cell)
        timestamp = datetime.now()
        sample = Sample(sample_id, comment, anti_a_reaction, anti_b_reaction,
                        anti_d_reaction, control_reaction, a1cell_reaction, b1cell_reaction, timestamp)
        return self.sample_repository.add_sample(sample)

    def get_all_samples(self, sample_index: int):
        samples = self.sample_repository.read()
        if len(samples) == 0:
            return "Ei tallennettuja näytteitä."
        listing = ""
        samples.sort(key=lambda sample: (sample.timestamp), reverse=True)
        begin = sample_index
        end = sample_index+5
        for sample in samples[begin:end]:
            timeparts = sample.timestamp.split(".")
            time = timeparts[0]
            anti_a = self.revert_reactions(sample.anti_a)
            anti_b = self.revert_reactions(sample.anti_b)
            anti_d = self.revert_reactions(sample.anti_d)
            control = self.revert_reactions(sample.control)
            a1_cell = self.revert_reactions(sample.a1_cell)
            b_cell = self.revert_reactions(sample.b_cell)
            listing = listing + \
                f"Näyte {sample.sample_id} (tallennettu {time}): Anti-A {anti_a}, Anti-B {anti_b}, Anti-D {anti_d}, Kontrolli {control}, A1-solu {a1_cell}, B-solu {b_cell}. \n Tulkinta: {self.get_results(sample.sample_id)} \n \n"
        return listing

    def get_number_of_samples(self):
        samples = self.sample_repository.read()
        return len(samples)

    def get_sample_by_id(self, sample_id: str):
        sample = self.sample_repository.get_sample_by_id(sample_id)
        if sample is None:
            return "Näytetunnisteella ei löydy näytettä"
        timeparts = sample.timestamp.split(".")
        time = timeparts[0]
        anti_a = self.revert_reactions(sample.anti_a)
        anti_b = self.revert_reactions(sample.anti_b)
        anti_d = self.revert_reactions(sample.anti_d)
        control = self.revert_reactions(sample.control)
        a1_cell = self.revert_reactions(sample.a1_cell)
        b_cell = self.revert_reactions(sample.b_cell)
        sample_data = f"Näyte {sample.sample_id} (tallennettu {time}): Anti-A {anti_a}, Anti-B {anti_b}, Anti-D {anti_d}, Kontrolli {control}, A1-solu {a1_cell}, B-solu {b_cell}. \n Tulkinta: {self.get_results(sample.sample_id)}"
        return sample_data

    def get_results(self, sample_id: str):
        sample = self.sample_repository.get_sample_by_id(sample_id)
        return sample.run_checks()
