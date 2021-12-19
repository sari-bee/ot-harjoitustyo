from services.transfusion_directions import TransfusionDirections
from config import POS_ABO_CELL_REACTIONS, POS_ABO_PLASMA_REACTIONS, POS_D_CELL_REACTIONS


class ABOLogic:

    """Luokan metodit testaavat näytteen sisäisen veriryhmälogiikan toteutumista.
    """

    @classmethod
    def run_abo_check(cls, anti_a, anti_b, anti_d, a1_cell, b_cell):
        """Metodi, joka tarkistaa solu- ja plasmapuolen ABO-logiikan toteutumisen

        Args:
            anti_a (int): Anti-A-reaktiovoimakkuus
            anti_b (int): Anti-B-reaktiovoimakkuus
            anti_d (int): Anti-D-reaktiovoimakkuus
            a1_cell (int): A1-solun reaktiovoimakkuus
            b_cell (int): B-solun reaktiovoimakkuus

        Returns:
            Merkkijono: Veriryhmän tulkinta
        """

        cell_abo = ABOLogic.cell_reaction_abo(anti_a, anti_b)
        cell_d = ABOLogic.cell_reaction_d(anti_d)
        plasma_abo = ABOLogic.plasma_reaction_abo(a1_cell, b_cell)

        if cell_abo == plasma_abo:
            return f"Potilaan veriryhmä on {cell_abo} RhD {cell_d}\n" + TransfusionDirections.abo_clear(cell_d)

        return f"Potilaan RhD-veriryhmä on RhD {cell_d}.\nPotilaan ABO-veriryhmä ei ole selvä. ABO on solupuolelta {cell_abo}, mutta plasmapuolelta {plasma_abo}.\n" + TransfusionDirections.abo_unclear(cell_d)

    @classmethod
    def cell_reaction_abo(cls, anti_a, anti_b):
        """Metodi tulkitsee solupuolen ABO-veriryhmän

        Args:
            anti_a (int): Anti-A-reaktiovoimakkuus
            anti_b (int): Anti-B-reaktiovoimakkuus

        Returns:
            Merkkijono: Solupuolen ABO-veriryhmän tulkinta
        """

        positive_cell_reactions = [int(reaction)
                                   for reaction in POS_ABO_CELL_REACTIONS]

        if anti_a in positive_cell_reactions and anti_b in positive_cell_reactions:
            return "AB"
        if anti_a in positive_cell_reactions and anti_b == 0:
            return "A"
        if anti_b in positive_cell_reactions and anti_a == 0:
            return "B"
        if anti_a == 0 and anti_b == 0:
            return "O"
        return "?"

    @classmethod
    def cell_reaction_d(cls, anti_d):
        """Metodi tulkitsee solupuolen RhD-veriryhmän

        Args:
            anti_d (int): Anti-D-reaktiovoimakkuus

        Returns:
            Merkkijono: Solupuolen RhD-veriryhmän tulkinta
        """

        positive_d_reactions = [int(reaction)
                                for reaction in POS_D_CELL_REACTIONS]

        if anti_d in positive_d_reactions:
            return "pos"
        if anti_d == 0:
            return "neg"
        return "?"

    @classmethod
    def plasma_reaction_abo(cls, a1_cell, b_cell):
        """Metodi tulkitsee plasmapuolen ABO-veriryhmän

        Args:
            a1_cell (int): A1-solun reaktiovoimakkuus
            b_cell (int): B-solun reaktiovoimakkuus

        Returns:
            Merkkijono: Plasmapuolen ABO-veriryhmän tulkinta
        """

        positive_plasma_reactions = [
            int(reaction) for reaction in POS_ABO_PLASMA_REACTIONS]

        if a1_cell in positive_plasma_reactions and b_cell in positive_plasma_reactions:
            return "O"
        if a1_cell == 0 and b_cell in positive_plasma_reactions:
            return "A"
        if a1_cell in positive_plasma_reactions and b_cell == 0:
            return "B"
        if a1_cell == 0 and b_cell == 0:
            return "AB"
        return "?"
