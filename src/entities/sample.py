from services import reaction_logic

class Sample:

    def __init__ (self, id: str):
        self.id=id
        self.anti_a = -1
        self.anti_b = -1
        self.anti_d = -1
        self.control = -1
        self.a_cell = -1
        self.b_cell = -1

    def input_cell_reactions(self, anti_a: int, anti_b: int, anti_d:int):
        self.anti_a = anti_a
        self.anti_b = anti_b
        self.anti_d = anti_d
        #how to input dp's?

    def input_control_reaction(self, control: int):
        self.control = control

    def input_plasma_reactions(self, a: int, b: int):
        self.a_cell = a
        self.b_cell = b

    def print(self):
        print(f"Näyte {self.id}: A {self.anti_a}, B {self.anti_b}, D {self.anti_d}")

    def list_all_exceptions(self):
        print("Poikkeamat:")
        anti_a = self.anti_a
        anti_b = self.anti_b
        anti_d = self.anti_d
        check_reaction_logic = reaction_logic.Reaction_logic()
        print(check_reaction_logic.cell_reaction_logic(anti_a, anti_b, anti_d))