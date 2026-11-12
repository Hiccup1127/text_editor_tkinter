import tkinter as tk
import ttkbootstrap as ttk
from app import *
from notebook import *
import filedialogs as f


class MainMenu(ttk.Menu):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        self.container = container

        self.file_menu = tk.Menu(self, bg=DARK, fg=DARK_FONT)
        self.add_cascade(label="File", menu=self.file_menu)

        self.file_menu.add_command(label="New file...", command=self.new_tab)
        self.file_menu.add_command(label="Open file...", command=self.get_file)
        self.file_menu.add_command(label="Save", command=self.set_file)
        self.file_menu.add_command(label="Save As...", command=self.set_file_as)
        self.file_menu.add_command(label="Close file", command=self.close_tab)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.container.destroy)

        self.edit_menu = tk.Menu(self, bg=DARK, fg=DARK_FONT)
        self.add_cascade(label="Edit", menu=self.edit_menu)

        self.edit_menu.add_command(label="Undo")
        self.edit_menu.add_command(label="Redo")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut")
        self.edit_menu.add_command(label="Copy")
        self.edit_menu.add_command(label="Paste")

        self.theme_menu = tk.Menu(self, bg=LIGHT, fg=LIGHT_FONT)
        self.add_cascade(label="Theme", menu=self.theme_menu)

        self.theme_menu.add_command(label="Light",
            command=lambda:self.container.set_theme(LIGHT,
            LIGHT_FONT, LIGHT_HOVER, LIGHT_SELECTED))
        self.theme_menu.add_command(label="Dark",
            command=lambda:self.container.set_theme(DARK,
            DARK_FONT, DARK_HOVER,DARK_SELECTED))

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