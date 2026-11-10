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
        self.file_menu.add_command(label="Save As...", command=self.save_file)
        def close_tab_menu():
            self.container.notebook.close_tab()
        self.file_menu.add_command(label="Close", command=close_tab_menu)

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

        self.theme_menu.add_command(label="Light",command=self.light_theme)
        self.theme_menu.add_command(label="Dark", command=self.dark_theme)
        self.theme_menu.add_separator()
        self.theme_menu.add_command(label="Settings")

    def light_theme(self):
        THEME = LIGHT
        THEME_FONT = LIGHT_FONT
        THEME_HOVER = LIGHT_HOVER
        THEME_SELECTED = LIGHT_SELECTED
        s = ttk.Style()
        
        s.layout("TNotebook", [])
        s.configure("TNotebook", background=THEME, foreground=THEME_FONT)
        s.configure("TNotebook", tabmargins=0)
        s.configure("TNotebook.Tab", background=THEME, foreground=THEME_FONT)
        s.map("TNotebook.Tab",
            background=[("active", THEME_HOVER),
                        ("selected", THEME_SELECTED)],
            foreground=[("selected", THEME_FONT)]
        )
        s.configure("TLabel", background=THEME, foreground=THEME_FONT)
        s.configure("TFrame", background=THEME)
        s.configure("Treeview", background=THEME)
        s.configure("separator1.TFrame", background=THEME_FONT)

        TabFrame.change_tab_theme(LIGHT, LIGHT_FONT)

        self.container.selected_theme = "light"
    
    def dark_theme(self):
        THEME = DARK
        THEME_FONT = DARK_FONT
        THEME_HOVER = DARK_HOVER
        THEME_SELECTED = DARK_SELECTED
        s = ttk.Style()
        
        s.layout("TNotebook", [])
        s.configure("TNotebook", background=THEME, foreground=THEME_FONT)
        s.configure("TNotebook", tabmargins=0)
        s.configure("TNotebook.Tab", background=THEME, foreground=THEME_FONT)
        s.map("TNotebook.Tab",
            background=[("active", THEME_HOVER),
                        ("selected", THEME_SELECTED)],
            foreground=[("selected", THEME_FONT)]
        )
        s.configure("TLabel", background=THEME, foreground=THEME_FONT)
        s.configure("TFrame", background=THEME)
        s.configure("Treeview", background=THEME)
        s.configure("separator1.TFrame", background=THEME_FONT)

        TabFrame.change_tab_theme(DARK, DARK_FONT)

        self.container.selected_theme = "dark"

    def open_file(self):
        path = f.get_file()
        file = open(path.name, "r")

        file_name = path.name.split("/")[-1]
        
        
        self.container.tab = TabFrame(self.container.notebook, file_name)
        self.container.notebook.add_tab(self.container.tab, file_name)
        self.container.tab.text_screen.insert(
            index=1.0, chars=file.read()
        )
        self.container.notebook.select(self.container.tab)
    
    def open_folder(self):
        path = f.get_folder()

        self.folder = path[0]
        self.folder_data = path[1]
    
    def save_file(self):
        tab = self.container.notebook.get_selected()
        print(tab, tab.tab_id, tab.tab_name, tab.tab_position)
        print(tab.text_screen.get(1.0, 'end'))