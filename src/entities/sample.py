from services.reaction_logic import ReactionLogic
from services.abo_logic import ABOLogic


class Sample:

    def __init__(self, sample_id: str, comment: str, anti_a: int, anti_b: int, anti_d: int, control: int, a1_cell: int, b_cell: int):
        self.sample_id = sample_id
        self.comment = comment
        self.anti_a = anti_a
        self.anti_b = anti_b
        self.anti_d = anti_d
        self.control = control
        self.a1_cell = a1_cell
        self.b_cell = b_cell

    def run_checks(self):
        reaction_checker = ReactionLogic()
        if reaction_checker.run_reaction_check(self.anti_a, self.anti_b, self.anti_d, self.control, self.a1_cell, self.b_cell) == True:
            abo_checker = ABOLogic()
            return abo_checker.run_abo_check(self.anti_a, self.anti_b, self.anti_d, self.a1_cell, self.b_cell)
        return reaction_checker.run_reaction_check(self.anti_a, self.anti_b, self.anti_d, self.control, self.a1_cell, self.b_cell)
