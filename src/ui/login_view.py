from tkinter import ttk, StringVar
from emoji import emojize


class LoginView:
    """Luokka luo kirjautumisnäkymän, jossa voi kirjautua sisään tai rekisteröityä.
    """

    def __init__(self, window, to_sample_view, user_handler):
        """Luokan konstruktori, joka luo näkymän.

        Args:
            window (window): ikkuna, johon näkymä luodaan
            to_sample_view: UI-luokan metodi, joka avaa näytenäkymän
            user_handler ([UserHandler): käynnistyskerran käyttäjäservice
        """

        self.__window = window
        self.__frame = None
        self.__to_sample_view = to_sample_view
        self.__user_handler = user_handler
        self.__input_username = None
        self.__input_new_username = None
        self.__login_button = None
        self.__add_new_user_button = None
        self.__message = None
        self.initialize()

    def grid(self):
        self.__frame.grid()

    def initialize(self):
        self.__frame = ttk.Frame(master=self.__window)
        self.__message = StringVar()
        self.__message.set("")

        welcome = ttk.Label(master=self.__window,
                            text=(
                                emojize(":red_circle: Tervetuloa veriryhmäapuriin :red_circle:")),
                            font="Helvetica 18 bold")

        give_username = ttk.Label(
            master=self.__window, text="Syötä käyttäjätunnus:")
        self.__input_username = ttk.Entry(master=self.__window)
        self.__login_button = ttk.Button(
            master=self.__window, text="Kirjaudu sisään", command=self.sample_view)

        give_new_username = ttk.Label(
            master=self.__window, text="Lisää uusi käyttäjätunnus:")
        self.__input_new_username = ttk.Entry(master=self.__window)
        self.__add_new_user_button = ttk.Button(
            master=self.__window, text="Lisää!", command=self.add_new_user)
        show_message = ttk.Label(master=self.__window,
                                 textvariable=self.__message)

        welcome.grid(row=0, column=0, columnspan=6, padx=5, pady=5)
        give_username.grid(row=1, column=0, columnspan=2, padx=5, pady=5)
        self.__input_username.grid(
            row=1, column=2, columnspan=2, padx=5, pady=5)
        self.__login_button.grid(row=1, column=4, columnspan=2, padx=5, pady=5)
        give_new_username.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
        self.__input_new_username.grid(
            row=2, column=2, columnspan=2, padx=5, pady=5)
        self.__add_new_user_button.grid(
            row=2, column=4, columnspan=2, padx=5, pady=5)
        show_message.grid(row=3, column=0, columnspan=6, padx=5, pady=5)

    def sample_view(self):
        """
        Sisäänkirjautumismetodi; joko käyttäjälle ilmoitetaan, että käyttäjätunnusta ei löydy,
        tai sitten kirjautumisikkuna inaktivoidaan ja näyteikkuna avataan.
        """

        username = None
        username = self.__input_username.get()
        user = self.__user_handler.find_user_by_username(username)

        if user is None:
            self.__message.set(
                f"Käyttäjää {username} ei löydy. Rekisteröi tarvittaessa uusi käyttäjätunnus.")

        else:
            self.__input_username.config(state="disabled")
            self.__input_new_username.config(state="disabled")
            self.__add_new_user_button.config(state="disabled")
            self.__login_button.config(state="disabled")

            self.__to_sample_view(user)

    def add_new_user(self):
        """Uuden käyttäjätunnuksen rekisteröiminen tai tieto, että käyttäjätunnus on käytössä.
        """

        username = None
        username = self.__input_new_username.get()
        if len(username) < 3:
            self.__message.set(
                "Käyttäjätunnuksen tulee olla vähintään kolme merkkiä pitkä.")
        else:
            result = self.__user_handler.add_new_user(username)

            if result is None:
                self.__message.set(
                    f"Käyttäjätunnus {username} on jo käytössä. Valitse toinen käyttäjätunnus.")

            else:
                self.__message.set(
                    f"Käyttäjätunnus {username} on nyt rekisteröity. Voit kirjautua sisään.")
