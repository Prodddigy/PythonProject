from tkinter import END, messagebox, DISABLED, NORMAL
from math import sqrt


def button_number_choice(number, entry):
    entry.config(state=NORMAL)
    current = entry.get()
    if number == "." and "." in current:
        entry.config(state=DISABLED)
    else:
        entry.delete(0, END)
        entry.insert(0, str(current) + str(number))
        entry.config(state=DISABLED)


def button_negate(entry):
    entry.config(state=NORMAL)
    current = entry.get()
    entry.delete(0, END)

    entry.insert(0, -1 * float(current))
    entry.config(state=DISABLED)


def button_clear(entry):
    entry.config(state=NORMAL)
    entry.delete(0, END)
    entry.config(state=DISABLED)


def button_erase(entry):
    entry.config(state=NORMAL)
    a = entry.get()
    if a != '':
        entry.delete(0, END)
        entry.insert(0, a[:-1])
    entry.config(state=DISABLED)


def button_add(entry):
    entry.config(state=NORMAL)
    first_number = entry.get()

    global current_symbol
    global current_number
    current_symbol = "addition"
    check_empty_number(first_number)
    entry.delete(0, END)
    entry.config(state=DISABLED)


def button_subtract(entry):
    entry.config(state=NORMAL)
    first_number = entry.get()

    global current_symbol
    global current_number
    current_symbol = "subtraction"
    check_empty_number(first_number)
    entry.delete(0, END)
    entry.config(state=DISABLED)


def button_multiply(entry):
    entry.config(state=NORMAL)
    first_number = entry.get()
    global current_symbol
    global current_number
    current_symbol = "multiplication"

    check_empty_number(first_number)
    entry.delete(0, END)
    entry.config(state=DISABLED)

def button_divide(entry):
    entry.config(state=NORMAL)
    first_number = entry.get()
    global current_symbol
    global current_number
    current_symbol = "division"
    check_empty_number(first_number)
    entry.delete(0, END)
    entry.config(state=DISABLED)


def check_empty_number(first_number):
    if first_number == '':
        messagebox.showinfo(title="Empty field", message="Before you press '=' create a equation ex. 2 + 2 :)")
    else:
        global current_number
        if first_number == ".":
            first_number = ".0"
        current_number = float(first_number)


def empty_number_replacer(entry):
    number = entry.get()

    if number == "." or number == "":
        number = "0"
    return number


def button_equal(entry):
    entry.config(state=NORMAL)
    second_number = empty_number_replacer(entry)
    entry.delete(0, END)
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
            try:
                entry.insert(0, current_number / float(second_number))

            except ZeroDivisionError:
                messagebox.showinfo(title="Division by zero Error", message="Come on, you are better than that "
                                                                            "try not to divide by zero...")
                entry.delete(0, END)
    entry.config(state=DISABLED)


def calc_square(entry):
    entry.config(state=NORMAL)
    current_num = empty_number_replacer(entry)
    entry.delete(0, END)

    try:

        entry.insert(0, float(current_num) ** 2)
    except OverflowError:
        messagebox.showinfo(title="Too big number", message="The number is too large and to difficult for python :( "
                                                            "to calculate")
    entry.config(state=DISABLED)


def calc_root(entry):
    entry.config(state=NORMAL)
    current_num = empty_number_replacer(entry)
    try:

        entry.insert(0, sqrt(float(current_num)))
    except ValueError:
        messagebox.showinfo(title="Precision point", message="Precision point is too long for python to handle")
    entry.config(state=DISABLED)


def calc_one_over(entry):
    entry.config(state=NORMAL)
    current_num = empty_number_replacer(entry)
    entry.delete(0, END)
    try:
        entry.insert(0, 1 / float(current_num))

    except ZeroDivisionError:
        messagebox.showinfo(title="Division by zero Error", message="Come on, you are better than that "
                                                                    "try not to divide by zero...")
    entry.config(state=DISABLED)


def calc_factorial(entry):
    entry.config(state=NORMAL)
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
    entry.config(state=NORMAL)
    current_num = int(empty_number_replacer(entry))
    entry.delete(0, END)
    entry.insert(0, float(current_num) / 100)
    entry.config(state=DISABLED)


def show_instruction():
    messagebox.showinfo(title="How to use this calculator", message="Instructions:"
                                                                    "Press number from 0-9 and press a desired calculation: +, -, /, *; and then choose second number for the equation.\n"
                                                                    "Finally press \" = \" button to show the result.\n"
                                                                    "Starting from Top left corner:\n"
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
