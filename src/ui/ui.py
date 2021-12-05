from tkinter import Toplevel
from ui.sample_view import SampleView
from ui.history_view import HistoryView
from services.sample_handler import SampleHandler


class UI:

    def __init__(self, window):
        self.window = window
        self.current_view = None
        self.sample_handler = SampleHandler()

    def start(self):
        self.current_view = SampleView(
            self.window, self.to_history, self.sample_handler)
        self.current_view.grid()

    def to_history(self):
        history_window = Toplevel(self.window)
        history_window.title("Näytehistoria")
        self.current_view = HistoryView(history_window, self.sample_handler)
        self.current_view.grid()
