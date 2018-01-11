import tkinter

root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
print("Width: %s, Height: %s" % (width, height))

'''
from screeninfo import get_monitors

width=get_monitors()[0].width
height=get_monitors()[0].height

print("Width: %s,  Height: %s" % (width, height))
'''
