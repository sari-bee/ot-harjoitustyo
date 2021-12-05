import unittest
from services.reaction_logic import ReactionLogic


class TestReactionLogic(unittest.TestCase):
    def setUp(self):
        self.reaction_logic = ReactionLogic()

    def test_run_reaction_check_with_acceptable_reactions(self):
        self.assertTrue(
            self.reaction_logic.run_reaction_check(4, 0, 0, 0, 0, 4))

    def test_run_reaction_check_with_unacceptable_reactions_antiA(self):
        self.assertEqual(self.reaction_logic.run_reaction_check(
            1, 0, 0, 0, 0, 4), "Potilaan veriryhmä ei ole selvä. Havaitut ongelmat ovat: \n- Heikko A-antigeeni\nTee jatkotutkimuksia. Anna potilaalle O RhD neg punasoluja, RhD neg trombosyyttejä ja AB plasmaa.")

    def test_run_reaction_check_with_unacceptable_reactions_antiB(self):
        self.assertEqual(self.reaction_logic.run_reaction_check(
            0, 1, 0, 0, 4, 0), "Potilaan veriryhmä ei ole selvä. Havaitut ongelmat ovat: \n- Heikko B-antigeeni\nTee jatkotutkimuksia. Anna potilaalle O RhD neg punasoluja, RhD neg trombosyyttejä ja AB plasmaa.")

    def test_run_reaction_check_with_unacceptable_reactions_antiD(self):
        self.assertEqual(self.reaction_logic.run_reaction_check(
            0, 0, 1, 0, 4, 4), "Potilaan veriryhmä ei ole selvä. Havaitut ongelmat ovat: \n- Heikko D-antigeeni\nTee jatkotutkimuksia. Anna potilaalle O RhD neg punasoluja, RhD neg trombosyyttejä ja AB plasmaa.")

    def test_run_reaction_check_with_unacceptable_reactions_control(self):
        self.assertEqual(self.reaction_logic.run_reaction_check(
            4, 4, 0, 2, 0, 0), "Potilaan veriryhmä ei ole selvä. Havaitut ongelmat ovat: \n- Kontrolli positiivinen\nTee jatkotutkimuksia. Anna potilaalle O RhD neg punasoluja, RhD neg trombosyyttejä ja AB plasmaa.")

    def test_run_reaction_check_with_unacceptable_reactions_Acell(self):
        self.assertEqual(self.reaction_logic.run_reaction_check(
            0, 4, 0, 0, 1, 0), "Potilaan veriryhmä ei ole selvä. Havaitut ongelmat ovat: \n- Heikko anti-A-isoagglutiniini tai ylimääräinen reaktio A1-solulla\nTee jatkotutkimuksia. Anna potilaalle O RhD neg punasoluja, RhD neg trombosyyttejä ja AB plasmaa.")

    def test_run_reaction_check_with_unacceptable_reactions_Bcell(self):
        self.assertEqual(self.reaction_logic.run_reaction_check(
            4, 0, 0, 0, 0, 1), "Potilaan veriryhmä ei ole selvä. Havaitut ongelmat ovat: \n- Heikko anti-B-isoagglutiniini tai ylimääräinen reaktio B-solulla\nTee jatkotutkimuksia. Anna potilaalle O RhD neg punasoluja, RhD neg trombosyyttejä ja AB plasmaa.")

    def test_run_reaction_check_with_DP_reaction_antiA(self):
        self.assertEqual(self.reaction_logic.run_reaction_check(
            5, 0, 0, 0, 0, 4), "Potilaan veriryhmä ei ole selvä. Havaitut ongelmat ovat: \n- Kaksoispopulaatio A-antigeenilla; tarkista verensiirrot!\nTee jatkotutkimuksia. Anna potilaalle O RhD neg punasoluja, RhD neg trombosyyttejä ja AB plasmaa.")

    def test_run_reaction_check_with_DP_reaction_antiB(self):
        self.assertEqual(self.reaction_logic.run_reaction_check(
            0, 5, 0, 0, 4, 0), "Potilaan veriryhmä ei ole selvä. Havaitut ongelmat ovat: \n- Kaksoispopulaatio B-antigeenilla; tarkista verensiirrot!\nTee jatkotutkimuksia. Anna potilaalle O RhD neg punasoluja, RhD neg trombosyyttejä ja AB plasmaa.")

    def test_run_reaction_check_with_DP_reaction_antiD(self):
        self.assertEqual(self.reaction_logic.run_reaction_check(
            4, 0, 5, 0, 0, 4), "Potilaan veriryhmä ei ole selvä. Havaitut ongelmat ovat: \n- Kaksoispopulaatio D-antigeenilla; tarkista verensiirrot!\nTee jatkotutkimuksia. Anna potilaalle O RhD neg punasoluja, RhD neg trombosyyttejä ja AB plasmaa.")
