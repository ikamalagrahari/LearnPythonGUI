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

root = PanedWindow()
root.pack(fill=BOTH, expand=1)

leftData = Label(root, text="Hello Python Coders !") #can not be hide
root.add(leftData)

pw2 = PanedWindow(root, orient=VERTICAL)
root.add(pw2)

topData = Label(pw2,text='Python GUI') #can be hide
pw2.add(topData)

bottomData = Label(pw2, text="Python Is Good Language") #can be hide
pw2.add(bottomData)



mainloop()
