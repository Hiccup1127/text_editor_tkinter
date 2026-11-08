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
            ("All files", "*.*")
        )
    )
    return file


def save_file():
    pass


def get_folder():
    folder = filedialog.askdirectory(
        title="Open a folder ...",
        initialdir = "C:\\Users\\catchy_cat14"
    )
    data = listdir(folder)

    f = []
    for dirpath, dirnames, filenames in walk(folder):
        row = (dirpath, dirnames, filenames)
        f.extend(row)
    
    print(f)

    return folder, data