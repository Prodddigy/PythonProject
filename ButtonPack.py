from tkinter import END, Button
import ButtonListener as bl


def number_buttons(root, entry):
    #może zrób w pętli jak się da
    button_1 = Button(root, text="1", padx=50, pady=20, command=lambda: bl.button_number_choice(1, entry))
    button_2 = Button(root, text="2", padx=50, pady=20, command=lambda: bl.button_number_choice(2, entry))
    button_3 = Button(root, text="3", padx=50, pady=20, command=lambda: bl.button_number_choice(3, entry))
    button_4 = Button(root, text="4", padx=50, pady=20, command=lambda: bl.button_number_choice(4, entry))
    button_5 = Button(root, text="5", padx=50, pady=20, command=lambda: bl.button_number_choice(5, entry))
    button_6 = Button(root, text="6", padx=50, pady=20, command=lambda: bl.button_number_choice(6, entry))
    button_7 = Button(root, text="7", padx=50, pady=20, command=lambda: bl.button_number_choice(7, entry))
    button_8 = Button(root, text="8", padx=50, pady=20, command=lambda: bl.button_number_choice(8, entry))
    button_9 = Button(root, text="9", padx=50, pady=20, command=lambda: bl.button_number_choice(9, entry))
    button_0 = Button(root, text="0", padx=50, pady=20, command=lambda: bl.button_number_choice(0, entry))
    button_dot = Button(root, text=".", padx=51, pady=20, command=lambda: bl.button_number_choice(".", entry))

    button_1.grid(row=4, column=0)
    button_2.grid(row=4, column=1)
    button_3.grid(row=4, column=2)
    button_4.grid(row=3, column=0)
    button_5.grid(row=3, column=1)
    button_6.grid(row=3, column=2)
    button_7.grid(row=2, column=0)
    button_8.grid(row=2, column=1)
    button_9.grid(row=2, column=2)
    button_0.grid(row=5, column=1)
    button_dot.grid(row=5, column=2)


def basic_calculation_buttons(root, entry):
    button_addition = Button(root, text="+", padx=69, pady=20, command=lambda: bl.button_add(entry))
    button_subtraction = Button(root, text="-", padx=69, pady=20, command=lambda: bl.button_subtract(entry))
    button_multiplication = Button(root, text="*", padx=69, pady=20, command=lambda: bl.button_multiply(entry))

    button_equal = Button(root, text="=", padx=69, pady=20, command=lambda: bl.button_equal(entry))

    button_addition.grid(row=4, column=4)
    button_subtraction.grid(row=3, column=4)
    button_multiplication.grid(row=2, column=4)

    button_equal.grid(row=5, column=4)


def manipulation_utilities_buttons(root, entry):
    button_negate = Button(root, text="¬", padx=50, pady=20, command=lambda: bl.button_negate(entry))

    button_clear = Button(root, text="C", padx=40, pady=20, command=lambda: bl.button_clear(entry))

    button_erase = Button(root, text="<x", padx=40, pady=20, command=lambda: bl.button_erase(entry))

    button_erase.grid(row=1, column=2)

    button_negate.grid(row=5, column=0)

    button_clear.grid(row=1, column=1)


def memory_managment_buttons():
    return
