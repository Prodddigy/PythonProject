from tkinter import END, messagebox, DISABLED, NORMAL
from math import sqrt

"""
This module provides a set of functions used for manipulation over entry value

Functions:
    button_number_choice -- is used by number buttons and dot buttons for entering new numbers
    button_negate -- is Used by negation button for negating the entry value
    button_clear -- is used by C button for clearing whole entry
    button_erase -- is used by <x button for erasing entry content digit by digit
    button_add -- is used by + button for addition of first number and the next inputted number
    button_subtract -- is used by - button for subtraction of first number from the next inputted number
    button_multiply -- is used by * button for multiplication of first number with the next inputted number
    button_divide -- is used by / button for division of first number with the next inputted number
    check_empty_number -- is used by +,-,/,*; buttons for checking if the inputted value is an empty string aka no input found
    empty_number_replacer -- used by =,x²,√,x!,%,⅟,M+,M-; buttons for replacing empty string or single dot in output with "0"
    button_equal -- is used for finalizing equations done by +,-,/,*; buttons and puts the result on the entry
    calc_square -- is used by x² button for calculating square of entry number
    calc_root -- is used by √ button for calculating square root of entry number
    calc_one_over --  is used for calculating division of 1 by entry number
    calc_factorial --  is used for calculating factorial of entry number
    calc_percentage --  is used for calculating percentage of entry number
    show_instruction --  when pressed pops out a messagebox with instructions on how to use this calculator
Global variables:
    current_symbol -- holds the value of current symbol: "division","addition","subtraction","multiplication"; chosen by user
    current_number -- holds value of the 1st number later calculated with next number after inputting +,-,/,* symbols
These globals are created in : button_subtract,button_add, button_multiply ,button_divide functions.
    
    
"""


def button_number_choice(number, entry):
    """
            is used by number buttons and dot button for entering new numbers, additionally checks if there are
             no more than 1 dot in the entry number.

            Args:
                entry (Entry): Entry which holds calculations done by user

            Returns:
                void
            """
    entry.config(state=NORMAL)
    current = entry.get()
    if number == "." and "." in current:
        entry.config(state=DISABLED)
    else:
        entry.delete(0, END)
        entry.insert(0, str(current) + str(number))
        entry.config(state=DISABLED)


def button_negate(entry):
    """
                is Used by negation button for negating the entry value

                Args:
                    entry (Entry): Entry which holds calculations done by user

                Returns:
                    void
                """
    entry.config(state=NORMAL)
    current = entry.get()
    entry.delete(0, END)

    entry.insert(0, -1 * float(current))
    entry.config(state=DISABLED)


def button_clear(entry):
    """
                   is used by C button for clearing whole entry

                   Args:
                       entry (Entry): Entry which holds calculations done by user

                   Returns:
                       void
                   """
    entry.config(state=NORMAL)
    entry.delete(0, END)
    entry.config(state=DISABLED)


def button_erase(entry):
    """
                       is used by <x button for erasing entry content digit by digit.
                       If the entry is empty it doesn't erase.

                       Args:
                           entry (Entry): Entry which holds calculations done by user

                       Returns:
                           void
                       """
    entry.config(state=NORMAL)
    a = entry.get()
    if a != '':
        entry.delete(0, END)
        entry.insert(0, a[:-1])
    entry.config(state=DISABLED)


def button_add(entry):
    """
                           is used by + button for addition of first number and the next inputted number.

                           Args:
                               entry (Entry): Entry which holds calculations done by user

                           Returns:
                               void
                           """
    entry.config(state=NORMAL)
    first_number = entry.get()

    global current_symbol
    global current_number
    current_symbol = "addition"
    check_empty_number(first_number)
    entry.delete(0, END)
    entry.config(state=DISABLED)


def button_subtract(entry):
    """
                               is used by - button for subtraction of first number from the next inputted number.

                               Args:
                                   entry (Entry): Entry which holds calculations done by user

                               Returns:
                                   void
                               """
    entry.config(state=NORMAL)
    first_number = entry.get()

    global current_symbol
    global current_number
    current_symbol = "subtraction"
    check_empty_number(first_number)
    entry.delete(0, END)
    entry.config(state=DISABLED)


def button_multiply(entry):
    """
                                   is used by * button for multiplication of first number with the next inputted number

                                   Args:
                                       entry (Entry): Entry which holds calculations done by user

                                   Returns:
                                       void
                                   """

    entry.config(state=NORMAL)
    first_number = entry.get()
    global current_symbol
    global current_number
    current_symbol = "multiplication"

    check_empty_number(first_number)
    entry.delete(0, END)
    entry.config(state=DISABLED)


def button_divide(entry):
    """
                                       is used by / button for division of first number with the next inputted number

                                       Args:
                                           entry (Entry): Entry which holds calculations done by user

                                       Returns:
                                           void
                                       """
    entry.config(state=NORMAL)
    first_number = entry.get()
    global current_symbol
    global current_number
    current_symbol = "division"
    check_empty_number(first_number)
    entry.delete(0, END)
    entry.config(state=DISABLED)


def check_empty_number(first_number):
    """
                    is used by +,-,/,*; buttons for checking if the inputted value is an empty string aka no input found.
                    if no input found from first_number, it pops out messagebox with appropriate warning.

                    Args:
                        first_number (string) : is the number inputted before clicking +,/,-,* buttons

                    Returns:
                        void
                    """
    if first_number == '':
        messagebox.showinfo(title="Empty field", message="Before you press '=' create a equation ex. 2 + 2 :)")
    else:
        global current_number
        if first_number == ".":
            first_number = ".0"
        current_number = float(first_number)


def empty_number_replacer(entry):
    """
                       used by =,x²,√,x!,%,⅟,M+,M-; buttons for replacing empty string or single dot in output with "0"

                       Args:
                           entry (Entry): Entry which holds calculations done by user

                       Returns:
                           number (string): checked number that is held in entry text attribute
                       """
    number = entry.get()

    if number == "." or number == "":
        number = "0"
    return number


def button_equal(entry):
    """
                           is used for finalizing equations done by +,-,/,*; buttons and puts the result on the entry.

                           Args:
                               entry (Entry): Entry which holds calculations done by user

                           Returns:
                                void
                           """
    entry.config(state=NORMAL)
    second_number = empty_number_replacer(entry)
    entry.delete(0, END)
    # it checks whether the global variables current_symbol and current number where ever created in the memory
    # in case user just presses = sign repeatedly
    if ('current_symbol' not in globals()) or 'current_number' not in globals():
        messagebox.showinfo(title="Empty field", message="Before you press '=' create a equation ex. 2 + 2 :)")
    else:

        if current_symbol == "addition":
            entry.insert(0, current_number + float(second_number))

        if current_symbol == "subtraction":
            entry.insert(0, current_number - float(second_number))

        if current_symbol == "multiplication":
            entry.insert(0, current_number * float(second_number))

        if current_symbol == "division":
            # in case of division by zero try catch handles it and show appropriate message box
            try:
                entry.insert(0, current_number / float(second_number))

            except ZeroDivisionError:
                messagebox.showinfo(title="Division by zero Error", message="Come on, you are better than that "
                                                                            "try not to divide by zero...")
                entry.delete(0, END)
    entry.config(state=DISABLED)


def calc_square(entry):
    """
                               is used by x² button for calculating square of entry number

                               Args:
                                   entry (Entry): Entry which holds calculations done by user

                               Returns:
                                    void
                               """
    entry.config(state=NORMAL)
    current_num = empty_number_replacer(entry)
    entry.delete(0, END)
# additionally it handles situations when number is too high for the calculation and pops out appropriate warning
    try:

        entry.insert(0, float(current_num) ** 2)
    except OverflowError:
        messagebox.showinfo(title="Too big number", message="The number is too large and to difficult for python :( "
                                                            "to calculate")
    entry.config(state=DISABLED)


def calc_root(entry):
    """
                               is used by √ button for calculating square root of entry number

                               Args:
                                   entry (Entry): Entry which holds calculations done by user

                               Returns:
                                    void
                               """

    entry.config(state=NORMAL)
    current_num = empty_number_replacer(entry)
    # additionally checks if precision is too problematic and too long for python and catches ValueError
    try:

        entry.insert(0, sqrt(float(current_num)))
    except ValueError:
        messagebox.showinfo(title="Precision point", message="Precision point is too long for python to handle")
    entry.config(state=DISABLED)


def calc_one_over(entry):
    """
                                   is used for calculating division of 1 by entry number

                                   Args:
                                       entry (Entry): Entry which holds calculations done by user

                                   Returns:
                                        void
                                   """
    entry.config(state=NORMAL)
    current_num = empty_number_replacer(entry)
    entry.delete(0, END)
    # additionally catches division by zero error
    try:
        entry.insert(0, 1 / float(current_num))

    except ZeroDivisionError:
        messagebox.showinfo(title="Division by zero Error", message="Come on, you are better than that "
                                                                    "try not to divide by zero...")
    entry.config(state=DISABLED)


def calc_factorial(entry):
    """
                                        is used for calculating factorial of entry number

                                       Args:
                                           entry (Entry): Entry which holds calculations done by user

                                       Returns:
                                            void
                                       """
    entry.config(state=NORMAL)
    # additionally catches if user tried to make a factorial of float point number instead of integer
    try:
        current_num = int(empty_number_replacer(entry))
        result = 1
        entry.delete(0, END)
        for n in range(2, current_num + 1):
            result *= n
        entry.insert(0, result)
    except TypeError:
        messagebox.showinfo(title="Factorial of float", message="In order to use factorial you must enter integer "
                                                                "number.")
    entry.config(state=DISABLED)


def calc_percentage(entry):
    """
                                            is used for calculating percentage of entry number

                                           Args:
                                               entry (Entry): Entry which holds calculations done by user

                                           Returns:
                                                void
                                           """
    entry.config(state=NORMAL)
    current_num = int(empty_number_replacer(entry))
    entry.delete(0, END)
    entry.insert(0, float(current_num) / 100)
    entry.config(state=DISABLED)


def show_instruction():
    """
                                            when pressed pops out a messagebox with instructions on how to use this calculator

                                           Args:
                                              No arguments

                                           Returns:
                                                void
                                           """

    messagebox.showinfo(title="How to use this calculator", message="Instructions:"
                                                                    "Press number from 0-9 and press a desired calculation: +, -, /, *; and then choose second number for the equation.\n"
                                                                    "Finally press \" = \" button to show the result.\n"
                                                                    "\n"
                                                                    "Starting from Top left corner:\n"
                                                                    "\n"
                                                                    "M+: this action adds the currently seen result in memory and is later shown on the left side corner.\n"
                                                                    "M-: on the other hands subtracts from the currently saved memory.\n"
                                                                    "MC: clears the current memory.\n"
                                                                    "MR: reads from the memory and puts it into the entry.\n"
                                                                    "C: cleans the current entry.\n"
                                                                    "<x: erases the entry digit by digit with each click.\n"
                                                                    "x²: raises the entry number to 2nd power.\n"
                                                                    "√: calculates a square root of the entry number.\n"
                                                                    "⅟: calculates division of 1 by entry number.\n"
                                                                    "x!: calculates factorial of the entry number.\n"
                                                                    "%: makes a percentage number of entry number.\n"
                                                                    "¬: this negates the entry number.\n"
                                                                    ".: adds a float point precision to the result.\n"
                                                                    "\'/\': division ; \'*\': muliplication ; \'-\': subtraction ; \'+\' addition ; \'=\': equal sign.\n")
