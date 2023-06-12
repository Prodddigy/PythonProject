from tkinter import *
import ButtonPack as bp
"""
This module is the main module of project it creates Root of TKinter 
and adds entry (Entry) to the root with memo_box(LabelFrame).
And after that it invokes methods from ButtonPack module that
fills the root with buttons and functionalities.


"""
if __name__ == "__main__":


    root = Tk()
    root['bg'] = 'grey'

    root.title("Best Calculator in the World!!!")

    # here I create entry for showing input and calculation and additionally we size it and choose its place
    entry = Entry(root, width=50, borderwidth=5)
    entry.config(state=DISABLED)
    entry.grid(row=0, column=0, columnspan=3, padx=15, pady=10)

    # memo_box will hold memory
    memo_box = LabelFrame(root, height=50, width=150, text="Here is your Memo", cursor="dot", bg = "grey")
    memo_box.config(font=("Courier", 10))
    memo_box.grid(row=0, column=4)

    # and at this point I fill the root with all necessary buttons
    bp.number_buttons(root, entry)
    bp.manipulation_utilities_buttons(root, entry)
    bp.basic_calculation_buttons(root, entry)
    bp.memory_management_buttons(root, memo_box, entry)
    bp.complex_calculation_buttons(root, entry)

    # here I make the calculator non-resizeable
    root.resizable(height=False, width=False)
    root.mainloop()
