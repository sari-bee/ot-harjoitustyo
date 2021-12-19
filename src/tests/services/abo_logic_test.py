import unittest
from services.abo_logic import ABOLogic


class TestABOLogic(unittest.TestCase):

    def test_run_abo_check_with_Aneg(self):
        result = ABOLogic.run_abo_check(
            4, 0, 0, 0, 4).split("\n")
        self.assertEqual(str(result[0]), "Potilaan veriryhmä on A RhD neg")

    def test_run_abo_check_with_Bneg(self):
        result = ABOLogic.run_abo_check(
            0, 4, 0, 4, 0).split("\n")
        self.assertEqual(str(result[0]), "Potilaan veriryhmä on B RhD neg")

    def test_run_abo_check_with_ABneg(self):
        result = ABOLogic.run_abo_check(
            4, 4, 0, 0, 0).split("\n")
        self.assertEqual(str(result[0]), "Potilaan veriryhmä on AB RhD neg")

    def test_run_abo_check_with_Oneg(self):
        result = ABOLogic.run_abo_check(
            0, 0, 0, 4, 4).split("\n")
        self.assertEqual(str(result[0]), "Potilaan veriryhmä on O RhD neg")

    def test_run_abo_check_with_Opos(self):
        result = ABOLogic.run_abo_check(
            0, 0, 4, 4, 4).split("\n")
        self.assertEqual(str(result[0]), "Potilaan veriryhmä on O RhD pos")

    def test_run_abo_check_with_wrong_cell_reaction_strength(self):
        result = ABOLogic.run_abo_check(
            2, 0, 0, 0, 4).split("\n")
        self.assertEqual(str(result[0]),
                         "Potilaan RhD-veriryhmä on RhD neg.")

    def test_run_abo_check_with_wrong_d_reaction_strength(self):
        result = ABOLogic.run_abo_check(
            4, 0, 1, 0, 4).split("\n")
        self.assertEqual(str(result[0]), "Potilaan veriryhmä on A RhD ?")

    def test_run_abo_check_with_wrong_plasma_reaction_strength(self):
        result = ABOLogic.run_abo_check(
            4, 0, 0, 0, 1).split("\n")
        self.assertEqual(str(result[1]),
                         "Potilaan ABO-veriryhmä ei ole selvä. ABO on solupuolelta A, mutta plasmapuolelta ?.")

    def test_run_abo_check_with_unacceptable_reactions(self):
        result = ABOLogic.run_abo_check(
            4, 0, 0, 2, 4).split("\n")
        self.assertEqual(str(result[1]),
                         "Potilaan ABO-veriryhmä ei ole selvä. ABO on solupuolelta A, mutta plasmapuolelta O.")
