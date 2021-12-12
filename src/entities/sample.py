from services.reaction_logic import ReactionLogic
from services.abo_logic import ABOLogic


class Sample:

    def __init__(self, sample_id: str, comment: str, anti_a: int, anti_b: int, anti_d: int, control: int, a1_cell: int, b_cell: int, timestamp: str):
        self.__sample_id = sample_id
        self.__comment = comment
        self.__anti_a = anti_a
        self.__anti_b = anti_b
        self.__anti_d = anti_d
        self.__control = control
        self.__a1_cell = a1_cell
        self.__b_cell = b_cell
        self.__timestamp = timestamp

    @property
    def sample_id(self):
        return self.__sample_id

    @property
    def comment(self):
        return self.__comment

    @property
    def anti_a(self):
        return self.__anti_a

    @property
    def anti_b(self):
        return self.__anti_b

    @property
    def anti_d(self):
        return self.__anti_d

    @property
    def control(self):
        return self.__control

    @property
    def a1_cell(self):
        return self.__a1_cell

    @property
    def b_cell(self):
        return self.__b_cell

    @property
    def timestamp(self):
        return self.__timestamp

    def run_checks(self):
        if ReactionLogic.run_reaction_check(self.__anti_a, self.__anti_b, self.__anti_d, self.__control, self.__a1_cell, self.__b_cell) is True:
            return ABOLogic.run_abo_check(self.__anti_a, self.__anti_b, self.__anti_d, self.__a1_cell, self.__b_cell)
        return ReactionLogic.run_reaction_check(self.__anti_a, self.__anti_b, self.__anti_d, self.__control, self.__a1_cell, self.__b_cell)
