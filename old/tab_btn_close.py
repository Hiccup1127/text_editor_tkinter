# Uncolmleted mechanism of closing button in notebook widget


# class MainNotebook(ttk.Notebook):
#     def __init__(self, container):
#         super().__init__(container)
#         self.container = container
        
#         self.bind("<ButtonPress-1>", self.on_close_press, True)
#         self.bind("<ButtonRelease-1>", self.on_close_release)

#         self.pack(expand=True, fill="both")

#     def on_close_press(self, event):
#         element = self.identify(event.x, event.y)

#         if "close" in element:
#             index = self.index("@%d,%d" % (event.x, event.y))
#             self.state(['pressed'])
#             self._active = index
#             return "break"

#     def on_close_release(self, event):
#         """Called when the button is released"""
#         if not self.instate(['pressed']):
#             return

#         element =  self.identify(event.x, event.y)
#         if "close" not in element:
#             # user moved the mouse off of the close button
#             return

#         index = self.index("@%d,%d" % (event.x, event.y))

#         if self._active == index:
#             self.forget(index)
#             self.event_generate("<<NotebookTabClosed>>")

#         self.state(["!pressed"])
#         self._active = None
        
#         if "close" in element:
#             print(tab)
#             self.forget(tab)


# class TabFrame(ttk.Frame):
#     def __init__(self, container):
#         super().__init__(container)
#         self.s = ttk.Style()
    
#     self.images = (
#             tk.PhotoImage("img_close", data='''
#                 R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
#                 d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
#                 5kEJADs=
#                 '''),
#             tk.PhotoImage("img_closeactive", data='''
#                 R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
#                 AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
#                 '''),
#             tk.PhotoImage("img_closepressed", data='''
#                 R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
#                 d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
#                 5kEJADs=
#             ''')
#         )
    
#     print(self.s.layout("TNotebook.Tab")) - to see what's needed
#     self.s.element_create("close_btn", "image", tk.PhotoImage(file="./icons/close-button.png"))
    
#     doesn't work(my attempt)
    
#     self.s.layout("TNotebook.Tab", [
#         ('TNotebook.tab', {
#             'sticky': 'nswe',
#             'children': [
#                 ('TNotebook.padding', {
#                     'sticky': 'nswe',
#                     'children': [
#                         ('TNotebook.focus', {
#                             'sticky': 'nswe',
#                             'children': [
#                                 ('TNotebook.label', {'sticky': 'nswe'}),
#                                 ("TNotebook.close_btn", {'sticky': 'nswe'})]}
#                         )]}
#                 )]}
#         )])

#     is working(from stackoverflow)

#     self.s.element_create("close", "image", "img_close",
#         ("active", "pressed", "!disabled", "img_closepressed"),
#         ("active", "!disabled", "img_closeactive"))
#     self.s.layout("TNotebook.Tab", [
#         ("TNotebook.tab", {
#             "children": [
#                 ("TNotebook.padding", {
#                     "children": [
#                         ("TNotebook.focus", {
#                             "children": [
#                                 ("TNotebook.label", {"side": "left", "sticky": ''}),
#                                 ("TNotebook.close", {"side": "left", "sticky": ''}),
#                             ]
#                         })
#                 ]
#                 }) ]
#         }) ])