import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_alussa_rahamaara_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_alussa_edullisten_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_alussa_maukkaiden_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kateisella_kassassa_rahaa_oikea_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_maukkaasti_kateisella_kassassa_rahaa_oikea_maara(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_edullisesti_kateisella_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_kateisella_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_edullisesti_kateisella_vaihtoraha_ok(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_syo_maukkaasti_kateisella_vaihtoraha_ok(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_maksu_ei_riita_syo_edullisesti_kateisella_kassassa_rahaa_oikea_maara(self):
        self.kassapaate.syo_edullisesti_kateisella(220)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maksu_ei_riita_syo_maukkaasti_kateisella_kassassa_rahaa_oikea_maara(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maksu_ei_riita_syo_edullisesti_kateisella_lounaiden_maara_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(220)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maksu_ei_riita_syo_maukkaasti_kateisella_kassassa_lounaiden_maara_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maksu_ei_riita_syo_edullisesti_kateisella_vaihtoraha_ok(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(220), 220)

    def test_maksu_ei_riita_syo_maukkaasti_kateisella_vaihtoraha_ok(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(300), 300)

    def test_syo_edullisesti_korttimaksu_toimii(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti))
    
    def test_syo_maukkaasti_korttimaksu_toimii(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti))

    def test_syo_edullisesti_kortilla_saldo_vahenee_oikein(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 760)

    def test_syo_maukkaasti_kortilla_saldo_vahenee_oikein(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo, 600)

    def test_syo_edullisesti_kortilla_lounaiden_maara_oikea(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_kortilla_lounaiden_maara_oikea(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_edullisesti_kortilla_ei_rahaa(self):
        uusimaksukortti = Maksukortti(10)
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(uusimaksukortti))
    
    def test_syo_maukkaasti_kortilla_ei_rahaa(self):
        uusimaksukortti = Maksukortti(10)
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(uusimaksukortti))

    def test_syo_edullisesti_kortilla_ei_rahaa_saldo_ei_vahene(self):
        uusimaksukortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(uusimaksukortti)
        self.assertEqual(uusimaksukortti.saldo, 10)

    def test_syo_maukkaasti_kortilla_ei_rahaa_saldo_ei_vahene(self):
        uusimaksukortti = Maksukortti(10)
        self.kassapaate.syo_maukkaasti_kortilla(uusimaksukortti)
        self.assertEqual(uusimaksukortti.saldo, 10)

    def test_syo_edullisesti_kortilla_ei_onnistu_lounaiden_maara_oikea(self):
        uusimaksukortti = Maksukortti(10)
        self.kassapaate.syo_edullisesti_kortilla(uusimaksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kortilla_ei_onnistu_lounaiden_maara_oikea(self):
        uusimaksukortti = Maksukortti(10)
        self.kassapaate.syo_maukkaasti_kortilla(uusimaksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_kassassa_rahaa_oikea_maara(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kateisella_kassassa_rahaa_oikea_maara(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kortin_saldo_kasvaa_ladatessa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 2000)
        self.assertEqual(self.maksukortti.saldo, 3000)

    def test_kassan_rahamaara_kasvaa_korttia_ladatessa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 2000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 102000)

    def test_saldon_lataus_negatiivisella_summalla_kassassa_rahaa_oikea_maara(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_saldon_lataus_negatiivisella_summalla_kortilla_rahaa_oikea_maara(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual(self.maksukortti.saldo, 1000)

