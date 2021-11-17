class ABO_logic:
    
    def __init__(self):
        self.positive_cell_reactions = [3, 4]
        self.negative_cell_reactions = [0]
        self.positive_d_reactions = [3, 4]
        self.negative_d_reactions = [0]
        self.positive_plasma_reactions = [2, 3, 4]
        self.negative_plasma_reactions = [0]

    def run_abo_check(self, anti_a: int, anti_b: int, anti_d: int, a: int, b: int):
        cell_abo = self.cell_reaction_abo(anti_a, anti_b)
        d = self.cell_reaction_d(anti_d)
        plasma_abo = self.plasma_reaction_abo(a, b)
        if cell_abo == plasma_abo:
            return f"Potilaan veriryhmä on {cell_abo} RhD {d}"
        else:
            return "ABO-logiikka ei toteudu!"


    def cell_reaction_abo(self, anti_a: int, anti_b: int):
        if anti_a in self.positive_cell_reactions and anti_b in self.positive_cell_reactions:
            return "AB"
        if anti_a in self.positive_cell_reactions and anti_b in self.negative_cell_reactions:
            return "A"
        if anti_b in self.positive_cell_reactions and anti_a in self.negative_cell_reactions:
            return "B"
        if anti_a in self.negative_cell_reactions and anti_b in self.negative_cell_reactions:
            return "O"
        else:
            return "?"
            

    def cell_reaction_d(self, anti_d: int):
        if anti_d in self.positive_d_reactions:
            return "pos"
        if anti_d in self.negative_d_reactions:
            return "neg"
        else:
            return "?"

    def plasma_reaction_abo(self, a:int, b: int):
        if a in self.positive_plasma_reactions and b in self.positive_plasma_reactions:
            return "O"
        if a in self.negative_plasma_reactions and b in self.positive_plasma_reactions:
            return "A"
        if a in self.positive_plasma_reactions and b in self.negative_plasma_reactions:
            return "B"
        if a in self.negative_plasma_reactions and b in self.negative_plasma_reactions:
            return "AB"
        else:
            return "?"