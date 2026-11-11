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
        self.light_theme()


        self.sidebar = Sidebar(self)


        self.notebook = MainNotebook(self)

        self.tab1 = TabFrame(self.notebook, "new")
        self.notebook.add_tab(self.tab1, "new")

        self.top_menu = top_menu.MainMenu(self)
        self.config(menu=self.top_menu)


        self.bind("q", lambda e: self.destroy())
    
    def light_theme(self):
        s = ttk.Style()
        s.layout("TNotebook", [])
        s.configure("TNotebook", background=LIGHT, foreground=LIGHT_FONT)
        s.configure("TNotebook", tabmargins=0)
        s.configure("TNotebook.Tab", background=LIGHT, foreground=LIGHT_FONT)
        s.map("TNotebook.Tab", background=[("active", LIGHT_HOVER),
                                           ("selected", LIGHT_SELECTED)],
                               foreground=[("selected", LIGHT_FONT)])
        s.configure("TLabel", background=LIGHT, foreground=LIGHT_FONT)
        s.configure("TFrame", background=LIGHT)
        s.configure("Treeview", background=LIGHT,foreground=LIGHT_FONT,
                                font=("Calibri", 11))
        s.configure("Treeview.Heading", background=LIGHT, foreground=LIGHT_FONT)
        s.map("Treeview", background=[("selected", LIGHT_SELECTED)],
                          foreground=[("selected", LIGHT_FONT)])
        s.configure("separator1.TFrame", background=LIGHT_FONT)
        TabFrame.change_tab_theme(LIGHT, LIGHT_FONT)
        self.selected_theme = "light"
    
    def dark_theme(self):
        s = ttk.Style()
        s.layout("TNotebook", [])
        s.configure("TNotebook", background=DARK, foreground=DARK_FONT)
        s.configure("TNotebook", tabmargins=0)
        s.configure("TNotebook.Tab", background=DARK, foreground=DARK_FONT)
        s.map("TNotebook.Tab", background=[("active", DARK_HOVER),
                                           ("selected", DARK_SELECTED)],
                               foreground=[("selected", DARK_FONT)])
        s.configure("TLabel", background=DARK, foreground=DARK_FONT)
        s.configure("TFrame", background=DARK)
        s.configure("Treeview", background=DARK, foreground=DARK_FONT)
        s.configure("Treeview.Heading", background=DARK, foreground=DARK_FONT)
        s.map("Treeview", background=[("selected", DARK_SELECTED)],
                          foreground=[("selected", DARK_FONT)])
        s.configure("separator1.TFrame", background=DARK_FONT)
        TabFrame.change_tab_theme(DARK, DARK_FONT)
        self.selected_theme = "dark"


class Sidebar(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.container = container
        self.width = 250
        self.config(width=self.width)
        self.pack_propagate(0)


        self.main_container = ttk.Frame(self)
        self.main_container.pack(side="left", expand=1, fill="both")

        self.title = ttk.Label(self.main_container, font="Calibri 16", text="OPEN FILES")
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
            event.x = 3
            self.width += event.x
        elif event.x < -5: 
            event.x = -3
            self.width += event.x
        else:
            self.width += event.x

        if self.width > 700 or self.width < 220:
            return;
        else:
            self.config(width=self.width)
    
    current_dir = False

    def open_directory(self, directory: str):
        if self.__class__.current_dir:
            self.forget_directory()
        self.dir_name = ttk.Label(self.main_container, font="Calibri 14", text=directory["Name"])
        self.dir_name.pack(fill="x", pady=(0, 10))

        self.content = ttk.Treeview(self.main_container, columns=("Dir"), show="tree")
        self.content.column("#0", width=0)
        self.content.heading("Dir", text="Folder", anchor="w")
            
        for n, p in directory["Files"]:
            a = self.content.insert("", 'end', values=(n))


        self.right_click_menu_on_sidebar = tk.Menu(self.container)
        self.right_click_menu_on_sidebar.add_command(label="Rename...",
            command=self.rename_file_in_directory)
        self.right_click_menu_on_sidebar.add_command(label="Copy path") # implement this

        self.content.bind("<Button-1>", lambda e: self.content.selection_set(()))
        self.content.bind("<Button-3>", lambda e:
            self.right_click_menu_on_sidebar.tk_popup(e.x_root, e.y_root))

        # TO DO: COPY PATH; RENAME; OPEN BY A CLICK; AND THAT'D BE THE END!
        self.xs = tk.Scrollbar(self.main_container,
        orient="horizontal", command=self.content.xview)
        self.content.config(xscrollcommand=self.xs.set)
        self.xs.pack(side="bottom", fill="x")
        self.content.pack(expand=1, fill="both")

        self.directory = directory
        self.__class__.current_dir = True

    def rename_file_in_directory(self):
        focused_file = self.content.focus() # implement opening the file by double-click
        index = int(focused_file[1:])-1
        print(self.directory["Files"][index]) # complete renaming the files feature
        x = input("-> ")
        self.content.insert("", str(focused_file)[1:], values=(x))
        self.content.delete(focused_file)

    def forget_directory(self):
        if not self.__class__.current_dir:
            return True
        self.dir_name.pack_forget()
        self.content.pack_forget()
        self.__class__.current_dir = False


def main():
    app = Application()
    app.mainloop()


if __name__=="__main__":
    main()