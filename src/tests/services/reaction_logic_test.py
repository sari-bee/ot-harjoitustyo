import unittest
from services.reaction_logic import Reaction_logic

class TestReactionLogic(unittest.TestCase):
    def setUp(self):
        pass

    def test_run_reaction_check_with_acceptable_reactions(self):
        reaction_logic = Reaction_logic()
        self.assertTrue(reaction_logic.run_reaction_check(4, 0, 0, 0, 0, 4))

    def test_run_reaction_check_with_unacceptable_reactions(self):
        reaction_logic = Reaction_logic()
        self.assertFalse(reaction_logic.run_reaction_check(4, 1, 0, 0, 0, 4))
