
from config import ABO_CLEAR, ABO_UNCLEAR, RHD_UNCLEAR, RHD_NEGATIVE, RHD_POSITIVE


class TransfusionDirections:

    """Luokka muodostaa verensiirto-ohjeet eri tapauksissa.

    Returns:
        Merkkijono: Verensiirto-ohje
    """

    @classmethod
    def abo_clear(cls, rhd):
        """Antaa verensiirto-ohjeet, jos ABO-määritys on selvä.

        Args:
            rhd (str): RhD-tulos

        Returns:
            Merkkijono: Verensiirto-ohje
        """

        if rhd == "pos":
            return f"Verensiirto-ohje: {ABO_CLEAR} {RHD_POSITIVE}"
        if rhd == "neg":
            return f"Verensiirto-ohje: {ABO_CLEAR} {RHD_NEGATIVE}"
        return f"Tee jatkotutkimuksia.\nVerensiirto-ohje: {ABO_CLEAR} {RHD_UNCLEAR}"

    @classmethod
    def abo_unclear(cls, rhd):
        """Antaa verensiirto-ohjeet, jos ABO-määritys on epäselvä.

        Args:
            rhd (str): RhD-tulos

        Returns:
            Merkkijono: Verensiirto-ohje
        """
        if rhd == "pos":
            return f"Tee jatkotutkimuksia.\nVerensiirto-ohje: {ABO_UNCLEAR} {RHD_POSITIVE}"
        if rhd == "neg":
            return f"Tee jatkotutkimuksia.\nVerensiirto-ohje: {ABO_UNCLEAR} {RHD_NEGATIVE}"
        return f"Tee jatkotutkimuksia.\nVerensiirto-ohje: {ABO_UNCLEAR} {RHD_UNCLEAR}"
