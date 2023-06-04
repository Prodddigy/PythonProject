from tkinter import *
from tkinter import messagebox




if __name__ == "__main__":

    root = Tk()

    root.title("Najlepszy Kalkulator na świecie!")

    entry = Entry(root, width = 50, borderwidth=5)

    entry.grid(row = 0 , column = 0 , columnspan = 3 , padx = 15, pady = 10)
    memo_box = LabelFrame(root, height = 50 ,width=150, text = "Here is your Memo")
    memo_box.config(font =("Courier", 10))
    memo_box.grid(row = 0 , column = 4 )
    root.mainloop()

