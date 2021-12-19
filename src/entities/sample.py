from services.reaction_logic import ReactionLogic
from services.abo_logic import ABOLogic


class Sample:

    """Luokka, jonka oliot sisältävät yksittäisten näytteiden tiedot.

    Attributes:
        sample_id: Näytteen näytetunniste
        comment: Näytekommentti
        anti_a: Anti-A:n tulos
        anti_b: Anti-B:n tulos
        anti_d: Anti-D:n tulos
        control: Kontrollin tulos
        a1_cell: A1-solun tulos
        b_cell: B-solun tulos
        timestamp: Näytteen tallettamisen aikaleima
    """

    def __init__(self, sample_id, comment, anti_a, anti_b,
                 anti_d, control, a1_cell, b_cell, timestamp):
        """Luokan konstruktori, joka luo uuden näyteolion.

        Args:
            sample_id (str): Näytteen näytetunniste
            comment (str): Näytekommentti
            anti_a (int): Anti-A:n tulos
            anti_b (int): Anti-B:n tulos
            anti_d (int): Anti-D:n tulos
            control (int): Kontrollin tulos
            a1_cell (int): A1-solun tulos
            b_cell (int): B-solun tulos
            timestamp (str): Näytteen tallettamisen kellonaika
        """

        self.__sample_id = sample_id
        self.__comment = comment
        self.__anti_a = anti_a
        self.__anti_b = anti_b
        self.__anti_d = anti_d
        self.__control = control
        self.__a1_cell = a1_cell
        self.__b_cell = b_cell
        self.__timestamp = timestamp

    @property
    def sample_id(self):
        """Palauttaa näytetunnisteen.

        Returns:
            Merkkijono: näytetunniste
        """

        return self.__sample_id

    @property
    def comment(self):
        """Palauttaa näytekommentin.

        Returns:
            Merkkijono: näytekommentti
        """

        return self.__comment

    @property
    def anti_a(self):
        """Palauttaa Anti-A:n tuloksen

        Returns:
            Kokonaisluku: Anti-A
        """

        return self.__anti_a

    @property
    def anti_b(self):
        """Palauttaa Anti-B:n tuloksen

        Returns:
            Kokonaisluku: Anti-B
        """

        return self.__anti_b

    @property
    def anti_d(self):
        """Palauttaa Anti-D:n tuloksen

        Returns:
            Kokonaisluku: Anti-D
        """

        return self.__anti_d

    @property
    def control(self):
        """Palauttaa kontrollin tuloksen

        Returns:
            Kokonaisluku: Kontrolli
        """

        return self.__control

    @property
    def a1_cell(self):
        """Palauttaa A1-solun tuloksen

        Returns:
            Kokonaisluku: A1-solu
        """

        return self.__a1_cell

    @property
    def b_cell(self):
        """Palauttaa B-solun tuloksen

        Returns:
            Kokonaisluku: B-solu
        """

        return self.__b_cell

    @property
    def timestamp(self):
        """Palauttaa näytteen tallentamisen aikaleiman

        Returns:
            Merkkijono: näytteen tallentamisen aikaleima (vvvv-kk-pp hh:mm:ss)
        """

        return self.__timestamp

    def run_checks(self):
        """Palauttaa näytteen tulosten tulkinnan ReactionLogic- ja ABOLogic-luokkien avulla

        Returns:
            Merkkijono: Näytteen tulosten tulkinta
        """

        if ReactionLogic.run_reaction_check(self.__anti_a, self.__anti_b,
                                            self.__anti_d, self.__control, self.__a1_cell, self.__b_cell) is True:
            return ABOLogic.run_abo_check(self.__anti_a, self.__anti_b, self.__anti_d,
                                          self.__a1_cell, self.__b_cell)

        return ReactionLogic.run_reaction_check(self.__anti_a, self.__anti_b, self.__anti_d,
                                                self.__control, self.__a1_cell, self.__b_cell)
