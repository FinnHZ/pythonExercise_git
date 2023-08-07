import tkinter as tk
from tkinter import ttk, DISABLED, NORMAL, W, E, N, S
from PIL import ImageTk    # don't use 'from tkinter import *', install PIL with 'pip install Pillow'
from PIL import Image as ima
from datetime import datetime as dt
import datetime as dts
import calendar



print(dt.now().date().year)
print(dt.now().date().month)
print(dt.now().date().day)


print(dt.now().time().hour)
print(dt.now().time().minute)
print(dt.now().time().second)


print(dt.now().weekday())   #0-6  -->  Mon-Sun
print(dts.date(2023, 3, 1))   
print(dts.date(2023, 3, 1).isoweekday())   #1-7  -->  Mon-Sun


print(calendar.day_name[dts.date(2023, 3, 1).weekday()])   #0-6  -->  Mon-Sun