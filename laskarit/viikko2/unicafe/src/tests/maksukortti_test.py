import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_lataus_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 20)

    def test_ota_rahaa_toimii(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 5)

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(10)
        self.assertEqual(self.maksukortti.saldo, 0)

    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(20)
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_metodi_palauttaa_true_jos_rahaa_otettu(self):
        self.assertTrue(self.maksukortti.ota_rahaa(5))

    def test_metodi_palauttaa_false_jos_ota_rahaa_ei_onnistu(self):
        self.assertFalse(self.maksukortti.ota_rahaa(20))

    def test_saldo_euroissa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")