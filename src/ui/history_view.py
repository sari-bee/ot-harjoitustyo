from tkinter import ttk, StringVar


class HistoryView:
    def __init__(self, window, sample_handler, user_handler, user):
        self.__window = window
        self.__frame = None
        self.__sample_handler = sample_handler
        self.__user_handler = user_handler
        self.__user = user
        self.__input_sample_id = None
        self.__sample_index = 0
        self.__search = 0
        self.__earlier_button = None
        self.__later_button = None
        self.initialize()

    def grid(self):
        self.__frame.grid()

    def initialize(self):
        self.__frame = ttk.Frame(master=self.__window)
        self.__search_results = StringVar()
        self.__search_results.set("")

        search_results = ttk.Label(master=self.__window,
                                   textvariable=self.__search_results)
        history_button = ttk.Button(
            master=self.__window, text="Selaa kaikkia näytteitä", command=self.click_sample_history)
        user_history_button = ttk.Button(
            master=self.__window, text="Tallettamasi näytteet", command=self.click_user_history)
        self.__input_sample_id = ttk.Entry(master=self.__window)
        search_by_id_button = ttk.Button(
            master=self.__window, text="Etsi näytetunnisteella", command=self.search_by_id)
        self.__later_button = ttk.Button(
            master=self.__window, text="Myöhemmät näytteet", command=self.get_later)
        self.__earlier_button = ttk.Button(
            master=self.__window, text="Aiemmat näytteet", command=self.get_earlier)

        self.__input_sample_id.grid(
            row=0, column=0, columnspan=3, padx=5, pady=5)
        search_by_id_button.grid(row=0, column=3, columnspan=3, padx=5, pady=5)
        user_history_button.grid(row=0, column=6, columnspan=2, padx=5, pady=5)
        history_button.grid(row=0, column=8, columnspan=2, padx=5, pady=5)
        search_results.grid(row=1, column=0, columnspan=10, padx=5, pady=5)
        self.__earlier_button.grid(
            row=2, column=0, columnspan=3, padx=5, pady=5)
        self.__later_button.grid(row=2, column=8, columnspan=3, padx=5, pady=5)

    def click_sample_history(self):
        self.__sample_index = 0
        self.__search = 1
        self.get_sample_history(self.__sample_index)

    def click_user_history(self):
        self.__sample_index = 0
        self.__search = 2
        self.get_user_history(self.__sample_index)

    def get_sample_history(self, index):
        if self.__sample_index < 4:
            self.__later_button.config(state="disabled")
        else:
            self.__later_button.config(state="enabled")
        number = self.__sample_handler.get_number_of_samples()
        if self.__sample_index > (number - 5):
            self.__earlier_button.config(state="disabled")
        else:
            self.__earlier_button.config(state="enabled")
        self.__search_results.set(
            self.__sample_handler.get_all_samples(index))

    def get_user_history(self, index):
        if self.__sample_index < 4:
            self.__later_button.config(state="disabled")
        else:
            self.__later_button.config(state="enabled")
        number = self.__user_handler.get_number_of_samples(self.__user)
        if self.__sample_index > (number - 5):
            self.__earlier_button.config(state="disabled")
        else:
            self.__earlier_button.config(state="enabled")
        sample_ids = self.__user_handler.get_samples_by_user(self.__user)
        if len(sample_ids) == 0:
            self.__search_results.set(
                "Käyttäjällä ei ole talletettuja näytteitä")
        else:
            self.__search_results.set(
                self.__sample_handler.get_samples_by_several_ids(sample_ids, index))

    def get_later(self):
        if self.__search == 0:
            self.__search_results.set("Valitse ensin haku")
        else:
            if self.__sample_index >= 4:
                self.__sample_index = self.__sample_index - 5
            if self.__search == 2:
                self.get_user_history(self.__sample_index)
            else:
                self.get_sample_history(self.__sample_index)

    def get_earlier(self):
        if self.__search == 0:
            self.__search_results.set("Valitse ensin haku")
        else:
            if self.__search == 2:
                number = self.__user_handler.get_number_of_samples(self.__user)
            else:
                number = self.__sample_handler.get_number_of_samples()
            if self.__sample_index <= (number - 5):
                self.__sample_index = self.__sample_index + 5
            if self.__search == 2:
                self.get_user_history(self.__sample_index)
            else:
                self.get_sample_history(self.__sample_index)

    def search_by_id(self):
        self.__search = 0
        sample_id = None
        sample_id = self.__input_sample_id.get()
        if len(sample_id) == 0:
            self.__search_results.set("Syötä näytetunniste")
        else:
            self.__search_results.set(
                self.__sample_handler.get_sample_by_id(sample_id))
            self.__input_sample_id.delete(0, 'end')
