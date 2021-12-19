import unittest
from services.transfusion_directions import TransfusionDirections


class TestTransfusionDirections(unittest.TestCase):

    def test_abo_unclear_printing(self):
        result = TransfusionDirections.abo_unclear("pos").split("\n")
        self.assertEqual(result[0], "Tee jatkotutkimuksia.")
