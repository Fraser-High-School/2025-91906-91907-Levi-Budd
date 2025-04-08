import tkinter as tk

MyWindow = tk.Tk()
MyWindow.geometry("500x550")

#create LabelFrame (200x200)
label = tk.LabelFrame(MyWindow, width=200, height=200)

#grid manager to set label localization
label.grid(row=0, column=0)

#label row and column configure: first argument is col or row id
label.grid_rowconfigure(0, weight=1)
label.grid_columnconfigure(0, weight=1)

#cancel propagation
label.grid_propagate(False)

#Create button and set it localization. You can change it font without changing size of button, but if You set too big not whole will be visible
button = tk.Button(label, text="Hello!", font=('Helvetica', '20'))

#Use sticky to button took up the whole label area
button.grid(row=0, column=0, sticky='nesw')

MyWindow.mainloop()





