import threading
from tkinter import *
import random
import time
import datetime as dt



root = Tk()

root.geometry("500x500")


buttontest =  Button(root, text="start", command=lambda:teststart())
buttontest.pack()

buttontest1 =  Button(root, text="stop", command=lambda:teststop())
buttontest1.pack()

buttontest2 =  Button(root, text="id", command=lambda:getid())
buttontest2.pack()



global runFlag
runFlag =False


def test():
    global runFlag
    runFlag = True

    while runFlag:
        timer_1 = dt.datetime.now()


        temVal = random.randint(0,100)
        time.sleep(1)

        timer_2 = dt.datetime.now()
        duration =float(str(timer_2 - timer_1).split(":")[-1])
        print(temVal, ";", duration)   #############


def teststart():
    global threadFlag
    threadFlag = threading.Thread(target=test)

    print(threadFlag)
    threadFlag.start()

def teststop():
    global runFlag
    runFlag = False
    global threadFlag
    threadFlag.join()
    teststart()
    

def getid():
    global threadFlag
    #print(threading._active.items())
    for id, thread in threading._active.items(): 
        print(id, thread)
    # print(threading._active.items)

root.mainloop()


