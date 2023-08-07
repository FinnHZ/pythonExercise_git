from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Menu bar test")
root.geometry("500x500")


menuBar = ttk.Menubutton(root, text="File")   #tk.Menu(root)
mm = Menu(menuBar, tearoff=0)


colors = ["red", "green", "blue"]
ttStr = StringVar()
for c in colors:
    mm.add_radiobutton (label=c, value=c, variable=ttStr)

menuBar["menu"] = mm
menuBar.pack(expand=True)


def changeTT(*args):
    print(ttStr.get())
    small = Toplevel()
    
    small.config(background=ttStr.get())
    

ttStr.trace("w", changeTT)

root.mainloop()
#***************************************************************************************
# mainPanel.config(menu = menuBar)
    
# menuBar.fileMenu = tk.Menu(menuBar, name = "fileMenu")
# menuBar.add_cascade(label = "File",menu = menuBar.fileMenu)
# menuBar.fileMenu.add_command(label = "File", command = doNothing)

# menuBar.exitMenu = tk.Menu(menuBar, name = "exitMenu")
# menuBar.add_cascade(label = "Exit",menu = menuBar.exitMenu)
# menuBar.exitMenu.add_command(label = "Exit", command = clientExit)



#***************************************************************************************

# import tkinter as tk
# from tkinter import ttk


# class App(tk.Tk):
#     def __init__(self):
#         super().__init__()

#         self.geometry('300x250')
#         self.title('Menubutton Demo')

#         # Menubutton variable
#         self.selected_color = tk.StringVar()
#         self.selected_color.trace("w", self.menu_item_selected)

#         # create the menu button
#         self.create_menu_button()

#     def menu_item_selected(self, *args):
#         """ handle menu selected event """
#         self.config(bg=self.selected_color.get())

#     def create_menu_button(self):
#         """ create a menu button """
#         # menu variable
#         colors = ('Red', 'Green', 'Blue')

#         # create the Menubutton
#         menu_button = ttk.Menubutton(
#             self,
#             text='Select a color')

#         # create a new menu instance
#         menu = tk.Menu(menu_button, tearoff=0)

#         for color in colors:
#             menu.add_radiobutton(
#                 label=color,
#                 value=color,
#                 variable=self.selected_color)

#         # associate menu with the Menubutton
#         menu_button["menu"] = menu

#         menu_button.pack(expand=True)


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()