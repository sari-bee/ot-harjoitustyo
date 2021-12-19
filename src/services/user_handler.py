from repositories.user_repository import UserRepository
from entities.user import User
from config import USERS_FILEPATH


class UserHandler:

    """Luokka, joka hoitaa kaiken käyttäjiin liittyvän logiikan käyttöliittymän kanssa.

    Attributes:
        user_repository: Ohjelman käynnistyskertakohtainen käyttäjärepository
    """

    def __init__(self):
        """Luokan konstruktori, joka luo käyttäjäpalvelun ja käyttäjärepositoryn
        """

        self.user_repository = UserRepository(USERS_FILEPATH)

    def add_new_user(self, username):
        """Uuden käyttäjän lisäys käyttäjärepositorioon

        Args:
            username (str): Käyttäjätunnus

        Returns:
            None: Jos käyttäjän lisääminen ei onnistu (käyttäjätunnus on jo käytössä)
            User: Jos käyttäjän lisääminen onnistuu
        """

        samples = []
        user = User(username, samples)
        success = self.user_repository.add_user(user)
        if not success:
            return None
        return user

    def find_user_by_username(self, username):
        """Hakee käyttäjän käyttäjätunnuksen perusteella

        Args:
            username (str): Käyttäjätunnus

        Returns:
            User: haettu käyttäjä
            None: jos käyttäjää ei löydy
        """

        return self.user_repository.find_user(username)

    def add_sample_to_user(self, user, sample_id_raw):
        """Lisää käyttäjän listaukseen uuden näytetunnisteen

        Args:
            user (User): Käyttäjä, jolle näyte lisätään
            sample_id (str): Näytteen näytetunniste
        """
        sample_id = sample_id_raw.upper()
        self.user_repository.add_sample(user, sample_id)

    def get_all_users(self):
        """Hakee kaikki rekisteröidyt käyttäjät

        Returns:
            Lista: Käyttäjätunnukset
            Merkkijono: jos käyttäjiä ei ole rekisteröity
        """

        usernames = self.user_repository.get_usernames()
        if len(usernames) == 0:
            return "Ei vielä käyttäjiä."
        return usernames

    def get_number_of_samples(self, user):
        """Hakee käyttäjälle talletettujen näytteiden määrän

        Args:
            user (User): Käyttäjä, jonka näytteet halutaan hakea

        Returns:
            Kokonaisluku: Näytteiden määrä
        """

        samples = self.user_repository.get_sample_ids_by_user(user)
        return len(samples)

    def get_samples_by_user(self, user):
        """Hakee käyttäjälle talletetut näytteet

        Args:
            user (User): Käyttäjä, jonka näytteet halutaan hakea

        Returns:
            Lista: lista käyttäjän tallentamien näytteiden näytetunnisteista
        """

        sample_ids = self.user_repository.get_sample_ids_by_user(user)
        return sample_ids
