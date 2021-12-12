class ABOLogic:

    @classmethod
    def run_abo_check(cls, anti_a: int, anti_b: int, anti_d: int, a1_cell: int, b_cell: int):
        cell_abo = ABOLogic.cell_reaction_abo(anti_a, anti_b)
        cell_d = ABOLogic.cell_reaction_d(anti_d)
        plasma_abo = ABOLogic.plasma_reaction_abo(a1_cell, b_cell)
        if cell_abo == plasma_abo:
            return f"Potilaan veriryhmä on {cell_abo} RhD {cell_d}"
        return f"Potilaan RhD-veriryhmä on RhD {cell_d}. \n Potilaan ABO-veriryhmä ei ole selvä. ABO on solupuolelta {cell_abo}, mutta plasmapuolelta {plasma_abo}. \n Tee jatkotutkimuksia ja anna potilaalle tarvittaessa O ryhmän punasoluja ja AB plasmaa."

    @classmethod
    def cell_reaction_abo(cls, anti_a: int, anti_b: int):
        positive_cell_reactions = [3, 4]
        negative_cell_reactions = [0]
        if anti_a in positive_cell_reactions and anti_b in positive_cell_reactions:
            return "AB"
        if anti_a in positive_cell_reactions and anti_b in negative_cell_reactions:
            return "A"
        if anti_b in positive_cell_reactions and anti_a in negative_cell_reactions:
            return "B"
        if anti_a in negative_cell_reactions and anti_b in negative_cell_reactions:
            return "O"
        return "?"

    @classmethod
    def cell_reaction_d(cls, anti_d: int):
        positive_d_reactions = [3, 4]
        negative_d_reactions = [0]
        if anti_d in positive_d_reactions:
            return "pos"
        if anti_d in negative_d_reactions:
            return "neg"
        return "?"

    @classmethod
    def plasma_reaction_abo(cls, a1_cell: int, b_cell: int):
        positive_plasma_reactions = [2, 3, 4]
        negative_plasma_reactions = [0]
        if a1_cell in positive_plasma_reactions and b_cell in positive_plasma_reactions:
            return "O"
        if a1_cell in negative_plasma_reactions and b_cell in positive_plasma_reactions:
            return "A"
        if a1_cell in positive_plasma_reactions and b_cell in negative_plasma_reactions:
            return "B"
        if a1_cell in negative_plasma_reactions and b_cell in negative_plasma_reactions:
            return "AB"
        return "?"
