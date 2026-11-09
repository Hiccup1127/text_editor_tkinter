import tkinter as tk
import ttkbootstrap as ttk
import tkinter.scrolledtext as st 

import app, top_menu, filedialogs


class MainNotebook(ttk.Notebook):
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        self.new_tab = TabFrame(self)
        self.insert(len(self.tabs()), self.new_tab, text="+")

        self.bind("<Button-1>", self.new_tab_click)
        self.bind("<Button1-Motion>", self.tab_ordering)
        self.pack(expand=True, fill="both")
    
    def add_new(self, tab: TabFrame(self.container), tabname: str="untitled", **kwargs):
        self.add(tab, text=tabname, **kwargs)
        self.insert(len(self.tabs())-1, self.new_tab, text="+")
        self.select(len(self.tabs())-2)
    
    def new_tab_click(self, event):
        try:
            current_index = self.index(f"@{event.x},{event.y}")
            if current_index==self.index(self.new_tab):
                tab = TabFrame(self.container)
                self.container.notebook.add_new(tab)
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
        self.text_screen = st.ScrolledText(self.text_frame,
            background=app.LIGHT,
            insertbackground=app.LIGHT_FONT,
            foreground=app.LIGHT_FONT,
            font=app.TEXT_FONT
        )
        # self.vs = ttk.Scrollbar(self.text_frame, command=self.text_screen.yview)
        # self.text_screen.config(yscrollcommand=self.vs.set)
        
        # self.vs.pack(fill="y", side="right")
        self.text_screen.pack(expand=True, fill="both", side="right")

        self.text_frame.pack(expand=True, fill="both")


        self.pack(expand=True, fill="both")
        self.__class__.instances.append(self)
    
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
    
    # def __str__(self)->str:
    #     for i in range(len(self.__class__.instances)):
    #         if self.__class__.instances[i]==self:
    #             return f"{i};{self.text_frame}"