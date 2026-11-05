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

        self.notebook.bind("<<NotebookTabChanged>>", self.notebook.new_tab_handle)


        self.tab1 = TabFrame(self)
        self.notebook.add(self.tab1, text="untitled")
        
        self.tab2 = TabFrame(self)
        self.notebook.add(self.tab2, text="untitled1")

        i = 1.0
        for tab in self.notebook.tabs():
            
            self.tab1.text_screen.insert(i, f"{tab}\n")
            i += 1
        
        self.tab1.text_screen.insert(i+1, len(self.notebook.tabs()))


        self.bind("q", lambda e: self.destroy())


class MainNotebook(ttk.Notebook):
    def __init__(self, container):
        super().__init__(container)
        self.container = container

        self.bind("<ButtonPress-1>", self.on_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_close_release)

        self.pack(expand=True, fill="both")
    
    def new_tab_handle(self, event):
        if self.select() == self.tabs()[-1]:
            index = len(self.tabs())
            new_tab = TabFrame(self.container)
            self.insert(index, new_tab, text="+")
            self.tab(index-1, text=f"untitled{index-1}")
            self.select(index-1)
    
    def on_close_press(self, event):
        element = self.identify(event.x, event.y)

        if "close" in element:
            index = self.index("@%d,%d" % (event.x, event.y))
            self.state(['pressed'])
            self._active = index
            return "break"

    def on_close_release(self, event):
        tab = self.select(len(self.tabs())-2)
        self.forget(tab)


class TabFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.s = ttk.Style()
        # self.s.element_create("close", "from", "default")


        self.images = (
            tk.PhotoImage("img_close", data='''
                R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
                '''),
            tk.PhotoImage("img_closeactive", data='''
                R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
                AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
                '''),
            tk.PhotoImage("img_closepressed", data='''
                R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
            ''')
        )
        self.s.element_create("close", "image", "img_close",
            ("active", "pressed", "!disabled", "img_closepressed"),
            ("active", "!disabled", "img_closeactive"))
        self.s.layout("TNotebook", [("TNotebook.client", {"sticky": "nswe"})])
        self.s.layout("TNotebook.Tab", [
            ("TNotebook.tab", {
                "children": [
                    ("TNotebook.padding", {
                        "children": [
                            ("TNotebook.focus", {
                                "children": [
                                    ("TNotebook.label", {"side": "left", "sticky": ''}),
                                    ("TNotebook.close", {"side": "left", "sticky": ''}),
                                ]
                        })
                    ]
                    }) ]
            }) ])
        self.s.layout("TNotebook", [])
        self.s.configure("TNotebook", tabmargins=0)
        self.s.configure("TFrame", background="lightgray")
        # self.config(padding=1)


        self.text_frame = ttk.Frame(self)

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