# the first method  I used to implement the "+" button
# on the right of the last tab that adds new untitled tab


# class MainNotebook(ttk.Notebook):
#     def __init__(self, container):
#         super().__init__(container)
#         self.container = container

#         self.new_tab = TabFrame(self)
#         self.insert(len(self.tabs()), self.new_tab, text="+")

#         self.bind("<Button-1>", self.new_tab_click)
#         self.bind("<Button1-Motion>", self.tab_ordering)
#         self.pack(expand=True, fill="both")
    
#     def add_tab(self, tab: TabFrame(), label: str="untitled", **kwargs):
#         self.add(tab, text=label, **kwargs)
#         self.insert(len(self.tabs())-1, self.new_tab, text="+")
#         self.select(len(self.tabs())-2) # self.select(len(self.tabs())-1)
#         if self.container.selected_theme=="dark":
#             TabFrame.change_tab_theme(app.DARK, app.DARK_FONT)

#     # ...

#     def new_tab_click(self, event):
#         try:
#             current_index = self.index(f"@{event.x},{event.y}")
#             if current_index==self.index(self.new_tab):
#                 tab = TabFrame(self)
#                 self.add_new(tab)
#         except Exception: # _tkinter.TclError
#             pass