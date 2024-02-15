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

    root = Tk()

    frame = Frame(root)
    frame.pack()

    frame2 = Frame(root)
    frame2.pack(side=BOTTOM)

    filebutton = Button(frame, text="FILE", fg="red")
    filebutton.pack(side=LEFT)

    editbutton = Button(frame, text="EDIT", fg="red")
    editbutton.pack(side=LEFT)

    optionbutton = Button(frame, text="OPTION", fg="red")
    optionbutton.pack(side=LEFT)

    viewbutton = Button(frame, text="OPTION", fg="green")
    viewbutton.pack(side=LEFT)


    root.title("Frame Example")
    root.mainloop()
