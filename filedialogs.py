import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog

from os import listdir
from os import walk


def get_file():
    file = filedialog.askopenfile(
        title="Open a file ...",
        filetypes=(
            ("Text file", "*.txt"),
            ("Python code", "*.py"),
            ("All files", ["*.*",])
        )
    )
    return file


def save_file_path(text: str):
    file_save = filedialog.asksaveasfile(
        defaultextension=".txt",
        filetypes = (
            ("Text file", ".txt"),
            ("Python code", ".py"),
            ("All files", ".*")
        ),
        # initialdir="C:\\Users\\"
    )
    if file_save is None:
        return;
    file_save.write(text)
    file_save.close()

def get_folder():
    folder = filedialog.askdirectory(
        title="Open a folder ...",
        initialdir = "C:\\Users\\"
    )
    data = listdir(folder)

    f = []
    for dd, ddn, fn in walk(folder):
        f.append(dd)
        f.append(ddn)
        f.append(fn)
    
    print(f)

    return folder, data