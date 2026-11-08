import tkinter as tk
import ttkbootstrap as ttk
import app
import filedialogs as f


class MainMenu(ttk.Menu):
    def __init__(self, container):
        super().__init__(container)
        self.container = container


        self.file_menu = ttk.Menu(self)
        self.add_cascade(label="File", menu=self.file_menu)

        self.file_menu.add_command(label="New file...",
            command=lambda: container.notebook.add_new(app.TabFrame(container))
        )
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Open file...", command=self.open_file)
        self.file_menu.add_command(label="Open folder...", command=self.open_folder)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save")
        self.file_menu.add_command(label="Save As...")
    
    def open_file(self):
        path = f.get_file()
        file = open(path.name, "r")

        file_name = path.name.split("/")[-1]
        
        
        self.container.tab = app.TabFrame(self.container)
        self.container.notebook.add_new(
            self.container.tab,
            tabname=file_name
        )
        self.container.tab.text_screen.insert(
            index=1.0, chars=file.read()
        )
        self.container.notebook.select(self.container.tab)
    
    def open_folder(self):
        path = f.get_folder()

        self.folder = path[0]
        self.folder_data = path[1]
        print(self.folder, self.folder_data)