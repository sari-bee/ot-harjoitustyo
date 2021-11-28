from tkinter import ttk, StringVar
from services.sample_handler import SampleHandler


class UI:
    def __init__(self, window):
        self.window = window
        self.sample_id = None
        self.result = None
        self.comment_box = None
        self.input_sample_id = None
        self.input_anti_a = None
        self.input_anti_b = None
        self.input_anti_d = None
        self.input_control = None
        self.input_a1_cell = None
        self.input_b1_cell = None
        self.input_comment_box = None
        self.sample_handler = SampleHandler()

    def start(self):
        self.sample_id = StringVar()
        self.sample_id.set("Näytetunniste: ")
        self.result = StringVar()
        self.result.set("Tulkinta: ")
        self.comment_box = StringVar()
        self.comment_box.set("Kommentti: ")

        welcome = ttk.Label(
            master=self.window, text="Tervetuloa veriryhmäapuriin", font="Helvetica 18 bold")

        give_sample_id = ttk.Label(
            master=self.window, text="Anna näytetunniste:")
        self.input_sample_id = ttk.Entry(master=self.window)

        give_results = ttk.Label(
            master=self.window, text="Anna reaktiovoimakkuudet numeroilla 0-4 tai kaksoispopulaatio DP:")
        give_anti_a = ttk.Label(master=self.window, text="Anti-A")
        give_anti_b = ttk.Label(master=self.window, text="Anti-B")
        give_anti_d = ttk.Label(master=self.window, text="Anti-D")
        give_control = ttk.Label(master=self.window, text="Kontrolli")
        give_a1_cell = ttk.Label(master=self.window, text="A1-solu")
        give_b_cell = ttk.Label(master=self.window, text="B-solu")
        self.input_anti_a = ttk.Entry(master=self.window)
        self.input_anti_b = ttk.Entry(master=self.window)
        self.input_anti_d = ttk.Entry(master=self.window)
        self.input_control = ttk.Entry(master=self.window)
        self.input_a1_cell = ttk.Entry(master=self.window)
        self.input_b1_cell = ttk.Entry(master=self.window)

        give_comment = ttk.Label(master=self.window, text="Lisää kommentti:")
        self.input_comment_box = ttk.Entry(master=self.window)

        button_check = ttk.Button(
            master=self.window, text="Tarkista", command=self.check)
        button_empty = ttk.Button(
            master=self.window, text="Tyhjennä tiedot", command=self.delete)

        show_sample_id = ttk.Label(
            master=self.window, textvariable=self.sample_id)
        show_results = ttk.Label(master=self.window, textvariable=self.result)
        show_comments = ttk.Label(
            master=self.window, textvariable=self.comment_box)

        welcome.grid(row=0, column=0, columnspan=6, padx=5, pady=5)
        give_sample_id.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
        self.input_sample_id.grid(
            row=1, column=2, columnspan=3, padx=5, pady=5)
        give_results.grid(row=2, column=0, columnspan=6, padx=5, pady=5)
        give_anti_a.grid(row=3, column=0, padx=5, pady=5)
        give_anti_b.grid(row=3, column=2, padx=5, pady=5)
        give_anti_d.grid(row=3, column=4, padx=5, pady=5)
        give_control.grid(row=4, column=0, padx=5, pady=5)
        give_a1_cell.grid(row=4, column=2, padx=5, pady=5)
        give_b_cell.grid(row=4, column=4, padx=5, pady=5)
        self.input_anti_a.grid(row=3, column=1, padx=5, pady=5)
        self.input_anti_b.grid(row=3, column=3, padx=5, pady=5)
        self.input_anti_d.grid(row=3, column=5, padx=5, pady=5)
        self.input_control.grid(row=4, column=1, padx=5, pady=5)
        self.input_a1_cell.grid(row=4, column=3, padx=5, pady=5)
        self.input_b1_cell.grid(row=4, column=5, padx=5, pady=5)
        give_comment.grid(row=5, column=0, columnspan=3, padx=5, pady=5)
        self.input_comment_box.grid(
            row=5, column=2, columnspan=3, padx=5, pady=5)
        button_check.grid(row=6, column=0, columnspan=6, padx=5, pady=5)
        show_sample_id.grid(row=7, column=0, columnspan=6, padx=5, pady=5)
        show_results.grid(row=8, column=0, columnspan=6, padx=5, pady=5)
        show_comments.grid(row=9, column=0, columnspan=6, padx=5, pady=5)
        button_empty.grid(row=10, column=0, columnspan=6, padx=5, pady=5)

        self.window.grid_columnconfigure(0, minsize=10)
        self.window.grid_columnconfigure(1, minsize=10)
        self.window.grid_columnconfigure(2, minsize=10)
        self.window.grid_columnconfigure(3, minsize=10)
        self.window.grid_columnconfigure(4, minsize=10)
        self.window.grid_columnconfigure(5, minsize=10)

    def check(self):
        sample_id = self.input_sample_id.get()
        self.sample_handler.add_sample_id(sample_id)
        getid = self.sample_handler.get_sample_id()
        self.sample_id.set(f"Näytetunniste: {getid}")
        anti_a = self.input_anti_a.get()
        anti_b = self.input_anti_b.get()
        anti_d = self.input_anti_d.get()
        control = self.input_control.get()
        a1_cell = self.input_a1_cell.get()
        b_cell = self.input_b1_cell.get()
        self.sample_handler.add_reactions(
            anti_a, anti_b, anti_d, control, a1_cell, b_cell)
        result = self.sample_handler.get_results()
        self.result.set(f"Tulkinta: \n {result}")
        comment = self.input_comment_box.get()
        self.sample_handler.add_comment(comment)
        getcomment = self.sample_handler.get_comment()
        self.comment_box.set(f"Kommentti: \n {getcomment}")

    def delete(self):
        self.input_sample_id.delete(0, 'end')
        self.sample_id.set("Näytetunniste: ")
        self.input_anti_a.delete(0, 'end')
        self.input_anti_b.delete(0, 'end')
        self.input_anti_d.delete(0, 'end')
        self.input_control.delete(0, 'end')
        self.input_a1_cell.delete(0, 'end')
        self.input_b1_cell.delete(0, 'end')
        self.input_comment_box.delete(0, 'end')
        self.result.set("Tulkinta: ")
        self.comment_box.set("Kommentti: ")
