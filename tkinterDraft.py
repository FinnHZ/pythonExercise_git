import tkinter
from tkinter import *

root = Tk()


def getCon(txtObj):
    txtttt = txtObj.get("1.0","end-1c")
    print(txtttt)


testTxt = Text(root)
testTxt.grid(row=0, column=0)


btnGet = Button(root, text="testGet", command=lambda tObj = testTxt: getCon(tObj))
btnGet.grid(row=1, column=0)


root.mainloop()