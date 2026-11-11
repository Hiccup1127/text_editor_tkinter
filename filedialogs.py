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

# CHECK the problems/file_saving.py to read some of my notes
def open_file(active_notebook: notebook.MainNotebook=None):
    try:
        file_object = filedialog.askopenfile(
            title="Open a file ...",
            filetypes=(
                ("Text file", "*.txt"),
                ("Python code", "*.py"),
                ("All files", ["*.*",])
            )
        )
        file_path = file_object.name
        file_name = file_path.split("/")[-1]
        active_notebook.tab_new = notebook.TabFrame(active_notebook, file_name)
        active_notebook.add_tab(active_notebook.tab_new, file_name)
        with open(file_path, "rb") as file:
            active_notebook.tab_new.text_screen.insert(
                index=1.0, chars=file.read())
        active_notebook.tab_new.tab_file_path = file_path
        active_notebook.select(active_notebook.tab_new)
        return file_path
    except Exception as e:
        print(f"Can't OPEN the file, {e}")
        return e;

def save_file(active_notebook: notebook.MainNotebook=None, force=False):
    try:
        active_tab = active_notebook.get_selected()
        tab_text = active_tab.text_screen.get(1.0, 'end') # should do by chuncks btw
        if active_tab.tab_file_path is None or force==True: # new tab or force
            file_object = filedialog.asksaveasfile(
                defaultextension=".txt",
                filetypes = (
                    ("Text file", ".txt"),
                    ("Python code", ".py"),
                    ("All files", ".*")
                ),
            )
            file_path = file_object.name
            file_name = file_path.split("/")[-1]
            with open(file_path, "w") as new_file:
                new_file.write(tab_text)
            active_notebook.change_tab(file_name)
            active_tab.tab_name = file_name
            active_tab.tab_file_path = file_path
        else: # not new tab, updating the existing file
            with open(active_tab.tab_file_path, "w") as file_to_write:
                file_to_write.write(tab_text)
        return active_tab.tab_file_path
    except Exception as e:
        print(f"Can't SAVE the file, {e}")
        return e;

def open_folder():
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
    except IndexError:
        return;