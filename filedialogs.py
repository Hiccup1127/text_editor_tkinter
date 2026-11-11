import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog

import notebook

import os
from os import walk


files = []

work_dir = {
    "Path": None,
    "Name": None,
    "SubDirectories": {},
    "DirectoryFiles": []
}


def get_file(active_notebook: notebook.MainNotebook=None):
    path = filedialog.askopenfile(
        title="Open a file ...",
        filetypes=(
            ("Text file", "*.txt"),
            ("Python code", "*.py"),
            ("All files", ["*.*",])
        )
    )
    if active_notebook:
        with open(path.name, "rb") as file:
            file_name = path.name.split("/")[-1]
            
            active_notebook.tab_new = notebook.TabFrame(active_notebook, file_name)
            active_notebook.add_tab(active_notebook.tab_new, file_name)
            active_notebook.tab_new.text_screen.insert(
                index=1.0, chars=file.read())
            active_notebook.tab_new.tab_file_path = path.name
            active_notebook.select(active_notebook.tab_new)
    return path


def save_file_path(text: str, optional_file_path: str=None):
    if optional_file_path is not None:
        try:
            with open(optional_file_path, "w") as new_file:
                new_file.write(text)
                new_file.close()
            return optional_file_path
        except Exception as e:
            return f"Got an unexpected error: {e}";
    else:
        try:  
            file_object = filedialog.asksaveasfile(
                defaultextension=".txt",
                filetypes = (
                    ("Text file", ".txt"),
                    ("Python code", ".py"),
                    ("All files", ".*")
                ),
            )
            file_path = file_object.name
            with open(file_path, "w") as new_file:
                new_file.write(text)
                new_file.close()
            return file_path
            # print(file_object) # complete refreshing the tab after saving new file            
        except UnboundLocalError, AttributeError:
            return;

def get_folder():
    try:
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
    except IndexError:
        return;