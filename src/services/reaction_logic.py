class Reaction_logic:
    
    def __init__(self):
        self.acceptable_cell_reactions = [0, 3, 4]
        self.acceptable_control_reactions = [0]
        self.acceptable_plasma_reactions = [0, 2, 3, 4]

    def run_reaction_check(self, anti_a: int, anti_b: int, anti_d: int, control: int, a: int, b: int):
        list_exceptions = []
        reactions_ok = False
        self.cell_reaction_logic(list_exceptions, anti_a, anti_b, anti_d)
        self.control_logic(list_exceptions, control)
        self.plasma_reaction_logic(list_exceptions, a, b)
        if len(list_exceptions) == 0:
            reactions_ok = True
            print("Reaktiovoimakkuudet kunnossa")
            return reactions_ok
        else:
            print("Poikkeamia oli seuraavissa reaktioissa:")
            for i in list_exceptions:
                print(i)
            print("Tee jatkotutkimuksia. Anna potilaalle tarvittaessa O RhD neg punasoluja, RhD neg trombosyyttejä ja AB plasmaa.")
            return reactions_ok

    def cell_reaction_logic(self, list_exceptions: list, anti_a: int, anti_b: int, anti_d: int):
        if anti_a not in self.acceptable_cell_reactions:
            list_exceptions.append("Anti-A")
        if anti_b not in self.acceptable_cell_reactions:
            list_exceptions.append("Anti-B")
        if anti_d not in self.acceptable_cell_reactions:
            list_exceptions.append("Anti-D")

    def control_logic(self, list_exceptions: list, control: int):
        if control not in self.acceptable_control_reactions:
            list_exceptions.append("Kontrolli")

    def plasma_reaction_logic(self, list_exceptions: list, a:int, b: int):
        if a not in self.acceptable_plasma_reactions:
            list_exceptions.append("A1-solu")
        if b not in self.acceptable_plasma_reactions:
            list_exceptions.append("B-solu")

