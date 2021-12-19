import unittest
from services.reaction_logic import ReactionLogic


class TestReactionLogic(unittest.TestCase):

    def test_run_reaction_check_with_acceptable_reactions(self):
        self.assertTrue(
            ReactionLogic.run_reaction_check(4, 0, 0, 0, 0, 4))

    def test_run_reaction_check_with_unacceptable_reactions_antiA_antiB_antiD(self):
        result = ReactionLogic.run_reaction_check(
            2, 1, 1, 0, 0, 4).split("\n")
        self.assertEqual(str(
            result[1:4]), "['- Heikko A-antigeeni', '- Heikko B-antigeeni', '- Heikko D-antigeeni']")

    def test_run_reaction_check_with_unacceptable_reactions_control_A1cell_Bcell(self):
        result = ReactionLogic.run_reaction_check(
            4, 0, 0, 1, 1, 1).split("\n")
        self.assertEqual(str(
            result[1:4]), "['- Kontrolli positiivinen', '- Heikko anti-A-isoagglutiniini tai ylimääräinen reaktio A1-solulla', '- Heikko anti-B-isoagglutiniini tai ylimääräinen reaktio B-solulla']")

    def test_run_reaction_check_with_unacceptable_reactions_antiA_antiB_antiD(self):
        result = ReactionLogic.run_reaction_check(
            5, 5, 5, 0, 0, 4).split("\n")
        self.assertEqual(str(
            result[1:4]), "['- Kaksoispopulaatio A-antigeenilla; tarkista verensiirrot!', '- Kaksoispopulaatio B-antigeenilla; tarkista verensiirrot!', '- Kaksoispopulaatio D-antigeenilla; tarkista verensiirrot!']")
