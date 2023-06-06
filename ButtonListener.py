from tkinter import END

global f_num
global math


def button_click(number, entry):
 #   e.delete(0,END)
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(number))

def button_negate(entry):
    current = entry.get()
    entry.delete(0, END)

    entry.insert(0,-1 * float(current))

def button_clear(entry):
    entry.delete(0,END)

def button_add(entry):
    first_number = entry.get()

    math = "addition"
    ##f_num = float(first_number)
    #check_empty_number(first_number)
    entry.delete(0, END)
