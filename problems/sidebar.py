# It's a sidebar that I just didn't want to complete :(


# import os
# from os import walk


# s = ttk.Style()
# s.layout("TNotebook", [])
# s.configure("TNotebook", background=theme, foreground=theme_font)
# s.configure("TNotebook", tabmargins=0)
# s.configure("TNotebook.Tab", background=theme, foreground=theme_font)
# s.map("TNotebook.Tab", background=[("active", theme_hover),
#                                 ("selected", theme_selected)],
#                     foreground=[("selected", theme_font)])
# s.configure("TLabel", background=theme, foreground=theme_font)
# s.configure("TFrame", background=theme)
# s.configure("Treeview", background=theme,foreground=theme_font,           #
#                         font=("Calibri", 11))                             #
# s.configure("Treeview.Heading", background=LIGHT, foreground=LIGHT_FONT)  #
# s.map("Treeview", background=[("selected", LIGHT_SELECTED)],              #
#                   foreground=[("selected", LIGHT_FONT)])                  #
# s.configure("separator1.TFrame", background=LIGHT_FONT)                   #
# TabFrame.change_tab_theme(theme, theme_font)


# class Sidebar(ttk.Frame):
#     def __init__(self, container):
#         super().__init__(container)
#         self.container = container
#         self.width = 250
#         self.config(width=self.width)
#         self.pack_propagate(0)


#         self.main_container = ttk.Frame(self)
#         self.main_container.pack(side="left", expand=1, fill="both")

#         self.title = ttk.Label(self.main_container, font="Calibri 16", text="OPEN FILES")
#         self.title.pack(fill="x", pady=(0, 15))


#         self.separator = ttk.Frame(self,
#             cursor="plus",
#             width=2,
#             style="separator1.TFrame"
#         )
#         self.separator.pack(side="left", expand=0, fill="y")
#         self.separator.pack_propagate(0)
#         self.separator.bind("<Button1-Motion>", self.resize)


#         self.pack(side="left", fill="both", expand=0)

#     def resize(self, event):
#         const_width = 250
#         if event.x > 5:
#             event.x = 3
#             self.width += event.x
#         elif event.x < -5: 
#             event.x = -3
#             self.width += event.x
#         else:
#             self.width += event.x

#         if self.width > 700 or self.width < 220:
#             return;
#         else:
#             self.config(width=self.width)
    
#     current_dir = False

#     def open_directory(self, directory: str):
#         if self.__class__.current_dir:
#             self.forget_directory()
#         self.dir_name = ttk.Label(self.main_container, font="Calibri 14", text=directory["Name"])
#         self.dir_name.pack(fill="x", pady=(0, 10))

#         self.content = ttk.Treeview(self.main_container, columns=("Dir"), show="tree")
#         self.content.column("#0", width=0)
#         self.content.heading("Dir", text="Folder", anchor="w")
            
#         for n, p in directory["Files"]:
#             a = self.content.insert("", 'end', values=(n))


#         self.right_click_menu_on_sidebar = tk.Menu(self.container)
#         self.right_click_menu_on_sidebar.add_command(label="Rename...",
#             command=self.rename_file_in_directory)
#         self.right_click_menu_on_sidebar.add_command(label="Copy path") # implement this

#         self.content.bind("<Button-1>", lambda e: self.content.selection_set(()))
#         self.content.bind("<Button-3>", lambda e:
#             self.right_click_menu_on_sidebar.tk_popup(e.x_root, e.y_root))

#         # TO DO: COPY PATH; RENAME; OPEN BY A CLICK; AND THAT'D BE THE END!
#         self.xs = tk.Scrollbar(self.main_container,
#         orient="horizontal", command=self.content.xview)
#         self.content.config(xscrollcommand=self.xs.set)
#         self.xs.pack(side="bottom", fill="x")
#         self.content.pack(expand=1, fill="both")

#         self.directory = directory
#         self.__class__.current_dir = True

#     def rename_file_in_directory(self):
#         focused_file = self.content.focus() # implement opening the file by double-click
#         index = int(focused_file[1:])-1
#         print(self.directory["Files"][index]) # complete renaming the files feature
#         x = input("-> ")
#         self.content.insert("", str(focused_file)[1:], values=(x))
#         self.content.delete(focused_file)

#     def forget_directory(self):
#         if not self.__class__.current_dir:
#             return True
#         self.dir_name.pack_forget()
#         self.content.pack_forget()
#         self.__class__.current_dir = False


# class MainMenu(ttk.Menu):
#     def __init__(self, container, **kwargs):
#         super().__init__(container, **kwargs)
        
#         # ...
        
#         self.file_menu.add_command(label="Open folder...", command=self.get_folder)
#         self.file_menu.add_command(label="Close folder", command=self.close_folder)
    
#     def get_folder(self):
#         dir = f.open_folder()
#         self.container.sidebar.open_directory(dir)
    
#     def close_folder(self):
#         dir = f.work_dir
#         dir["Path"] = None
#         dir["Name"] = None
#         dir["Files"] = []
#         self.container.sidebar.forget_directory()


# work_dir = {
#     "Path": None,
#     "Name": None,
#     "Files": [],
# }

# def open_folder(path: str=None):
#     try:
#         if path is None:
#             path = filedialog.askdirectory(
#                 title="Open a folder ...",
#                 initialdir = "C:\\Users\\"
#             )
#         list_of_files = []
#         for i in os.listdir(path):
#             path_to_the_file = os.path.join(path, i)
#             if os.path.isfile(path_to_the_file):
#                 list_of_files.append((i, path_to_the_file.replace("\\", "/")))

#         work_dir["Path"] = path
#         work_dir["Name"] = path.split("/")[-1]
#         work_dir["Files"] = list_of_files

#         return work_dir
#     except Exception as e:
#         print(f"Can't OPEN the directory, {e}")
#         return e;