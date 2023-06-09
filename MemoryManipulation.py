from tkinter import END
from ButtonListener import empty_number_replacer


def memory_addition(memo_content, entry):
    entry_number = empty_number_replacer(entry)
    memo = memo_content.cget("text")

    memo_content.config(text=float(entry_number) + float(memo))


def memory_subtraction(memo_content, entry):
    entry_number = empty_number_replacer(entry)
    memo = memo_content.cget("text")

    memo_content.config(text=float(memo) - float(entry_number))


def memory_read(memo_content, entry):
    entry.delete(0, END)
    entry.insert(0, memo_content.cget("text"))


def memory_clean(memo_content):
    memo_content.config(text=0)
