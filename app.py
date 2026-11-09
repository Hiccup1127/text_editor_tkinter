import tkinter as tk
import tkinter.ttk as ttk
import ttkbootstrap as ttk
import tkinter.scrolledtext as st
import top_menu


LIGHT = "#fcfbf9"
LIGHT_FONT = "#000000"
LIGHT_HOVER =    "#f2d0b5"
LIGHT_SELECTED = "#fcb276"
DARK = "black"
DARK_FONT = "white"
DARK_HOVER =    "#2f2156"
DARK_SELECTED = "#161238"
THEME = LIGHT
THEME_FONT = LIGHT_FONT
THEME_HOVER = LIGHT_HOVER
THEME_SELECTED = LIGHT_SELECTED
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

        self.tab1 = TabFrame(self)
        self.notebook.add_new(self.tab1, "new")
        

        self.bind("q", lambda e: self.destroy())


class MainNotebook(ttk.Notebook):
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        self.new_tab = TabFrame(self)
        self.insert(len(self.tabs()), self.new_tab, text="+")

        self.bind("<Button-1>", self.new_tab_click)
        self.bind("<Button1-Motion>", self.tab_ordering)
        self.pack(expand=True, fill="both")
    
    def add_new(self, tab: TabFrame(), tabname: str="untitled", **kwargs):
        self.add(tab, text=tabname, **kwargs)
        self.insert(len(self.tabs())-1, self.new_tab, text="+")
        self.select(len(self.tabs())-2)
        if self.container.selected_theme=="dark":
            TabFrame.change_tab_theme(DARK, DARK_FONT)
    
    def new_tab_click(self, event):
        try:
            current_index = self.index(f"@{event.x},{event.y}")
            if current_index==self.index(self.new_tab):
                tab = TabFrame(self.container)
                self.add_new(tab)
        except Exception: # _tkinter.TclError
            pass

    def tab_ordering(self, event):
        try:
            insertion_index = self.index(f"@{event.x},{event.y}")
            self.insert(insertion_index, child=self.select())
        except Exception: # _tkinter.TclError
            pass


class TabFrame(ttk.Frame):
    instances = []

    def __init__(self, container):
        super().__init__(container)
        # self.config(padding=1)


        self.text_frame = ttk.Frame(self)

        # self.text_screen = ttk.Text(self.text_frame)
        self.text_screen = st.ScrolledText(
            self.text_frame,
            background=THEME, # make changes somewhere here
            insertbackground=THEME_FONT,
            foreground=THEME_FONT,
            font=TEXT_FONT
        )
        # self.vs = ttk.Scrollbar(self.text_frame, command=self.text_screen.yview)
        # self.text_screen.config(yscrollcommand=self.vs.set)
        
        # self.vs.pack(fill="y", side="right")
        self.text_screen.pack(expand=True, fill="both", side="right")

        self.text_frame.pack(expand=True, fill="both")

        # self.__class__.__name__ = "__main__"
        self.__class__.instances.append(self)
        self.pack(expand=True, fill="both")
    
    @classmethod
    def get_instances(cls):
        return cls.instances

    @classmethod
    def change_tab_theme(cls, theme, theme_font):
        for i in cls.instances:
            i.text_screen.config(
            background=theme,
            insertbackground=theme_font,
            foreground=theme_font,
        )


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