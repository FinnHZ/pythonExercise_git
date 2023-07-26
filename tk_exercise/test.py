from tkinter import *


def test111(event=None):
    print("successful")


root = Tk()

root.geometry("500x500")

root.bind("<Alt-s>",test111)


root.mainloop()