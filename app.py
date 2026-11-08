import tkinter as tk
import tkinter.ttk as ttk
import ttkbootstrap as ttk
import tkinter.scrolledtext as st
import top_menu


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


        self.bind("q", lambda e: self.destroy())


class MainNotebook(ttk.Notebook):
    def __init__(self, container):
        super().__init__(container)

        self.new_tab = TabFrame(self)
        self.insert(len(self.tabs()), self.new_tab, text="+")

        self.bind("<Button-1>", self.new_tab_click)
        self.bind("<Button1-Motion>", self.tab_ordering)
        self.pack(expand=True, fill="both")
    
    def add_new(self, tab: TabFrame(), tabname: str="untitled"):
        self.add(tab, text=tabname)
        self.insert(len(self.tabs())-1, self.new_tab, text="+")
    
    def new_tab_click(self, event):
        try:
            current_index = self.index(f"@{event.x},{event.y}")
            if current_index==self.index(self.new_tab):
                tab_to_add = TabFrame(self)
                self.add_new(tab_to_add)
                self.insert(len(self.tabs())-1, self.new_tab, text="+")
        except Exception: # _tkinter.TclError
            pass

    def tab_ordering(self, event):
        try:
            insertion_index = self.index(f"@{event.x},{event.y}")
            self.insert(insertion_index, child=self.select())
        except Exception: # _tkinter.TclError
            pass


class TabFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.s = ttk.Style()
        self.s.layout("TNotebook", [])
        self.s.configure("TNotebook", tabmargins=0)
        self.s.configure("TFrame", background="lightgray")
        # self.config(padding=1)


        self.text_frame = ttk.Frame(self)

        # self.text_screen = ttk.Text(self.text_frame)
        self.text_screen = st.ScrolledText(self.text_frame)
        # self.vs = ttk.Scrollbar(self.text_frame, command=self.text_screen.yview)
        # self.text_screen.config(yscrollcommand=self.vs.set)
        
        # self.vs.pack(fill="y", side="right")
        self.text_screen.pack(expand=True, fill="both", side="right")

        self.text_frame.pack(expand=True, fill="both")


        self.pack(expand=True, fill="both")


class Sidebar(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.style = ttk.Style()
        self.style.configure("separator1.TFrame", background="green")


        self.main_container = ttk.Frame(self)
        self.main_container.pack(side="left", expand=1, fill="both")

        self.title = ttk.Label(self.main_container, font="Calibri 16", text="Folder")
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