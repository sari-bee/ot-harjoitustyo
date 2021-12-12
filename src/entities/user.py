class User:

    """Luokka, jonka oliot sisältävät yksittäisten käyttäjien tiedot.

    Attributes:
        username: Käyttäjätunnus
        sample_ids: Lista käyttäjätunnukseen liitetyistä näytetunnisteista
    """

    def __init__(self, username, sample_ids):
        """Luokan konstruktori, joka luo uuden käyttäjäolion

        Args:
            username (str): Käyttäjätunnus
            sample_ids (list): Lista käyttäjätunnukseen liitetyistä näytetunnisteista
        """
        self.__username = username
        self.__sample_ids = sample_ids

    @property
    def username(self):
        """Palauttaa käyttäjätunnuksen

        Returns:
            Merkkijono: käyttäjätunnus
        """
        return self.__username

    @property
    def sample_ids(self):
        """Palauttaa listan käyttäjätunnukseen liitettyjä näytetunnisteita

        Returns:
            Lista: käyttäjätunnukset
        """
        return self.__sample_ids

    def add_sample_id(self, sample_id):
        """Lisää uuden näytetunnisteen käyttäjätunnuskohtaiseen listaan

        Args:
            sample_id (str): Näytetunniste
        """
        self.__sample_ids.append(sample_id)
