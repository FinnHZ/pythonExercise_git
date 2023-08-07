import tkinter as tk
from tkinter import *
import time
import threading
import math


root = tk.Tk()
root.title("instrument design test")
root.geometry("800x600")


radius = 300
width_inter = 800
height_inter = 600
# print(math.radians(1))
# print(math.pi/180)
offsetVal_x = 3
offsetVal_y = 2


def pinDynamically(startAngular, dynamicStart_x, dynamicStart_y):
    while startAngular < 180:
        startAngular += 1
        
        # radiansAngular = math.radians(startAngular)

        # offsetChange_x = radius*(1-math.cos(radiansAngular))
        # offsetChange_y = radius*math.sin(radiansAngular)

        dynamicEnd_x = 0
        dynamicEnd_y = 0
        
        if startAngular < 90:
            dynamicEnd_x = dynamicStart_x - offsetVal_x/2 - radius*math.cos(math.radians(startAngular))
            dynamicEnd_y = dynamicStart_y - offsetVal_y/2 - radius*math.sin(math.radians(startAngular))
        elif startAngular >= 90 and startAngular <= 180:
            if startAngular == 90:
                print(math.radians(startAngular))


            dynamicEnd_x = dynamicStart_x - offsetVal_x - radius*math.cos(math.radians(startAngular))
            dynamicEnd_y = dynamicStart_y - offsetVal_y - radius*math.sin(math.radians(startAngular))
            if startAngular == 90:
                print(dynamicEnd_x, dynamicEnd_y)
                print(math.cos(math.radians(startAngular)), math.sin(math.radians(startAngular)))

        
        canvas_paras.coords(pinPoint, dynamicStart_x, dynamicStart_y, dynamicEnd_x, dynamicEnd_y)
        
        
        time.sleep(0.05)
        # print(dynamicEnd_x)
    




paraSetArea = tk.Frame(root, width = width_inter, height = height_inter)
paraSetArea.place(x = 0, y = 0)

canvas_paras = Canvas(paraSetArea, width = height_inter, height = radius, background="red")
canvas_paras.place(x = 50, y = 50,)

semicircle = canvas_paras.create_arc(offsetVal_x, offsetVal_y, height_inter, height_inter, start=180, extent=-180, fill="yellow") #



initialStart_x = radius+offsetVal_x
initialStart_y = radius+offsetVal_y
initialEnd_x = initialStart_x - radius*math.cos(math.radians(0))
initialEnd_y = initialStart_y - radius*math.sin(math.radians(0))


pinPoint = canvas_paras.create_line(initialStart_x, initialStart_y, initialEnd_x, initialEnd_y)

# pinPoint = canvas_paras.create_line(initialStart_x, initialStart_y, initialStart_x, 0)

pinThread = threading.Thread(target=pinDynamically, args=(0, initialStart_x, initialStart_y)) #
pinThread.start()




root.mainloop()