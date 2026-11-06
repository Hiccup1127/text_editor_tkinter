import tkinter as tk
import tkinter.ttk as ttk
import ttkbootstrap as ttk
import tkinter.scrolledtext as st


class Application(tk.Tk):
    def __init__(self, title="Text editor"):
        super().__init__()
        self.title(title)
        self.geometry("700x600")


        self.notebook = MainNotebook(self)

        self.tab1 = TabFrame(self)
        self.notebook.add_new(self.tab1, "new")


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
        current_index = self.index(f"@{event.x},{event.y}")
        if current_index==self.index(self.new_tab):
            tab_to_add = TabFrame(self)
            self.add_new(tab_to_add)
            self.insert(len(self.tabs())-1, self.new_tab, text="+")
    
    def tab_ordering(self, event):
        insertion_index = self.index(f"@{event.x},{event.y}")
        self.insert(insertion_index, child=self.select())


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


def main():
    app = Application()
    app.mainloop()


if __name__=="__main__":
    main()