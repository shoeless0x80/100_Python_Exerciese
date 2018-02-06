#Create a program that asks the user to submit text through a GUI

from tkinter import *

data = []

def addLine():
    data.append(entry.get())
    entry.delete(0,END)

def saveChanges():
    print(data)
    with open("98.txt", "a+") as file:
        for i in data:
            file.write(i+"\n")
    del data[:]

def saveAndClose():
    with open("98.txt", "a+") as file:
        for i in data:
            file.write(i+"\n")
    window.destroy()

window = Tk()

entry = Entry(window)
entry.grid(row=0,column=1)

#addLineButton = Button(window,text="Add line",width=12,command=lambda: data.append(entry.get()))
addLineButton = Button(window,text="Add line",width=12,command=addLine)
addLineButton.grid(row=0,column=2)

saveChangesButton = Button(window,text="Save changes",width=12,command=saveChanges)
saveChangesButton.grid(row=0,column=3)

saveAndCloseButton = Button(window,text="Save and Close",width=12,command=saveAndClose)
saveAndCloseButton.grid(row=0,column=4)

window.mainloop()

'''
from tkinter import *

window = Tk()

file = open("user_gui.txt", "a+")

def add():
    file.write(e2_value.get() + "\n")
    entry.delete(0, END)

def save():
    global file
    file.close()
    file = open("user_gui.txt", "a+")

def close():
    file.close()
    window.destroy()

user_value = StringVar()
entry = Entry(window, textvariable=user_value)
entry.grid(row=0, column=0)

button_add = Button(window, text="Add line", command=add)
button_add.grid(row=0, column=1)

button_save = Button(window, text="Save changes", command=save)
button_save.grid(row=0, column=2)

button_close = Button(window, text="Save and Close", command=close)
button_close.grid(row=0,column=3)

window.mainloop()
'''
