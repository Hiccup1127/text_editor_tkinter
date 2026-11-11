import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog

import os
from os import walk


files = []

work_dir = {
    "Path": None,
    "Name": None,
    "SubDirectories": {},
    "DirectoryFiles": []
}


def get_file():
    file = filedialog.askopenfile(
        title="Open a file ...",
        filetypes=(
            ("Text file", "*.txt"),
            ("Python code", "*.py"),
            ("All files", ["*.*",])
        )
    )

    # move the "with" open file statement to here from line 51 top_menu.py

    return file


def save_file_path(text: str, optional_file_path: str=None):
    if optional_file_path is not None:
        # try:
        with open(optional_file_path, "w") as new_file:
            new_file.write(text)
            new_file.close()
        # except Exception:
        #     pass
    else:    
        file_object = filedialog.asksaveasfile(
            defaultextension=".txt",
            filetypes = (
                ("Text file", ".txt"),
                ("Python code", ".py"),
                ("All files", ".*")
            ),
            # initialdir="C:\\Users\\"
        )
        if file_path is None:
            return;
        file_path = file_object.name

        print(file_object) # complete refreshing tab after saving new file
        
        # with open(file_path, "w") as new_file:
        #     new_file.write(text)
        #     new_file.close()

def get_folder():
    folder = filedialog.askdirectory(
        title="Open a folder ...",
        initialdir = "C:\\Users\\"
    )

    path = folder
    folder_name = folder.split("/")[-1]
    folder_data = folder[1]

    work_dir["Path"] = path
    work_dir["Name"] = folder_name

    return work_dir

    # data = listdir(folder)

    # f = []
    # for dd, ddn, fn in walk(folder):
    #     f.append(dd)
    #     f.append(ddn)
    #     f.append(fn)
    
    # print(f)

    # return folder, data