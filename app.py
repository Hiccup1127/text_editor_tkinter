import tkinter as tk
import tkinter.ttk as ttk
import ttkbootstrap as ttk
import tkinter.scrolledtext as st
import top_menu
from notebook import *


LIGHT = "#fcfbf9"
LIGHT_FONT = "#000"
LIGHT_HOVER =    "#f2d0b5"
LIGHT_SELECTED = "#fcb276"
DARK = "#131116"
DARK_FONT = "#fff"
DARK_HOVER =    "#393244"
DARK_SELECTED = "#5e4d7c"
TEXT_FONT = ("Monospace", "12")


class Application(tk.Tk):
    def __init__(self, title="Text editor"):
        super().__init__()
        self.title(title)
        self.geometry("800x600")


        self.selected_theme = "light"
        self.top_menu = top_menu.MainMenu(self)
        self.config(menu=self.top_menu)
        self.top_menu.light_theme()


        self.sidebar = Sidebar(self)


        self.notebook = MainNotebook(self)

        self.tab1 = TabFrame(self.notebook, "new")
        self.notebook.add_tab(self.tab1, "new")


        self.bind("q", lambda e: self.destroy())


class Sidebar(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.width = 250
        self.config(width=self.width)
        self.pack_propagate(0)


        self.main_container = ttk.Frame(self)
        self.main_container.pack(side="left", expand=1, fill="both")

        self.title = ttk.Label(self.main_container, font="Calibri 14", text="OPEN FILES")
        self.title.pack(fill="x", pady=(0, 15))


        self.separator = ttk.Frame(self,
            cursor="plus",
            width=2,
            style="separator1.TFrame"
        )
        self.separator.pack(side="left", expand=0, fill="y")
        self.separator.pack_propagate(0)
        self.separator.bind("<Button1-Motion>", self.resize)


        self.pack(side="left", fill="both", expand=0)

    def resize(self, event):
        const_width = 250
        if event.x > 5:
            event.x = 1
            self.width += event.x
        elif event.x < -5: 
            event.x = -1
            self.width += event.x
        else:
            self.width += event.x

        if self.width > 400 or self.width < 220:
            return;
        else:
            self.config(width=self.width)
    
    current_dir = False

    def open_directory(self, folder_name: str):
        if self.__class__.current_dir:
            self.forget_directory()
        self.dir_name = ttk.Label(self.main_container, font="Calibri 12", text=folder_name)
        self.dir_name.pack(fill="x", pady=(0, 10))

        self.content = ttk.Treeview(self.main_container, columns=("Dir"), show="tree")
        self.content.column("#0", width=30)
        self.content.heading("Dir", text="Folder", anchor="w")

        a = self.content.insert("", 'end', values=("Folder1"))
        self.content.insert(a, 'end', values=("Folder12"))
        self.content.insert(a, 'end', values=("Folder13"))
        b = self.content.insert("", 'end', values=("Folder2"))
        self.content.insert(b, 'end', values=("Folder22"))
        self.content.insert(b, 'end', values=("Folder23"))
        c = self.content.insert("", 'end', values=("Folder3"))
        d = self.content.insert(c, 'end', values=("Folder32"))
        self.content.insert(d, 'end', values=("Folder33"))
        self.content.insert(d, 'end', values=("Folder33"))
        self.content.insert(d, 'end', values=("FILE"))
        self.content.insert("", 'end', values=("File"))
        self.content.insert("", 'end', values=("File"))
        self.content.insert("", 'end', values=("File"))
        self.content.insert("", 'end', values=("File"))
        self.content.insert("", 'end', values=("File"))

        self.content.bind("<Button-1>", lambda e: self.content.selection_set(()))

        self.xs = tk.Scrollbar(self.main_container,
        orient="horizontal", command=self.content.xview)
        self.content.config(xscrollcommand=self.xs.set)
        self.xs.pack(side="bottom", fill="x")
        self.content.pack(expand=1, fill="both")

        self.__class__.current_dir = True

    def forget_directory(self):
        self.dir_name.pack_forget()
        self.content.pack_forget()
        self.__class__.current_dir = False


def main():
    app = Application()
    app.mainloop()


if __name__=="__main__":
    main()