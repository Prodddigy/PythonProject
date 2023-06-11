from tkinter import END, DISABLED, NORMAL
from ButtonListener import empty_number_replacer
"""
This module provides a set of functions used for memory manipulation.

Functions:
    memory_addition -- Adds a entry value to the memory_content text
    memory_subtraction -- Subtracts a entry value from the memory_content text
    memory_read -- Reads value from memory_content text and inserts it into entry field
    memory clean -- Cleans the memory_content text
"""

def memory_addition(memo_content, entry):
    """
        Adds a entry value to the memory_content text

        Args:
            memo_content (Label) : Label which holds the memory value
            entry (Entry): Entry which holds calculations done by user

        Returns:
            void
        """
    entry_number = empty_number_replacer(entry)
    memo = memo_content.cget("text")

    memo_content.config(text=float(entry_number) + float(memo))


def memory_subtraction(memo_content, entry):
    """
            Subtracts a entry value from the memory_content text

            Args:
                memo_content (Label) : Label which holds the memory value
                entry (Entry): Entry which holds calculations done by user

            Returns:
                void
            """
    entry_number = empty_number_replacer(entry)
    memo = memo_content.cget("text")

    memo_content.config(text=float(memo) - float(entry_number))


def memory_read(memo_content, entry):
    """
                Reads value from memory_content text and inserts it into entry field

                Args:
                    memo_content (Label) : Label which holds the memory value
                    entry (Entry): Entry which holds calculations done by user

                Returns:
                    void
                """
    entry.config(state=NORMAL)
    entry.delete(0, END)
    entry.insert(0, memo_content.cget("text"))
    entry.config(state=DISABLED)


def memory_clean(memo_content):
    """
                Cleans the memory_content text

                Args:
                    memo_content (Label) : Label which holds the memory value

                Returns:
                    void
                """

    memo_content.config(text=0)
