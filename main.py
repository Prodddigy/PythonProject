from tkinter import *
from tkinter import messagebox
import ButtonPack as bp

global entry

if __name__ == "__main__":
    global root

    root = Tk()

    root.title("Najlepszy Kalkulator na świecie!")

    entry = Entry(root, width=50, borderwidth=5)

    entry.grid(row=0, column=0, columnspan=3, padx=15, pady=10)
    memo_box = LabelFrame(root, height=50, width=150, text="Here is your Memo", cursor="dot")
    memo_box.config(font=("Courier", 10))
    memo_box.grid(row=0, column=4)

    bp.number_buttons(root, entry)
    bp.manipulation_utilities_buttons(root, entry)
    bp.basic_calculation_buttons(root, entry)
    bp.memory_management_buttons(root, memo_box, entry)
    bp.complex_calculation_buttons(root, entry)

    root.resizable(height=False, width=False)
    root.mainloop()
