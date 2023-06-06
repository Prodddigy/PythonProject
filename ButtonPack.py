from tkinter import END, Button
import ButtonListener as bl

def number_buttons(root,entry):
    button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: bl.button_click(1,entry))
    button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: bl.button_click(2,entry))
    button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: bl.button_click(3,entry))
    button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: bl.button_click(4,entry))
    button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: bl.button_click(5,entry))
    button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: bl.button_click(6,entry))
    button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: bl.button_click(7,entry))
    button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: bl.button_click(8,entry))
    button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: bl.button_click(9,entry))
    button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: bl.button_click(0,entry))
    button_dot = Button(root, text=".", padx=40, pady=20, command=lambda: bl.button_click(".", entry))

    button_1.grid(row=3, column=0)
    button_2.grid(row=3, column=1)
    button_3.grid(row=3, column=2)
    button_4.grid(row=2, column=0)
    button_5.grid(row=2, column=1)
    button_6.grid(row=2, column=2)
    button_7.grid(row=1, column=0)
    button_8.grid(row=1, column=1)
    button_9.grid(row=1, column=2)
    button_0.grid(row=4, column=1)
    button_dot.grid(row=4, column=2)


def basic_calculation_buttons(root, entry):
    button_addition = Button(root, text="+", padx=39, pady=20)
    return
def mainpulation_utilities_buttons(root, entry):

    button_negate = Button(root, text="¬", padx=40, pady=20, command=lambda: bl.button_negate(entry))

    button_clear = Button(root, text="WYCZYŚĆ", padx=75, pady=20,command=lambda: bl.button_clear(entry) )

    button_negate.grid(row=4, column=0)

    button_clear.grid(row=4, column=1, columnspan=2)
