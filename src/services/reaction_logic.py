class ReactionLogic:

    # Pylintin herjaukset muuttujista a, b ja d disabloitu, kun veriryhmät nyt vain sattuvat olemaan sen nimisiä.

    def __init__(self):
        self.acceptable_cell_reactions = [0, 3, 4, 5]
        self.acceptable_control_reactions = [0]
        self.acceptable_plasma_reactions = [0, 2, 3, 4]

    def run_reaction_check(self, anti_a: int, anti_b: int, anti_d: int, control: int, a: int, b: int):  # pylint: disable=invalid-name
        list_exceptions = []
        if anti_a == -1 or anti_b == -1 or anti_d == -1 or control == -1 or a == -1 or b == -1:
            return "Syötit virheellisen reaktiovoimakkuuden tai reaktiovoimakkuus puuttuu"
        self.cell_reaction_logic(list_exceptions, anti_a, anti_b, anti_d)
        self.control_logic(list_exceptions, control)
        self.plasma_reaction_logic(list_exceptions, a, b)
        if len(list_exceptions) == 0:
            return True
        result = "Potilaan veriryhmä ei ole selvä. Havaitut ongelmat ovat \n"
        for i in list_exceptions:
            result = result + i + "\n"
        result = result + "Tee jatkotutkimuksia. \n Anna potilaalle tarvittaessa O RhD neg punasoluja, RhD neg trombosyyttejä ja AB plasmaa."
        return result

    def cell_reaction_logic(self, list_exceptions: list, anti_a: int, anti_b: int, anti_d: int):
        if anti_a == 5:
            list_exceptions.append("- Kaksoispopulaatio A-antigeenilla")
        if anti_a not in self.acceptable_cell_reactions:
            list_exceptions.append("- Heikko A-antigeeni")
        if anti_b == 5:
            list_exceptions.append("- Kaksoispopulaatio B-antigeenilla")
        if anti_b not in self.acceptable_cell_reactions:
            list_exceptions.append("- Heikko B-antigeeni")
        if anti_d == 5:
            list_exceptions.append("- Kaksoispopulaatio D-antigeenilla")
        if anti_d not in self.acceptable_cell_reactions:
            list_exceptions.append("- Heikko D-antigeeni")

    def control_logic(self, list_exceptions: list, control: int):
        if control not in self.acceptable_control_reactions:
            list_exceptions.append("- Kontrolli positiivinen")

    def plasma_reaction_logic(self, list_exceptions: list, a: int, b: int):  # pylint: disable=invalid-name
        if a not in self.acceptable_plasma_reactions:
            list_exceptions.append("- Heikko anti-A-isoagglutiniini")
        if b not in self.acceptable_plasma_reactions:
            list_exceptions.append("- Heikko anti-B-isoagglutiniini")
