from pathlib import Path
from entities.user import User


class UserRepository:

    """Luokka, joka huolehtii käyttäjäolioiden tallentamisesta ja lukemisesta csv-tiedostoon.

    Attributes:
        path: Polku konekohtaiseen csv-tiedostoon.
    """

    def __init__(self, path):
        """Luokan konstruktori, joka luo ohjelman käynnistyskertakohtaisen käyttäjärepositoryn.

        Args:
            path (str): Polku konekohtaiseen csv-tiedostoon.
        """

        self.__path = path

    def read(self):
        """Metodi lukee talletettujen käyttäjien tiedot csv-tiedostosta ja muuntaa ne listaksi.

        Returns:
            Lista: Tallennetut käyttäjäoliot
        """

        users = []
        Path(self.__path).touch()

        with open(self.__path) as file:
            for row in file:
                if row == "":
                    pass
                if row == "\n":
                    pass
                row = row.replace("\n", "")
                split = row.split(";")
                if len(split) == 0:
                    pass
                else:
                    username = split[0]
                    sample_ids = []
                    i = 1
                    while i < len(split):
                        sample_ids.append(split[i])
                        i = i+1
                    user = User(username, sample_ids)
                    users.append(user)

        return users

    def write(self, users):
        """Metodi tallentaa käyttäjäoliot csv-tiedostoon.

        Args:
            users (list): Lista käyttäjäolioita
        """

        Path(self.__path).touch()

        with open(self.__path, "w") as file:
            for user in users:
                row = user.username
                for sample_id in user.sample_ids:
                    row = row + ";" + str(sample_id)
                row = row + "\n"
                file.write(row)

    def add_user(self, new_user):
        """Lisää uuden käyttäjäolion tallennettujen käyttäjien tiedostoon.

        Args:
            new_user (User): Käyttäjäolio

        Returns:
            False: jos lisättävän käyttäjän käyttäjätunnus löytyy jo käyttäjien listalta
            True: jos käyttäjän lisäys onnistui (eli käyttäjätunnus oli uniikki)
        """

        users = self.read()

        for user in users:
            if user.username == new_user.username:
                return False

        users.append(new_user)
        self.write(users)
        return True

    def find_user(self, username):
        """Noutaa käyttäjäolion käyttäjätunnuksen perusteella

        Args:
           username (str): Halutun käyttäjän käyttäjätunnus

        Returns:
            User: Haluttu käyttäjäolio
            None: jos etsittävää käyttäjätunnusta ei löydy
        """

        users = self.read()

        for user in users:
            if user.username == username:
                return user

        return None

    def add_sample(self, user: User, added_sample_id):
        """Lisää näytetunnisteen käyttäjän näytetunnistelistaan

        Args:
            user (User): Käyttäjä, jolle näytetunniste lisätään
            added_sample_id (str): Näytetunniste, joka halutaan lisätä käyttäjän listaan
        """

        users = self.read()
        i = 0

        while i < len(users):
            if users[i].username == user.username:
                right_user = users[i]
                break
            i = i+1

        right_user.add_sample_id(added_sample_id)
        users[i] = right_user
        self.write(users)

    def get_usernames(self):
        """Hakee kaikki rekisteröidyt käyttäjät

        Returns:
            Lista: käyttäjätunnukset
        """

        users = self.read()
        usernames = []

        for user in users:
            usernames.append(user.username)

        return usernames

    def get_sample_ids_by_user(self, wanted_user):
        """Hakee kaikki käyttäjälle tallennetut näytetunnisteet

        Args:
            wanted_user (User): Käyttäjä, jonka näytetunnisteet halutaan hakea

        Returns:
            Lista: lista käyttäjän tallentamien näytteiden näytetunnisteista
            None: jos käyttäjää ei löydy
        """

        users = self.read()

        for user in users:
            if user.username == wanted_user.username:
                return user.sample_ids

        return None
