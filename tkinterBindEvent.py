import tkinter
from tkinter import *



def closeEditing(aimObj, aimVal):

    aimVal.set("left click!")
    aimObj.destroy()


def leftClickFunc(event=None, aimObj=None):
    print("left click!")
    popText = Toplevel()
    popText.protocol('WM_DELETE_WINDOW', lambda editBox=popText, boxValue=aimObj: closeEditing(editBox, boxValue))
    



# .bind("<Button-1>", self.commandControl)
# .bind("<Return>", lambda event=None: self.loginVerify_submit(event))
# .bind("<Configure>", self.on_resize)
# self.settingPage.protocol('WM_DELETE_WINDOW', lambda: self.closeCurrentSetting())

root = Tk()
root.geometry("200x200")

testEntVal = StringVar()
testEntry = Entry(root, textvariable = testEntVal)
testEntry.grid(row = 0, column = 0)


testEntVal1 = StringVar()
testEntry1 = Entry(root, textvariable = testEntVal1)
testEntry1.grid(row = 1, column = 0)

testEntry.bind("<Button-1>", lambda event=None, obj=testEntVal: leftClickFunc(event, obj))
testEntry1.bind("<Button-1>", lambda event1=None, obj1=testEntVal1: leftClickFunc(event1, obj1))




root.mainloop()
