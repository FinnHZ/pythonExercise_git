import tkinter as tk
from tkinter import *
from tkinter import ttk

class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.state('zoomed')
        self.title("Thermal Application")
        self.resizable(width = False, height = False)
        
        self.width_screen= self.winfo_screenwidth()
        self.height_screen= self.winfo_screenheight()

        self.navPart = Label(self, background="white")
        self.navPart.place(x=0, y=0, width=self.width_screen, height=int(self.height_screen/45))
        
        self.menuTitles = ["Data", "Setting", "Account", "Help"]
        for t in range(0, len(self.menuTitles)):
            self.menuSection(t)


    def menuSection(self, index):
        menuBtn_1 = tk.Menubutton(self.navPart, text=self.menuTitles[index], background="white")
        menuDropDown = Menu(menuBtn_1, tearoff=0, background="white")
        menuListDict = {
            "0": ["Loading..", "Save", "Upload", "Download"],
            "1": ["Setting**", "Options**"],
            "2": ["Create account", "Change password", "Adjust permissions", "Log In", "Log out"],
            "3": ["Help**", "Contact**", "About.."]
        }
        ttStr = StringVar()
        for m in menuListDict[str(index)]:
            menuDropDown.add_radiobutton (label=m, value=m, variable=ttStr)
        menuBtn_1["menu"] = menuDropDown
        menuBtn_1.grid(column=index, row=0, padx=1)



if __name__ == "__main__":
    app = App()
    app.mainloop()