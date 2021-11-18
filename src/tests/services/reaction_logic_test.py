import unittest
from services.reaction_logic import Reaction_logic

class TestReactionLogic(unittest.TestCase):
    def setUp(self):
        self.reaction_logic = Reaction_logic()

    def test_run_reaction_check_with_acceptable_reactions(self):
        self.assertTrue(self.reaction_logic.run_reaction_check(4, 0, 0, 0, 0, 4))

    def test_run_reaction_check_with_unacceptable_reactions_antiA(self):
        self.assertFalse(self.reaction_logic.run_reaction_check(1, 0, 0, 0, 0, 4))

    def test_run_reaction_check_with_unacceptable_reactions_antiB(self):
        self.assertFalse(self.reaction_logic.run_reaction_check(0, 1, 0, 0, 4, 0))

    def test_run_reaction_check_with_unacceptable_reactions_antiD(self):
        self.assertFalse(self.reaction_logic.run_reaction_check(0, 0, 1, 0, 4, 4))

    def test_run_reaction_check_with_unacceptable_reactions_control(self):
        self.assertFalse(self.reaction_logic.run_reaction_check(4, 4, 0, 2, 0, 0))

    def test_run_reaction_check_with_unacceptable_reactions_Acell(self):
        self.assertFalse(self.reaction_logic.run_reaction_check(0, 4, 0, 0, 1, 0))

    def test_run_reaction_check_with_unacceptable_reactions_Bcell(self):
        self.assertFalse(self.reaction_logic.run_reaction_check(4, 0, 0, 0, 0, 1))

    def test_run_reaction_check_with_minus1_reaction(self):
        self.assertFalse(self.reaction_logic.run_reaction_check(4, -1, 0, 0, 0, 1))

    def test_run_reaction_check_with_DP_reaction_antiA(self):
        self.assertFalse(self.reaction_logic.run_reaction_check(5, 0, 0, 0, 0, 4))

    def test_run_reaction_check_with_DP_reaction_antiB(self):
        self.assertFalse(self.reaction_logic.run_reaction_check(0, 5, 0, 0, 4, 0))

    def test_run_reaction_check_with_DP_reaction_antiD(self):
        self.assertFalse(self.reaction_logic.run_reaction_check(4, 0, 5, 0, 0, 4))
