from tkinter import ttk, StringVar


class HistoryView:
    def __init__(self, window, sample_handler):
        self.window = window
        self.frame = None
        self.sample_handler = sample_handler
        self.input_sample_id = None
        self.sample_index = 0
        self.initialize()

    def grid(self):
        self.frame.grid()

    def initialize(self):
        self.frame = ttk.Frame(master=self.window)
        self.search_results = StringVar()
        self.search_results.set("")

        search_results = ttk.Label(master=self.window,
                                   textvariable=self.search_results)
        history_button = ttk.Button(
            master=self.window, text="Selaa näytteitä", command=self.get_sample_history)
        self.input_sample_id = ttk.Entry(master=self.window)
        search_by_id_button = ttk.Button(
            master=self.window, text="Etsi näytetunnisteella", command=self.search_by_id)
        later_button = ttk.Button(
            master=self.window, text="Myöhemmät näytteet", command=self.get_later)
        earlier_button = ttk.Button(
            master=self.window, text="Aiemmat näytteet", command=self.get_earlier)

        self.input_sample_id.grid(
            row=0, column=0, columnspan=5, padx=5, pady=5)
        search_by_id_button.grid(row=0, column=5, columnspan=3, padx=5, pady=5)
        history_button.grid(row=0, column=8, columnspan=3, padx=5, pady=5)
        search_results.grid(row=1, column=0, columnspan=10, padx=5, pady=5)
        earlier_button.grid(row=2, column=0, columnspan=3, padx=5, pady=5)
        later_button.grid(row=2, column=8, columnspan=3, padx=5, pady=5)

    def get_sample_history(self):
        self.search_results.set(
            self.sample_handler.get_all_samples(self.sample_index))

    def get_later(self):
        if self.sample_index >= 4:
            self.sample_index = self.sample_index - 5
        self.get_sample_history()

    def get_earlier(self):
        number = self.sample_handler.get_number_of_samples()
        if self.sample_index <= (number - 5):
            self.sample_index = self.sample_index + 5
        self.get_sample_history()

    def search_by_id(self):
        sample_id = None
        sample_id = self.input_sample_id.get()
        if len(sample_id) == 0:
            self.search_results.set("Syötä näytetunniste")
        else:
            self.search_results.set(
                self.sample_handler.get_sample_by_id(sample_id))
            self.input_sample_id.delete(0, 'end')
