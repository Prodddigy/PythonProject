from tkinter import END


def memory_addition(memo_content, entry):
    entry_number = entry.get()
    memo = memo_content.cget("text")

    if entry_number == "." or entry_number == "":
        entry_number = 0

    memo_content.config(text=float(entry_number) + float(memo))


def memory_subtraction(memo_content, entry):
    entry_number = entry.get()
    memo = memo_content.cget("text")

    if entry_number == "." or entry_number == "":
        entry_number = 0

    memo_content.config(text=float(memo) - float(entry_number))


def memory_read(memo_content, entry):
    entry.delete(0, END)
    entry.insert(0, memo_content.cget("text"))

def memory_clean(memo_content):
    memo_content.config(text =0)