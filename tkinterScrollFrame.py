import tkinter as tk
 
root = tk.Tk()
 
# Create a canvas
canvas = tk.Canvas(root, height=200, width=300, background="lightblue")
canvas.pack()
 
# Create a frame
frame = tk.Frame(root, bg="red")
 
# Add the frame to the canvas
canvas.create_window(0, 50, window=frame, anchor="nw")
 
# Add a button to the frame
button = tk.Button(frame, text="Click me!")
button.pack(padx = 20, pady = 20)
 
root.mainloop()