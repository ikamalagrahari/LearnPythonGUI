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

#LOGIN PAGE

    frame =Frame(root)
    label = Label(frame, text="Username :")
    label.pack(side=LEFT)

    entry = Entry(frame, bd=5)
    entry.pack(side=LEFT)
    frame.pack()

    frame2 = Frame(root)
    label2 = Label(frame2, text="Password :")
    label2.pack(side=LEFT)

    password = Entry(frame2, bd=5)
    password.pack(side=LEFT)
    frame2.pack() #Can USE LEFT RIGHT TOP BOTTOM FOR ADUSTING LABEL AND ENTRY
                  # frame2.pack(side=LEFT)

    root.title("Entry Example")
    root.mainloop()