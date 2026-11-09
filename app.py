import tkinter as tk
import tkinter.ttk as ttk
import ttkbootstrap as ttk
import tkinter.scrolledtext as st
import top_menu
from notebook import *


LIGHT = "#fcfbf9"
LIGHT_FONT = "#000000"
LIGHT_HOVER =    "#f2d0b5"
LIGHT_SELECTED = "#fcb276"
DARK = "black"
DARK_FONT = "white"
DARK_HOVER =    "#2f2156"
DARK_SELECTED = "#161238"
TEXT_FONT = ("Monospace", "12")


class Application(tk.Tk):
    def __init__(self, title="Text editor"):
        super().__init__()
        self.title(title)
        self.geometry("800x600")


        self.sidebar = Sidebar(self)


        self.notebook = MainNotebook(self)

        self.tab1 = TabFrame(self)
        self.notebook.add_new(self.tab1, "new")


        self.top_menu = top_menu.MainMenu(self)
        self.config(menu=self.top_menu)
        self.top_menu.light_theme()


        self.bind("q", lambda e: self.destroy())


class Sidebar(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)


        self.main_container = ttk.Frame(self)
        self.main_container.pack(side="left", expand=1, fill="both")

        self.title = ttk.Label(self.main_container, font="Calibri 16", text="Content")
        self.title.pack(fill="x")

        self.content = ttk.Treeview(self.main_container)
        self.content.pack(expand=1, fill="both")


        self.separator = ttk.Frame(self,
            cursor="plus",
            width=2,
            style="separator1.TFrame"
        )
        self.separator.pack(side="left", expand=0, fill="y")
        self.separator.pack_propagate(0)
        self.separator.bind("<Button1-Motion>", self.resize)


        self.width = 250
        self.config(width=self.width)
        self.pack_propagate(0)

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


def main():
    app = Application()
    app.mainloop()


if __name__=="__main__":
    main()