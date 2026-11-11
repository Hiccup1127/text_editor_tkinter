import tkinter as tk
import ttkbootstrap as ttk
from app import *
from notebook import *
import filedialogs as f


class MainMenu(ttk.Menu):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        self.container = container

        self.file_menu = tk.Menu(self, bg=LIGHT, fg=LIGHT_FONT)
        self.add_cascade(label="File", menu=self.file_menu)

        def new_tab():
            tab = TabFrame(self.container.notebook)
            self.container.notebook.add_tab(tab)
        self.file_menu.add_command(label="New file...", command=new_tab)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Open file...", command=self.open_file)
        self.file_menu.add_command(label="Open folder...", command=self.open_folder)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As...", command=self.save_file_as)
        def close_tab_menu():
            self.container.notebook.close_tab()
        self.file_menu.add_command(label="Close", command=close_tab_menu)
        self.file_menu.add_command(label="Close folder", command=self.close_folder)

        self.edit_menu = tk.Menu(self, bg=LIGHT, fg=LIGHT_FONT)
        self.add_cascade(label="Edit", menu=self.edit_menu)

        self.edit_menu.add_command(label="Undo")
        self.edit_menu.add_command(label="Redo")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut")
        self.edit_menu.add_command(label="Copy")
        self.edit_menu.add_command(label="Paste")

        self.theme_menu = tk.Menu(self, bg=LIGHT, fg=LIGHT_FONT)
        self.add_cascade(label="Theme", menu=self.theme_menu)

        self.theme_menu.add_command(label="Light",command=self.container.light_theme)
        self.theme_menu.add_command(label="Dark", command=self.container.dark_theme)
        self.theme_menu.add_separator()
        self.theme_menu.add_command(label="Settings")

    def open_file(self):
        path = f.get_file()
        with open(path.name, "rb") as file:
            file_name = path.name.split("/")[-1]
            
            self.container.tab_new = TabFrame(self.container.notebook, file_name)
            self.container.notebook.add_tab(self.container.tab_new, file_name)
            self.container.tab_new.text_screen.insert(
                index=1.0, chars=file.read()
            )
            self.container.tab_new.tab_file_path = path.name
            self.container.notebook.select(self.container.tab_new)

    def save_file(self):
        current_tab = self.container.notebook.get_selected()
        if current_tab.tab_file_path is None:
            self.save_file_as()
        else:
            text = current_tab.text_screen.get(1.0, 'end')
            f.save_file_path(text, current_tab.tab_file_path)

    def save_file_as(self):
        tab = self.container.notebook.get_selected()
        text = tab.text_screen.get(1.0, 'end')
        f.save_file_path(text)
    
    def open_folder(self):
        dir = f.get_folder()
        self.container.sidebar.open_directory(f.work_dir.get("Name"))
    
    def close_folder(self):
        f.work_dir["Path"] = None
        f.work_dir["Name"] = None
        f.work_dir["SubDirectories"] = {}
        f.work_dir["DirectoryFiles"] = []
        self.container.sidebar.forget_directory()