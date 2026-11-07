import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog


def get_file():
    file = filedialog.askopenfile(
        title="Open a file...",
        filetypes=(
            ("Text file", "*.txt"),
            ("Python code", "*.py"),
            ("All files", "*.*")
        )
    )
    return file


def save_file():
    pass


def open_folder():
    pass