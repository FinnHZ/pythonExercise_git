import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilename


clickFlag = False
# a function for the click button 
def clickMe(testObj):
    global clickFlag
    if clickFlag == False:
        testObj.set('this is a test')
        clickFlag = True
    else:
        testObj.set('')
        clickFlag = False


def clickMe2(testObj):
    testObj.set('this is a test for call funciton')


progressflag = False
def progressfunc(proObj,textOfButton):
    global progressflag
    if progressflag == False:
        proObj.start(25)
        textOfButton.set('Stop')
        progressflag = True
    else:
        proObj.stop()
        textOfButton.set('Start')
        progressflag = False

def getPath(labelStr):
    folderPath = askdirectory()
    labelStr.set(folderPath)