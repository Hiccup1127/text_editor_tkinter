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

        self.file_menu.add_command(label="New file...", command=self.new_tab)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Open file...", command=self.get_file)
        self.file_menu.add_command(label="Open folder...", command=self.get_folder)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save", command=self.set_file)
        self.file_menu.add_command(label="Save As...", command=self.set_file_as)
        self.file_menu.add_command(label="Close", command=self.close_tab)
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

    def new_tab(self):
        tab = TabFrame(self.container.notebook)
        self.container.notebook.add_tab(tab)
    
    def close_tab(self):
        self.container.notebook.close_tab()

    def get_file(self):
        file = f.open_file(self.container.notebook)

    def set_file(self):
        file = f.save_file(self.container.notebook)

    def set_file_as(self):                     
        file = f.save_file(self.container.notebook, force=True)
    
    def get_folder(self):
        dir = f.open_folder()
        self.container.sidebar.open_directory(f.work_dir.get("Name"))
    
    def close_folder(self):
        dir = f.work_dir
        dir["Path"] = None
        dir["Name"] = None
        dir["SubDirectories"] = {}
        dir["DirectoryFiles"] = []
        self.container.sidebar.forget_directory()