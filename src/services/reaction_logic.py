from services.transfusion_directions import TransfusionDirections
from config import POS_ABO_CELL_REACTIONS, POS_ABO_PLASMA_REACTIONS, POS_D_CELL_REACTIONS


class ReactionLogic:

    """
    Luokan metodit tarkistavat, ovatko näytteen reaktiot sopivia veriryhmän tulkintaan
    vai onko jo yksittäisessä reaktiossa jotakin, mikä tekee veriryhmästä epäselvän.
    """

    @classmethod
    def run_reaction_check(cls, anti_a, anti_b, anti_d, control, a1_cell, b_cell):
        """Metodi, joka koostaa listan havaituista poikkeamista

        Args:
            anti_a (int): Anti-A-reaktiovoimakkuus
            anti_b (int): Anti-B-reaktiovoimakkuus
            anti_d (int): Anti-D-reaktiovoimakkuus
            control (int): Kontrollin reaktiovoimakkuus
            a1_cell (int): A1-solun reaktiovoimakkuus
            b_cell (int): B-solun reaktiovoimakkuus

        Returns:
            Merkkijono: Listaus havaituista poikkeamista
            True: Jos poikkeamalista on tyhjä (eli jos poikkeamia ei havaittu)
        """

        list_exceptions = []
        ReactionLogic.cell_reaction_logic(
            list_exceptions, anti_a, anti_b, anti_d)
        ReactionLogic.control_logic(list_exceptions, control)
        ReactionLogic.plasma_reaction_logic(list_exceptions, a1_cell, b_cell)

        if len(list_exceptions) == 0:
            return True

        result = "Potilaan veriryhmä ei ole selvä. Havaitut ongelmat ovat:\n"
        for i in list_exceptions:
            result = result + i + "\n"

        result = result + TransfusionDirections.abo_unclear("?")
        return result

    @classmethod
    def cell_reaction_logic(cls, list_exceptions, anti_a, anti_b, anti_d):
        """Tarkistaa ovatko solupuolen reaktioiden reaktiovoimakkuudet sopivat veriryhmän tulkintaan
        eli onko jo yksittäisessä reaktiossa jotakin, mikä tekee veriryhmästä epäselvän.

        Args:
            list_exceptions (list): Lista, johon kerätään mahdolliset poikkeamat
            anti_a (int): Anti-A:n reaktiovoimakkuus
            anti_b (int): Anti-B:n reaktiovoimakkuus
            anti_d (int): Anti-D:n reaktiovoimakkuus
        """

        acceptable_abo_cell_reactions = [
            int(reaction) for reaction in POS_ABO_CELL_REACTIONS]
        acceptable_abo_cell_reactions.append(0)

        if anti_a == 5:
            list_exceptions.append(
                "- Kaksoispopulaatio A-antigeenilla; tarkista verensiirrot!")
        elif anti_a not in acceptable_abo_cell_reactions:
            list_exceptions.append("- Heikko A-antigeeni")
        if anti_b == 5:
            list_exceptions.append(
                "- Kaksoispopulaatio B-antigeenilla; tarkista verensiirrot!")
        elif anti_b not in acceptable_abo_cell_reactions:
            list_exceptions.append("- Heikko B-antigeeni")

        acceptable_d_reactions = [int(reaction)
                                  for reaction in POS_D_CELL_REACTIONS]
        acceptable_d_reactions.append(0)

        if anti_d == 5:
            list_exceptions.append(
                "- Kaksoispopulaatio D-antigeenilla; tarkista verensiirrot!")
        elif anti_d not in acceptable_d_reactions:
            list_exceptions.append("- Heikko D-antigeeni")

    @classmethod
    def control_logic(cls, list_exceptions, control):
        """Tarkistaa että kontrolli on negatiivinen eli että veriryhmän voi tulkita

        Args:
            list_exceptions (list): Lista, johon kerätään mahdolliset poikkeamat
            control (int): Kontrollin reaktiovoimakkuus
        """

        if control != 0:
            list_exceptions.append("- Kontrolli positiivinen")

    @classmethod
    def plasma_reaction_logic(cls, list_exceptions, a1_cell, b_cell):
        """Tarkistaa ovat plasmapuolen reaktioiden reaktiovoimakkuudet sopivat veriryhmän tulkintaan
        eli onko jo yksittäisessä reaktiossa jotakin, mikä tekee veriryhmästä epäselvän.

        Args:
            list_exceptions (list): Lista, johon kerätään mahdolliset poikkeamat
            a1_cell (int): A1-solun reaktiovoimakkuus
            b_cell (int): B-solun reaktiovoimakkuus
        """

        acceptable_plasma_reactions = [
            int(reaction) for reaction in POS_ABO_PLASMA_REACTIONS]
        acceptable_plasma_reactions.append(0)

        if a1_cell not in acceptable_plasma_reactions:
            list_exceptions.append(
                "- Heikko anti-A-isoagglutiniini tai ylimääräinen reaktio A1-solulla")
        if b_cell not in acceptable_plasma_reactions:
            list_exceptions.append(
                "- Heikko anti-B-isoagglutiniini tai ylimääräinen reaktio B-solulla")
