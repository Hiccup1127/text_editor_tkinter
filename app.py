import tkinter as tk
import tkinter.ttk as ttk
import ttkbootstrap as ttk


class Application(tk.Tk):
    def __init__(self, title="Text editor"):
        super().__init__()
        self.title(title)
        self.geometry("700x600")


def main():
    app = Application()
    app.mainloop()


if __name__=="__main__":
    main()