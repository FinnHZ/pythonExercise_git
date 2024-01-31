import tkinter as tk
from tkinter import ttk, Canvas, Scrollbar,VERTICAL, HORIZONTAL, N, S, E, W, messagebox, DISABLED, NORMAL
import time
import threading
import struct
import ctypes
import inspect
import datetime
import winreg


################ initial part----------------------------------------------------------------------------------
root = tk.Tk()
root.state("zoomed")


widthScreen = root.winfo_screenwidth()
heightScreen = root.winfo_screenheight()


displayPageMax = 18
unitWidth = widthScreen / displayPageMax
unitHeight = heightScreen / displayPageMax




################ function part----------------------------------------------------------------------------------
class OperateExp:
    def __init__(self) -> None:
        self.itemsNum = 0
        self.itemDict = []


    def addItems(self, rootName):
        self.itemsNum += 1

        itemMax = displayPageMax-2 # - 2 :    this 2 is for the two orientation arrows at top/bottom
        if self.itemsNum > itemMax:
            morerRange = self.itemsNum - itemMax
            displayScrollCanvas.configure(scrollregion=(0, 0, 0, (displayPageMax+morerRange)*int(unitHeight)))  #scrollregion=(w, n, e, s) , 'e' is not important here becuase we don't have horizontal scroll-- >A tuple (w, n, e, s) that defines over how large an area the canvas can be scrolled, where w is the left side, n the top, e the right side, and s the bottom.
            displayScrollCanvas.itemconfig(scrollItemWindows, height = (displayPageMax+morerRange)*int(unitHeight)) # update the height of show range for the window from canvas_paras.create_window
        
        backgColor = "red"
        
        if self.itemsNum % 2 == 0:
            backgColor = "white"

        testItem = tk.Label(rootName, text=str(self.itemsNum) ,background = backgColor)
        testItem.place(x = 0, y = (self.itemsNum-1)*int(unitHeight), width = 9*int(unitWidth), height = int(unitHeight))
        self.itemDict.append(testItem)


    def delItems(self):
        self.itemsNum -= 1
        
        itemMax = displayPageMax -1  # - 2 :    this 2 is for the two orientation arrows at top/bottom
        if self.itemsNum <= itemMax:
            displayScrollCanvas.configure(scrollregion=(0, 0, 0, (displayPageMax-1)*int(unitHeight)))
            displayScrollCanvas.itemconfig(scrollItemWindows, height = (displayPageMax-1)*int(unitHeight))
        else:
            lessRange = itemMax - self.itemsNum
            displayScrollCanvas.configure(scrollregion=(0, 0, 0, (displayPageMax-lessRange)*int(unitHeight)))
            displayScrollCanvas.itemconfig(scrollItemWindows, height = (displayPageMax-lessRange)*int(unitHeight))
        
        delObj = self.itemDict.pop(-1)
        delObj.destroy()
        


################ scroll part----------------------------------------------------------------------------------
displayScrollFrame = tk.Frame(root, background = "red") #, background = "red"
displayScrollFrame.place(x = 0, y = 0, width = 9*int(unitWidth), height = displayPageMax*int(unitHeight))

displayScrollCanvas = Canvas(displayScrollFrame, width = 9*int(unitWidth), height = displayPageMax*int(unitHeight), scrollregion=(0, 0, 9*int(unitWidth), (displayPageMax)*int(unitHeight)), background="white", relief="raised")
displayScrollCanvas.place(x=0, y=0)

scrollItemsFrame = tk.Frame(displayScrollCanvas, background = "yellow") #, background = "yellow"
displayVerScroll = Scrollbar(displayScrollCanvas, orient = VERTICAL)
displayVerScroll.place(x = 9*int(unitWidth)-20, y = 0, width = 20, height = displayPageMax*int(unitHeight))
displayVerScroll.configure(command = displayScrollCanvas.yview)
displayScrollCanvas.config(yscrollcommand = displayVerScroll.set)
scrollItemWindows = displayScrollCanvas.create_window(-1, -2, window = scrollItemsFrame, anchor="nw", width = 9*int(unitWidth)-20, height = displayPageMax*int(unitHeight))



opIns = OperateExp()


addBtn = tk.Button(root, text = "Add", background="green", command=lambda r=scrollItemsFrame: opIns.addItems(r))
addBtn.place(x = 9*int(unitWidth), y = 0, width = 9*int(unitWidth), height = (displayPageMax/2)*int(unitHeight))

deleteBtn = tk.Button(root, text = "Del", background="blue", command=lambda: opIns.delItems())
deleteBtn.place(x = 9*int(unitWidth), y = (displayPageMax/2)*int(unitHeight), width = 9*int(unitWidth), height = (displayPageMax/2)*int(unitHeight))




















root.mainloop()