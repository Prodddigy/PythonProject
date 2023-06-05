from tkinter import END


def button_click(number, entry):
 #   e.delete(0,END)
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(number))

def button_negate(entry):
    current = entry.get()
    entry.delete(0, END)
    if(float(current) < 0):
        entry.insert(0,-)