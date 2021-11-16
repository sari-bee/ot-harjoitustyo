class Reaction_logic:
    
    def __init__(self):
        self.acceptable_cell_reactions = (0, 3, 4)
        self.acceptable_plasma_reactions = (0, 2, 3, 4)
        self.list_exceptions = []

    def cell_reaction_logic(self, anti_a: int, anti_b: int, anti_d: int):
        if anti_a not in self.acceptable_cell_reactions:
            self.list_exceptions.append("Anti-A")
        if anti_b not in self.acceptable_cell_reactions:
            self.list_exceptions.append("Anti-B")
        if anti_d not in self.acceptable_cell_reactions:
            self.list_exceptions.append("Anti-D")
        return self.list_exceptions
        
        #list of reasons -> put in another service or smth
        #ylläpitäjälle mahdollisuus muokata reaktiovoimakkuuksia - "ylläpitäjätoiminnot"
        #päättelyt erilliseen tiedostoon?
