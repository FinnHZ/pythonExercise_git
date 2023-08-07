import tkinter as tk
from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = Tk()
root.geometry("500x500")

# fieldtest = ttk.LabelFrame(root, text="fieldtest")
# fieldtest.pack()


s1 = ttk.Scrollbar(root) #, orient=HORIZONTAL
s1.set(0.6, 0)
s1.pack(side="right")




# fig = Figure(figsize=(5,5), dpi=72)
# ax = fig.add_subplot(111)

# ax.plot([1,2,3,4,5,6,7], [1,2,3,4,5,6,7])

# canvas =FigureCanvasTkAgg(fig, master=root)
# canvas.draw()
# canvas.get_tk_widget().pack()








root.mainloop()