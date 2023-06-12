from tkinter import Button, Frame, Label
import ButtonListener as bl
import MemoryManipulation as mm

"""
This module provides a set of functions used for creation of buttons that fill the calculator 

Functions:
    number_buttons -- Adds buttons 0-9 and a dot "." to the root
    basic_calculation_buttons -- Adds buttons to the root: +,-,*,/,=; for addition, subtraction,multiplication,division and  equation sign 
    manipulation_utilities_buttons -- Adds buttons to the root for simple manipulation of contents of entry like:¬,C,<x; for
                                        negation, clearing whole entry, backspace clearing digit by digit 
    memory_management_buttons -- Adds buttons to the root: M+,M-,MR,MC; for addition to memory, subtraction from memory,
                                    reading from memory, clearing the memory
    complex_calculation_buttons -- Adds buttons to the root which manipulates the entry in more complex ways:
                                    x²,√,x!,%: for calculating power of 2 of entry number, square roof of entry number,
                                    factorial of entry number, creates a percentage of an entry number
                                    Additionally adds i button that shows instructions for calculator.
"""


def number_buttons(root, entry):
    """
            Adds buttons 0-9 and a dot "." to the root

            Args:
                root (TK) : is the window for putting in buttons and other functionalities'
                entry (Entry): Entry which holds calculations done by user

            Returns:
                void
            """
    button_1 = Button(root, text="1", padx=50, pady=20, command=lambda: bl.button_number_choice(1, entry), bg="grey", fg = "white",font=15)
    button_2 = Button(root, text="2", padx=50, pady=20, command=lambda: bl.button_number_choice(2, entry), bg="grey", fg = "white",font=15)
    button_3 = Button(root, text="3", padx=50, pady=20, command=lambda: bl.button_number_choice(3, entry), bg="grey", fg = "white",font=15)
    button_4 = Button(root, text="4", padx=50, pady=20, command=lambda: bl.button_number_choice(4, entry), bg="grey", fg = "white",font=15)
    button_5 = Button(root, text="5", padx=50, pady=20, command=lambda: bl.button_number_choice(5, entry), bg="grey", fg = "white",font=15)
    button_6 = Button(root, text="6", padx=50, pady=20, command=lambda: bl.button_number_choice(6, entry), bg="grey", fg = "white",font=15)
    button_7 = Button(root, text="7", padx=50, pady=20, command=lambda: bl.button_number_choice(7, entry), bg="grey", fg = "white",font=15)
    button_8 = Button(root, text="8", padx=50, pady=20, command=lambda: bl.button_number_choice(8, entry), bg="grey", fg = "white",font=15)
    button_9 = Button(root, text="9", padx=50, pady=20, command=lambda: bl.button_number_choice(9, entry), bg="grey", fg = "white",font=15)
    button_0 = Button(root, text="0", padx=50, pady=20, command=lambda: bl.button_number_choice(0, entry), bg="grey", fg = "white",font=15)
    button_dot = Button(root, text=".", padx=51, pady=20, command=lambda: bl.button_number_choice(".", entry), bg="grey", fg = "white",font=15)

    button_1.grid(row=5, column=0)
    button_2.grid(row=5, column=1)
    button_3.grid(row=5, column=2)
    button_4.grid(row=4, column=0)
    button_5.grid(row=4, column=1)
    button_6.grid(row=4, column=2)
    button_7.grid(row=3, column=0)
    button_8.grid(row=3, column=1)
    button_9.grid(row=3, column=2)
    button_0.grid(row=6, column=1)
    button_dot.grid(row=6, column=2)


def basic_calculation_buttons(root, entry):
    """
                Adds buttons to the root: +,-,*,/,=; for addition, subtraction,multiplication,division and  equation sign

                Args:
                    root (TK) : is the window for putting in buttons and other functionalities'
                    entry (Entry): Entry which holds calculations done by user

                Returns:
                    void
                """
    button_addition = Button(root, text="+", font="Times 12", padx=68, pady=20, command=lambda: bl.button_add(entry), bg ="#88e0dd")
    button_subtraction = Button(root, text="-", font="Times 12", padx=70, pady=20,
                                command=lambda: bl.button_subtract(entry), bg ="#88e0dd")
    button_multiplication = Button(root, text="*", font="Times 12", padx=69, pady=20,
                                   command=lambda: bl.button_multiply(entry), bg ="#88e0dd")
    button_division = Button(root, text="/", font="Times 12", padx=71, pady=20, command=lambda: bl.button_divide(entry), bg ="#88e0dd")

    button_equal = Button(root, text="=", font="Times 12", padx=70, pady=20, command=lambda: bl.button_equal(entry),bg="#1d7720")

    button_addition.grid(row=5, column=4)
    button_subtraction.grid(row=4, column=4)
    button_multiplication.grid(row=3, column=4)
    button_division.grid(row=2, column=4)

    button_equal.grid(row=6, column=4)


def manipulation_utilities_buttons(root, entry):
    """
                    Adds buttons to the root for simple manipulation of contents of entry like:¬,C,<x; for
                                        negation, clearing whole entry, backspace clearing digit by digit

                    Args:
                        root (TK) : is the window for putting in buttons and other functionalities'
                        entry (Entry): Entry which holds calculations done by user

                    Returns:
                        void
                    """
    clean_frame = Frame(root)
    button_negate = Button(root, text="¬", padx=50, pady=20, command=lambda: bl.button_negate(entry), bg="grey")

    button_clear = Button(clean_frame, text="C", padx=21, pady=13, command=lambda: bl.button_clear(entry), bg="red")

    button_erase = Button(clean_frame, text="<x", padx=17, pady=13, command=lambda: bl.button_erase(entry), bg="orange")

    clean_frame.grid(row=1, column=2)

    button_erase.grid(row=1, column=2)

    button_negate.grid(row=6, column=0)

    button_clear.grid(row=1, column=1)


def memory_management_buttons(root, memo_box, entry):
    """
                        Adds buttons to the root: M+,M-,MR,MC; for addition to memory, subtraction from memory,
                                    reading from memory, clearing the memory

                        Args:
                            root (TK) : is the window for putting in buttons and other functionalities'
                            memo_box (LabelFrame) : is the box which holds memory value
                            entry (Entry): Entry which holds calculations done by user

                        Returns:
                            void
                        """
    memo_frame = Frame(root)
    memo_mrc_frame = Frame(root)
    memo_content = Label(memo_box, text="0")

    button_memo_plus = Button(memo_frame, text="M+", padx=15, pady=13,
                              command=lambda: mm.memory_addition(memo_content, entry),bg ="#e572cc")
    button_memo_minus = Button(memo_frame, text="M-", padx=15, pady=13,
                               command=lambda: mm.memory_subtraction(memo_content, entry),bg ="#e572cc")
    button_mr = Button(memo_mrc_frame, text="MR", padx=15, pady=13, command=lambda: mm.memory_read(memo_content, entry),bg ="#e572cc")
    button_mc = Button(memo_mrc_frame, text="MC", padx=15, pady=13, command=lambda: mm.memory_clean(memo_content),bg ="#e572cc")

    memo_content.pack()

    memo_mrc_frame.grid(row=1, column=1)
    memo_frame.grid(row=1, column=0)

    button_mr.pack(side="right")
    button_mc.pack(side="left")

    button_memo_plus.pack(side="left")
    button_memo_minus.pack(side="right")


def complex_calculation_buttons(root, entry):
    """
                            Adds buttons to the root which manipulates the entry in more complex ways:
                                    x²,√,x!,%,⅟: for calculating power of 2 of entry number, square roof of entry number,
                                    factorial of entry number, creates a percentage of an entry number, divide 1 by entry number.
                                    Additionally, adds "i" button that shows instructions for calculator.
                                    "i" button is put here for the design purposes and does not implicitly serve
                                    as a functionality.

                            Args:
                                root (TK) : is the window for putting in buttons and other functionalities'
                                entry (Entry): Entry which holds calculations done by user

                            Returns:
                                void
                            """
    square_radical_frame = Frame(root)
    oneover_factorial_frame = Frame(root)
    perc_info_frame = Frame(root)

    square_button = Button(square_radical_frame, text="x²", padx=48, pady=4, command=lambda: bl.calc_square(entry))
    radical_button = Button(square_radical_frame, text="√", padx=49, pady=4, command=lambda: bl.calc_root(entry))
    one_over_button = Button(oneover_factorial_frame, text="⅟", padx=48, pady=4,
                             command=lambda: bl.calc_one_over(entry))
    factorial_button = Button(oneover_factorial_frame, text="x!", padx=48, pady=4,
                              command=lambda: bl.calc_factorial(entry))
    precentage_button = Button(perc_info_frame, text="%", padx=48, pady=4, command=lambda: bl.calc_percentage(entry))
    info_button = Button(perc_info_frame, text="i", padx=48, pady=4, command=lambda: bl.show_instruction(), bg="yellow")

    square_button.pack(side="top")
    radical_button.pack(side="bottom")

    one_over_button.pack(side="top")
    factorial_button.pack(side="bottom")

    precentage_button.pack(side="top")
    info_button.pack(side="bottom")

    square_radical_frame.grid(row=2, column=0, sticky="nsew")
    oneover_factorial_frame.grid(row=2, column=1, sticky="nsew")
    perc_info_frame.grid(row=2, column=2, sticky="nsew")
