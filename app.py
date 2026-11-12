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
        self.geometry("750x600")
        self.selected_theme = "dark"
        self.set_theme(LIGHT, LIGHT_FONT, LIGHT_HOVER, LIGHT_SELECTED)

        self.notebook = MainNotebook(self)

        self.tab1 = TabFrame(self.notebook, "new")
        self.notebook.add_tab(self.tab1, "new")

        self.top_menu = top_menu.MainMenu(self)
        self.config(menu=self.top_menu)

        self.bind("q", lambda e: self.destroy())
    
    def set_theme(self, theme, theme_font, theme_hover, theme_selected):
        s = ttk.Style()
        s.layout("TNotebook", [])
        s.configure("TNotebook", background=theme, foreground=theme_font)
        s.configure("TNotebook", tabmargins=0)
        s.configure("TNotebook.Tab", background=theme, foreground=theme_font)
        s.map("TNotebook.Tab",
            background=[("active", theme_hover),("selected", theme_selected)],
            foreground=[("selected", theme_font)])
        s.configure("TLabel", background=theme, foreground=theme_font)
        s.configure("TFrame", background=theme)
        TabFrame.change_tab_theme(theme, theme_font)
        self.selected_theme = "dark" if self.selected_theme=="light" else "light"


def main():
    app = Application()
    app.mainloop()


if __name__=="__main__":
    main()