# import tkinter
import tkinter as tk
from module.testfunc import clickMe, clickMe2

# make window instance
window = tk.Tk()

# give it a name
window.title('test_tkinter')

# define the size of the window
window.geometry('500x300')


testVar = tk.StringVar()
label_test = tk.Label(window, textvariable=testVar, bg="red", fg="white", font=('Arial',12), width=30, height=2)
label_test.place(x=10, y=10)


button_test = tk.Button(window, text="click me", bg="white", fg="black", font=('Arial',12), width=30, height=2, command=lambda:clickMe(testVar))
button_test.place(x=10,y=40)







# make it run through loop
window.mainloop()

