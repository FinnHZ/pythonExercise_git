import tkinter as tk
from tkinter import ttk, DISABLED, NORMAL, W, E, N, S



root = tk.Tk()
root.geometry("200x200")
root.title("tkinterDynamicAddElement")


addBtn = tk.Button(root, text="Add", command=lambda para="sdsadsad": addDynamic(para))
addBtn.grid(row=0, column=0)



def addDynamic(pa):
    newBtn = tk.Button(root, text="New", command=lambda para="nnenneee": newDynamic(para))
    newBtn.grid(row=1, column=0)


def newDynamic(ne):
    print(ne)



root.mainloop()