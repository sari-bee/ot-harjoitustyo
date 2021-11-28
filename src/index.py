from tkinter import Tk
from ui.ui import UI

window = Tk()
window.title("Veriryhmäapuri")
ui = UI(window)
ui.start()
window.mainloop()
