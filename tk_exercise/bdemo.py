import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askdirectory, askopenfilename
from module.testfunc import progressfunc,getPath


window = tk.Tk()

window.title('demo')

window.geometry('300x200')

window.iconbitmap('./img/favicon.ico')

#window.resizable(0,0)


label_text = tk.StringVar()
label_path = ttk.Label(window, textvariable=label_text)
#label_path = tk.Label(window, textvariable=label_text, font=('Arial',10))
button_path = ttk.Button(window, text="Get Path",style='',command=lambda:getPath(label_text))
# button_path = tk.Button(window, text="Get Path", bg="white", fg="black", font=('Arial',10), width=10, height=1,command=lambda:getPath(label_text))
label_path.place(x=10, y=20)
button_path.place(x=10, y=45)


frame = ttk.Frame()
pd = ttk.Progressbar(frame, length=200, mode='determinate')
frame.place(x=10, y=70)
pd.pack()

buttontext = tk.StringVar()
buttontext.set('Start')
button_pro = tk.Button(window, textvariable=buttontext, bg="white", fg="black", font=('Arial',10), width=20, height=1, command=lambda: progressfunc(pd,buttontext))
button_pro.place(x=10, y=95)






window.mainloop()