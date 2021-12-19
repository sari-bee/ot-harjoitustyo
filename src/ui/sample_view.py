from tkinter import ttk, StringVar
from services.sample_handler import SampleHandler


class SampleView:
    """Luokka luo näytenäkymän, jossa voi syöttää näytteen tiedot ja saada tulkinnan.
    """

    def __init__(self, window, to_history, sample_handler, user_handler, user):
        """Luokan konstruktori, joka luo näkymän.

        Args:
            window (window): ikkuna, johon näkymä luodaan
            to_history: UI-luokan metodi, joka avaa historianäkymän
            sample_handler (SampleHandler): käynnistyskerran näyteservice
            user_handler (UserHandler): käynnistyskerran käyttäjäservice
            user (User): käynnistyskerran sisäänkirjautunut käyttäjä
        """

        self.__window = window
        self.__frame = None
        self.__to_history = to_history
        self.__sample_id = None
        self.__result = None
        self.__comment_box = None
        self.__input_sample_id = None
        self.__input_anti_a = None
        self.__input_anti_b = None
        self.__input_anti_d = None
        self.__input_control = None
        self.__input_a1_cell = None
        self.__input_b_cell = None
        self.__input_comment_box = None
        self.__sample_handler = sample_handler
        self.__user_handler = user_handler
        self.__user = user
        self.initialize()

    def grid(self):
        self.__frame.grid()

    def initialize(self):
        self.__frame = ttk.Frame(master=self.__window)
        self.__sample_id = StringVar()
        self.__sample_id.set("")
        self.__result = StringVar()
        self.__result.set("")
        self.__comment_box = StringVar()
        self.__comment_box.set("")

        welcome = ttk.Label(
            master=self.__window, text="Veriryhmäapuri",
            font="Helvetica 18 bold")

        give_sample_id = ttk.Label(
            master=self.__window, text="Anna näytetunniste:")
        self.__input_sample_id = ttk.Entry(master=self.__window)

        give_results = ttk.Label(
            master=self.__window, text="Anna reaktiovoimakkuudet 0-4 tai kaksoispopulaatio DP:")
        give_anti_a = ttk.Label(master=self.__window, text="Anti-A")
        give_anti_b = ttk.Label(master=self.__window, text="Anti-B")
        give_anti_d = ttk.Label(master=self.__window, text="Anti-D")
        give_control = ttk.Label(master=self.__window, text="Kontrolli")
        give_a1_cell = ttk.Label(master=self.__window, text="A1-solu")
        give_b_cell = ttk.Label(master=self.__window, text="B-solu")
        self.__input_anti_a = ttk.Entry(master=self.__window)
        self.__input_anti_b = ttk.Entry(master=self.__window)
        self.__input_anti_d = ttk.Entry(master=self.__window)
        self.__input_control = ttk.Entry(master=self.__window)
        self.__input_a1_cell = ttk.Entry(master=self.__window)
        self.__input_b_cell = ttk.Entry(master=self.__window)

        give_comment = ttk.Label(master=self.__window, text="Lisää kommentti:")
        self.__input_comment_box = ttk.Entry(master=self.__window)

        button_check = ttk.Button(
            master=self.__window, text="Tarkista", command=self.check)
        button_empty = ttk.Button(
            master=self.__window, text="Tyhjennä kentät", command=self.delete)
        button_history = ttk.Button(
            master=self.__window, text="Näytehistoria", command=self.history)

        show_sample_id = ttk.Label(
            master=self.__window, textvariable=self.__sample_id)
        show_results = ttk.Label(master=self.__window,
                                 textvariable=self.__result)
        show_comments = ttk.Label(
            master=self.__window, textvariable=self.__comment_box)

        welcome.grid(row=0, column=0, columnspan=6, padx=5, pady=5)
        give_sample_id.grid(row=1, column=1, columnspan=2, padx=5, pady=5)
        self.__input_sample_id.grid(
            row=1, column=2, columnspan=2, padx=5, pady=5)
        give_results.grid(row=2, column=0, columnspan=6, padx=5, pady=5)
        give_anti_a.grid(row=3, column=0, padx=5, pady=5)
        give_anti_b.grid(row=3, column=2, padx=5, pady=5)
        give_anti_d.grid(row=3, column=4, padx=5, pady=5)
        give_control.grid(row=4, column=0, padx=5, pady=5)
        give_a1_cell.grid(row=4, column=2, padx=5, pady=5)
        give_b_cell.grid(row=4, column=4, padx=5, pady=5)
        self.__input_anti_a.grid(row=3, column=1, padx=5, pady=5)
        self.__input_anti_b.grid(row=3, column=3, padx=5, pady=5)
        self.__input_anti_d.grid(row=3, column=5, padx=5, pady=5)
        self.__input_control.grid(row=4, column=1, padx=5, pady=5)
        self.__input_a1_cell.grid(row=4, column=3, padx=5, pady=5)
        self.__input_b_cell.grid(row=4, column=5, padx=5, pady=5)
        give_comment.grid(row=5, column=0, columnspan=3, padx=5, pady=5)
        self.__input_comment_box.grid(
            row=5, column=2, columnspan=3, padx=5, pady=5)
        button_check.grid(row=6, column=0, columnspan=6, padx=5, pady=5)
        button_empty.grid(row=7, column=0, columnspan=6, padx=5, pady=5)
        show_sample_id.grid(row=8, column=0, columnspan=6, padx=5, pady=5)
        show_results.grid(row=9, column=0, columnspan=6, padx=5, pady=5)
        show_comments.grid(row=10, column=0, columnspan=6, padx=5, pady=5)
        button_history.grid(row=11, column=0, columnspan=6, padx=5, pady=5)

    def check(self):
        """
        Haetaan käyttäjän syöttämät tiedot käyttöliittymästä.
        Tarkistetaan, ovatko kaikki pakolliset kentät täytettyjä.
        Tarkistetaan, ovatko syötteet valideja.
        Tarkistetaan, onko käyttäjän syöttämä näytetunniste jo käytössä.
        Talletetaan näytteen tiedot näyte- ja käyttäjätiedostoihin.
        Annetaan tulkinta.
        """

        sample_id = None
        comment = None
        anti_a = None
        anti_b = None
        anti_d = None
        control = None
        a1_cell = None
        b_cell = None

        sample_id = self.__input_sample_id.get()
        comment = self.__input_comment_box.get()
        anti_a = self.__input_anti_a.get()
        anti_b = self.__input_anti_b.get()
        anti_d = self.__input_anti_d.get()
        control = self.__input_control.get()
        a1_cell = self.__input_a1_cell.get()
        b_cell = self.__input_b_cell.get()

        if len(sample_id) == 0:
            self.__sample_id.set("Näytetunniste on pakollinen tieto!")
            self.__result.set("")
            self.__comment_box.set("")
        elif len(anti_a) == 0 or len(anti_b) == 0 or len(anti_d) == 0:
            self.__result.set("Jokin reaktiovoimakkuus puuttuu!")
            self.__sample_id.set("")
            self.__comment_box.set("")
        elif len(control) == 0 or len(a1_cell) == 0 or len(b_cell) == 0:
            self.__result.set("Jokin reaktiovoimakkuus puuttuu!")
            self.__sample_id.set("")
            self.__comment_box.set("")

        elif SampleHandler.check_input(anti_a, anti_b, anti_d, control, a1_cell, b_cell) is True:
            if len(comment) == 0:
                comment = "-"
            if not self.__sample_handler.add_sample_data(
                    sample_id, comment, anti_a, anti_b, anti_d, control, a1_cell, b_cell):
                self.__sample_id.set(
                    "Syötit näytetunnisteen, joka on jo käytössä.")
                self.__result.set("")
                self.__comment_box.set("")
            else:
                self.__user_handler.add_sample_to_user(self.__user, sample_id)
                result = self.__sample_handler.get_results(sample_id.upper())
                self.__sample_id.set(f"Näytetunniste: {sample_id.upper()}")
                self.__comment_box.set(f"Kommentti: {comment}")
                self.__result.set(f"Tulkinta: {result}")

        else:
            problem = SampleHandler.check_input(
                anti_a, anti_b, anti_d, control, a1_cell, b_cell)
            self.__result.set(
                f"Syötit virheellisen reaktiovoimakkuuden seuraavissa kentissä:\n{problem}")
            self.__sample_id.set("")
            self.__comment_box.set("")

    def delete(self):
        """Kenttien tyhjennys.
        """

        self.__input_sample_id.delete(0, 'end')
        self.__sample_id.set("")
        self.__input_anti_a.delete(0, 'end')
        self.__input_anti_b.delete(0, 'end')
        self.__input_anti_d.delete(0, 'end')
        self.__input_control.delete(0, 'end')
        self.__input_a1_cell.delete(0, 'end')
        self.__input_b_cell.delete(0, 'end')
        self.__input_comment_box.delete(0, 'end')
        self.__result.set("")
        self.__comment_box.set("")

    def history(self):
        """Siirtyminen historiaikkunaan.
        """

        self.__to_history(self.__user)
