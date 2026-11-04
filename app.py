import tkinter as tk
import tkinter.ttk as ttk
import ttkbootstrap as ttk


class Application(tk.Tk):
    def __init__(self, title="Text editor"):
        super().__init__()
        self.title(title)
        self.geometry("700x600")

        self.tab1 = TabFrame(self)

        self.bind("q", lambda e: self.destroy())


class TabFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.s = ttk.Style()
        self.s.configure("TFrame", background="lightgreen")
        self.config(padding=1)


        self.text_frame = ttk.Frame(self)

        self.text_screen = ttk.Text(self.text_frame)
        self.vs = ttk.Scrollbar(self.text_frame, command=self.text_screen.yview)
        self.text_screen.config(yscrollcommand=self.vs.set)
        
        self.vs.pack(fill="y", side="right")
        self.text_screen.pack(expand=True, fill="both", side="right")

        self.text_frame.pack(expand=True, fill="both")


        # self.btn = ttk.Button(self, text="Submit", command=None)
        # self.btn.pack(fill="x")


        self.pack(expand=True, fill="both")


def main():
    app = Application()
    app.mainloop()


if __name__=="__main__":
    main()