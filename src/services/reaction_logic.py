class ReactionLogic:

    @classmethod
    def run_reaction_check(cls, anti_a: int, anti_b: int, anti_d: int, control: int, a1_cell: int, b_cell: int):
        list_exceptions = []
        ReactionLogic.cell_reaction_logic(
            list_exceptions, anti_a, anti_b, anti_d)
        ReactionLogic.control_logic(list_exceptions, control)
        ReactionLogic.plasma_reaction_logic(list_exceptions, a1_cell, b_cell)
        if len(list_exceptions) == 0:
            return True
        result = "Potilaan veriryhmä ei ole selvä. Havaitut ongelmat ovat: \n"
        for i in list_exceptions:
            result = result + i + "\n"
        result = result + "Tee jatkotutkimuksia. Anna potilaalle O RhD neg punasoluja, RhD neg trombosyyttejä ja AB plasmaa."
        return result

    @classmethod
    def cell_reaction_logic(cls, list_exceptions: list, anti_a: int, anti_b: int, anti_d: int):
        acceptable_cell_reactions = [0, 3, 4, 5]
        if anti_a == 5:
            list_exceptions.append(
                "- Kaksoispopulaatio A-antigeenilla; tarkista verensiirrot!")
        if anti_a not in acceptable_cell_reactions:
            list_exceptions.append("- Heikko A-antigeeni")
        if anti_b == 5:
            list_exceptions.append(
                "- Kaksoispopulaatio B-antigeenilla; tarkista verensiirrot!")
        if anti_b not in acceptable_cell_reactions:
            list_exceptions.append("- Heikko B-antigeeni")
        if anti_d == 5:
            list_exceptions.append(
                "- Kaksoispopulaatio D-antigeenilla; tarkista verensiirrot!")
        if anti_d not in acceptable_cell_reactions:
            list_exceptions.append("- Heikko D-antigeeni")

    @classmethod
    def control_logic(cls, list_exceptions: list, control: int):
        acceptable_control_reactions = [0]
        if control not in acceptable_control_reactions:
            list_exceptions.append("- Kontrolli positiivinen")

    @classmethod
    def plasma_reaction_logic(cls, list_exceptions: list, a1_cell: int, b_cell: int):
        acceptable_plasma_reactions = [0, 2, 3, 4]
        if a1_cell not in acceptable_plasma_reactions:
            list_exceptions.append(
                "- Heikko anti-A-isoagglutiniini tai ylimääräinen reaktio A1-solulla")
        if b_cell not in acceptable_plasma_reactions:
            list_exceptions.append(
                "- Heikko anti-B-isoagglutiniini tai ylimääräinen reaktio B-solulla")
