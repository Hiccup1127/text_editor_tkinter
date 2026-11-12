import tkinter as tk
import ttkbootstrap as ttk
import tkinter.scrolledtext as st

import tkinter.font as tkfont

import app


class MainNotebook(ttk.Notebook):
    def __init__(self, container):
        super().__init__(container)
        self.container = container
        self.bind("<Button1-Motion>", self.tab_ordering)
        self.pack(expand=True, fill="both")
    
    def add_tab(self, tab: TabFrame(), label: str="untitled"):
        self.add(tab, text=label)
        self.select(len(self.tabs())-1)
        if self.container.selected_theme=="dark":
            TabFrame.change_tab_theme(app.DARK, app.DARK_FONT)

    def change_tab(self, label: str="untitled"):
        current_tab_head = self.tab(self.select(), text=label)
        current_tab_head["text"] = label

    def close_tab(self):
        tab = self.get_selected()
        TabFrame.delete_instance(tab.tab_id)
        self.forget(self.index(self.select()))
    
    def get_selected(self):
        try:
            tab_id = self.select()[-1]
            if str.isalpha(tab_id):
                tab_id = "1"
            return TabFrame.get_instance(int(tab_id))
        except IndexError:
            raise IndexError("All the tabs are gone.")

    def tab_ordering(self, event):
        try:
            tab = self.get_selected()
            insertion_index = self.index(f"@{event.x},{event.y}")
            self.insert(insertion_index, child=self.select())
            tab.tab_position = insertion_index
        except Exception: # _tkinter.TclError
            pass


class TabFrame(ttk.Frame):
    instances = []

    def __init__(self, container, tab_name="untitled"):
        super().__init__(container)

        index_before_last = str(self)[-1:]
        if str.isalpha(index_before_last):
            index_before_last = "1"
        self.tab_id = index_before_last
        self.tab_name = tab_name
        self.tab_position = len(container.tabs())
        self.tab_file_path = None

        self.__class__.instances.append(
            (self, self.tab_name, self.tab_id, self.tab_position))

        font = tkfont.Font(font=app.TEXT_FONT)
        tab_width = font.measure("  " * 4)
        self.text_frame = ttk.Frame(self)
        self.text_screen = st.ScrolledText(self.text_frame,
            background=app.LIGHT,
            insertbackground=app.LIGHT_FONT,
            foreground=app.LIGHT_FONT,
            font=app.TEXT_FONT,
            undo=True,
            tabs=tab_width,
        )
        self.text_screen.pack(expand=True, fill="both", side="right")
        self.text_frame.pack(expand=True, fill="both")


        self.pack(expand=True, fill="both")

    @classmethod
    def get_all_instances(cls):
        return cls.instances
    
    @classmethod
    def get_instance(cls, index:int)->bool:
        try:
            for link, name, id, pos in cls.instances:
                if int(id)==int(index):
                    return link
            return False
        except ValueError:
            return "Got an unexpected argument."

    @classmethod
    def delete_instance(cls, index:int)->bool:
        try:
            for a in cls.instances:
                if int(a[2])==int(index):
                    cls.instances.remove(a)
                    return True
            return False
        except ValueError:
            return "Got an unexpected argument."

    @classmethod
    def change_tab_theme(cls, theme, theme_font):
        for link, name, id, pos in cls.instances:
            link.text_screen.config(
            background=theme,
            insertbackground=theme_font,
            foreground=theme_font,
        )