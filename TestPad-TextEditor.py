try:
    from tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk

    py3 = False

except ImportError:
    import tkinter.ttk as ttk

    py3 = True

def show():
    filewind = Toplevel(root)
    button = Button(filewind, text="Hello")
    button.pack()

root = Tk()

menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=show)
filemenu.add_command(label="Open", command=show)
filemenu.add_command(label="Save", command=show)
filemenu.add_command(label="Save As", command=show)
filemenu.add_command(label="Exit", command=show)

filemenu.add_separator()

filemenu.add_command(label="Quit", command=show)
menubar.add_cascade(label="File",menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=show)
editmenu.add_separator()
editmenu.add_command(label="Redo",command=show)
editmenu.add_command(label="Copy",command=show)
editmenu.add_command(label="Paste",command=show)
editmenu.add_command(label="Cut",command=show)
editmenu.add_command(label="Delete",command=show)
editmenu.add_command(label="Select All",command=show)

menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar,tearoff=0)
helpmenu.add_command(label="Help Details", command=show)
helpmenu.add_command(label="About TextPad", command=show)
menubar.add_cascade(label="Help", menu=helpmenu)
menubar.add_cascade(label="Help", menu=helpmenu)


root.config(menu=menubar)
root.title("TextPad - Text Editor")
root.mainloop()