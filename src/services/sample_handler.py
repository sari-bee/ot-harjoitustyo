from entities.sample import Sample
#from repositories.sample_repository import SampleRepository

# Pylintin herjaukset muuttujista a, b ja d disabloitu, kun veriryhmät nyt vain sattuvat olemaan sen nimisiä.

class SampleHandler:

    def __init__(self):
        #self.sample_repository = SampleRepository()
        self.sample = Sample()

    def add_sample_id(self, sample_id: str):
        self.sample.sample_id = sample_id

    def get_sample_id(self):
        return self.sample.sample_id

    def add_comment(self, comment: str):
        self.sample.comment = comment

    def get_comment(self):
        return self.sample.comment

    def add_reactions(self, anti_a: str, anti_b: str, anti_d: str, control: str, a: str, b: str):  # pylint: disable=invalid-name
        anti_a_reaction = self.sample.validate_reaction(anti_a)
        anti_b_reaction = self.sample.validate_reaction(anti_b)
        anti_d_reaction = self.sample.validate_reaction(anti_d)
        control_reaction = self.sample.validate_reaction(control)
        a_reaction = self.sample.validate_reaction(a)
        b_reaction = self.sample.validate_reaction(b)
        self.sample.input_reactions(anti_a_reaction, anti_b_reaction,
                                    anti_d_reaction, control_reaction, a_reaction, b_reaction)
        return True

    def get_results(self):
        return self.sample.run_checks()
