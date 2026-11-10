### The actual problem here:


__name__ attribute of the class' instances from different modules
was different.

That caused the issue in the theme toggle menu implementation.

The solution in the actual code was separating the code that initializes
the main tab frame and it's notebook widget into a singe file.


When I initialise a TabFrame from app.py which is a main script in the project,
the object of it is saved with __main__ attribute of its module name(__name__),
it looks like this: 

`<__main__.TabFrame object ...>`

It produces inisde the new_tab_click() method of my MainNotebook class

(it's my implementation of the "+" button that adds a new tab in right
of all the existing tabs, regular mechanism of the most lightweight
modern text editors)

```

class MainNotebook(ttk.Notebook):
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        # ...
    
    def add_new(self, tab: TabFrame(), tabname: str="untitled", **kwargs):
        self.add(tab, text=tabname, **kwargs)
        # ...
    
    def new_tab_click(self, event):
        try:
            current_index = self.index(f"@{event.x},{event.y}")
            if current_index==self.index(self.new_tab):
                tab = TabFrame(self.container)  # <--- this line
                self.add_new(tab)
        except Exception: # _tkinter.TclError
            pass

```

When I do the same but the initialization of the object comes in top_menu.py,
its __name__ attribute sets to 'app' by default(which is the name of
the app.py module).

`<app.TabFrame object>`

It's producing here

```

class MainMenu(ttk.Menu):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        self.container = container

        self.file_menu = tk.Menu(self, bg=THEME, fg=THEME_FONT)
        self.add_cascade(label="File", menu=self.file_menu)

        def new_file():
            tab = TabFrame(container) # <--- this line.
            container.notebook.add_new(tab)
        self.file_menu.add_command(label="New file...", command=new_file)
        # ...

```

When I placed all the TabFrame and Notebook code into single separated file
the initialization process started assigning the name of the module
(notebook.py) to the __name__ attribute for all the instances of the
TabFrame class regardless of the place in the code where it's called.

And considering this, iteration through all the instances has become
much easier.





this is the full code of the old version of app.py

```

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
        print(TabFrame.get_instances())
    
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
        # self.__class__.instances.append(self)
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


```


this is the full code of the old version of top_menu.py

```

import tkinter as tk
import ttkbootstrap as ttk
from app import *
import filedialogs as f


class MainMenu(ttk.Menu):
    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        self.container = container

        self.file_menu = tk.Menu(self, bg=THEME, fg=THEME_FONT)
        self.add_cascade(label="File", menu=self.file_menu)

        def new_file():
            tab = TabFrame(container)
            container.notebook.add_new(tab)
        self.file_menu.add_command(label="New file...", command=new_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Open file...", command=self.open_file)
        self.file_menu.add_command(label="Open folder...", command=self.open_folder)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save")
        self.file_menu.add_command(label="Save As...")
        self.file_menu.add_command(label="Close file")

        self.edit_menu = tk.Menu(self, bg=THEME, fg=THEME_FONT)
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

    # def set_theme(self, theme, theme_font, theme_hover, theme_selected):
    #     style = ttk.Style()
        
    #     style.layout("TNotebook", [])
    #     style.configure("TNotebook", background=theme, foreground=theme_font)
    #     style.configure("TNotebook", tabmargins=0)
    #     style.configure("TNotebook.Tab", background=theme, foreground=theme_font)
    #     style.map("TNotebook.Tab",
    #         background=[("active", theme_hover),
    #                     ("selected", theme_selected)],
    #         foreground=[("selected", theme_font)]
    #     )
    #     style.configure("TLabel", background=theme, foreground=theme_font)
    #     style.configure("TFrame", background=theme)
    #     style.configure("Treeview", background=theme)
    #     style.configure("separator1.TFrame", background=theme_font)

    #     for tab in TabFrame.get_instances():
    #         tab.text_screen.config(
    #             background=theme,
    #             insertbackground=theme_font,
    #             foreground=theme_font,
    #         )

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

        self.container.selected_theme == "light"
    
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

        self.container.selected_theme == "dark"

    def open_file(self):
        path = f.get_file()
        file = open(path.name, "r")

        file_name = path.name.split("/")[-1]
        
        
        self.container.tab = TabFrame(self.container)
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
        # print(self.folder, self.folder_data)

```