import unittest
from services.abo_logic import ABOLogic


class TestABOLogic(unittest.TestCase):
    def setUp(self):
        self.abo_logic = ABOLogic()

    def test_run_abo_check_with_Aneg(self):
        self.assertEqual(str(self.abo_logic.run_abo_check(
            4, 0, 0, 0, 4)), "Potilaan veriryhmä on A RhD neg")

    def test_run_abo_check_with_Bneg(self):
        self.assertEqual(str(self.abo_logic.run_abo_check(
            0, 4, 0, 4, 0)), "Potilaan veriryhmä on B RhD neg")

    def test_run_abo_check_with_ABneg(self):
        self.assertEqual(str(self.abo_logic.run_abo_check(
            4, 4, 0, 0, 0)), "Potilaan veriryhmä on AB RhD neg")

    def test_run_abo_check_with_Oneg(self):
        self.assertEqual(str(self.abo_logic.run_abo_check(
            0, 0, 0, 4, 4)), "Potilaan veriryhmä on O RhD neg")

    def test_run_abo_check_with_Apos(self):
        self.assertEqual(str(self.abo_logic.run_abo_check(
            4, 0, 4, 0, 4)), "Potilaan veriryhmä on A RhD pos")

    def test_run_abo_check_with_Bpos(self):
        self.assertEqual(str(self.abo_logic.run_abo_check(
            0, 4, 4, 4, 0)), "Potilaan veriryhmä on B RhD pos")

    def test_run_abo_check_with_ABpos(self):
        self.assertEqual(str(self.abo_logic.run_abo_check(
            4, 4, 4, 0, 0)), "Potilaan veriryhmä on AB RhD pos")

    def test_run_abo_check_with_Opos(self):
        self.assertEqual(str(self.abo_logic.run_abo_check(
            0, 0, 4, 4, 4)), "Potilaan veriryhmä on O RhD pos")

    def test_run_abo_check_with_wrong_cell_reaction_strength(self):
        self.assertEqual(str(self.abo_logic.run_abo_check(2, 0, 0, 0, 4)),
                         "Potilaan RhD-veriryhmä on RhD neg. \n Potilaan ABO-veriryhmä ei ole selvä. ABO on solupuolelta ?, mutta plasmapuolelta A. \n Tee jatkotutkimuksia ja anna potilaalle tarvittaessa O ryhmän punasoluja ja AB plasmaa.")

    def test_run_abo_check_with_wrong_d_reaction_strength(self):
        self.assertEqual(str(self.abo_logic.run_abo_check(
            4, 0, 1, 0, 4)), "Potilaan veriryhmä on A RhD ?")

    def test_run_abo_check_with_wrong_plasma_reaction_strength(self):
        self.assertEqual(str(self.abo_logic.run_abo_check(4, 0, 0, 0, 1)),
                         "Potilaan RhD-veriryhmä on RhD neg. \n Potilaan ABO-veriryhmä ei ole selvä. ABO on solupuolelta A, mutta plasmapuolelta ?. \n Tee jatkotutkimuksia ja anna potilaalle tarvittaessa O ryhmän punasoluja ja AB plasmaa.")

    def test_run_abo_check_with_unacceptable_reactions(self):
        self.assertEqual(str(self.abo_logic.run_abo_check(4, 0, 0, 2, 4)),
                         "Potilaan RhD-veriryhmä on RhD neg. \n Potilaan ABO-veriryhmä ei ole selvä. ABO on solupuolelta A, mutta plasmapuolelta O. \n Tee jatkotutkimuksia ja anna potilaalle tarvittaessa O ryhmän punasoluja ja AB plasmaa.")
