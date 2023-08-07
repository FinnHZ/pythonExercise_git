import tkinter as tk
from module.testfunc import clickMe



# create a instance for a tk window
window = tk.Tk()

# set the title name of a window
window.title("second window")

# set the size of the window
window.geometry("500x500")

# create a string variable to get the result of funciton clickMe()
# testVar = tk.StringVar()
testVar = tk.StringVar()
# create a label 
label_test = tk.Label(window, textvariable=testVar, bg="red", fg="white", font=('Arial',12), width=30, height=2)

# set the postion of the label
label_test.place(x=10, y=10)



clickFlag = False
# a function for the click button 
def clickMe():
    global clickFlag
    if clickFlag == False:
        testVar.set('this is a test')
        clickFlag = True
    else:
        testVar.set('')
        clickFlag = False

# createa a button and give the function 'clickMe' as the function when user click 
button_test = tk.Button(window, text="click me", bg="white", fg="black", font=('Arial',12), width=30, height=2, command=clickMe)
button_test.place(x=10,y=40)


# make app work.
window.mainloop()