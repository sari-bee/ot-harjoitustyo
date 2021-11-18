from services.reaction_logic import Reaction_logic
from services.abo_logic import ABO_logic

class Sample:

    def __init__ (self, id: str):
        self.id=id
        self.anti_a = -1
        self.anti_b = -1
        self.anti_d = -1
        self.control = -1
        self.a_cell = -1
        self.b_cell = -1

    def input_reactions(self, anti_a: int, anti_b: int, anti_d:int, control:int, a_cell: int, b_cell:int):
        self.anti_a = anti_a
        self.anti_b = anti_b
        self.anti_d = anti_d
        self.control = control
        self.a_cell = a_cell
        self.b_cell = b_cell

    def __str__(self):
        return f"A {self.anti_a}, B {self.anti_b}, D {self.anti_d}, A1-solu: {self.a_cell}, B-solu: {self.b_cell}"

    def run_checks(self):
        reaction_checker = Reaction_logic()
        if (reaction_checker.run_reaction_check(self.anti_a, self.anti_b, self.anti_d, self.control, self.a_cell, self.b_cell)):
            abo_checker = ABO_logic()
            return abo_checker.run_abo_check(self.anti_a, self.anti_b, self.anti_d, self.a_cell, self.b_cell)
        else:
            return "Tee jatkotutkimuksia. Anna potilaalle tarvittaessa O RhD neg punasoluja, RhD neg trombosyyttejä ja AB plasmaa."

    def validate_reaction(self, reaction: str):
        valid_reactions = ["0", "1", "2", "3", "4", "DP"]
        reaction_strength = -1
        if reaction not in valid_reactions:
            return reaction_strength
        elif reaction == "DP":
            reaction_strength = 5
        else:
            reaction_strength = int(reaction)
        return reaction_strength


    