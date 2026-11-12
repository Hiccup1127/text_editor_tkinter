import tkinter as tk
import ttkbootstrap as ttk
from tkinter import filedialog

import notebook

# CHECK the problems/file_saving.py to read some of my notes
def open_file(active_notebook: notebook.MainNotebook=None):
    try:
        active_tab = active_notebook.get_selected()
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
        file_text = str()
        with open(file_path, "rb") as file:
            file_text = file.read()
        if active_tab.tab_file_path is None:
            active_tab.tab_name = file_name
            active_tab.tab_file_path = file_path
            active_tab.text_screen.insert(index=1.0, chars=file_text)
            active_notebook.change_tab(file_name)
        else:
            active_notebook.tab_new = notebook.TabFrame(active_notebook, file_name)
            active_notebook.add_tab(active_notebook.tab_new, file_name)
            active_notebook.tab_new.text_screen.insert(index=1.0, chars=file_text)
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
            if active_tab.tab_file_path is not None and force==True:
                active_notebook.tab_new = notebook.TabFrame(active_notebook, file_name)
                active_notebook.add_tab(active_notebook.tab_new, file_name)
                active_notebook.tab_new.text_screen.insert(index=1.0, chars=tab_text)
                active_notebook.tab_new.tab_file_path = file_path
                active_notebook.select(active_notebook.tab_new)
            else:
                active_tab.tab_name = file_name
                active_tab.tab_file_path = file_path
                active_notebook.change_tab(file_name)
        else: # not new tab, updating the existing file
            with open(active_tab.tab_file_path, "w") as file_to_write:
                file_to_write.write(tab_text)
        return active_tab.tab_file_path
    except Exception as e:
        print(f"Can't SAVE the file, {e}")
        return e;