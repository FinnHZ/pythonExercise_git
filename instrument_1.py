import tkinter as tk
from tkinter import *
import time
import threading


root = tk.Tk()
root.title("instrument design test")
root.geometry("400x300")

radius = 150


def drawDynamically(startAngular):
    while startAngular > -180:
        startAngular -= 1
        canvas_paras.itemconfig(semicircle, extent = startAngular)
        time.sleep(0.05)
        print(startAngular)
    



paraSetArea = tk.Frame(root, width = 400, height = 300)
paraSetArea.place(x = 0, y = 0)

canvas_paras = Canvas(paraSetArea, width = 300, height = radius, background="red")
canvas_paras.place(x = 50, y = 50)

semicircle = canvas_paras.create_arc(0, 0, radius, radius, start=180, extent=0, fill="yellow") #


drawThread = threading.Thread(target=drawDynamically, args=(0, )) #
drawThread.start()




root.mainloop()