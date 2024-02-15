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

    var = StringVar()
    var1 = StringVar()
    var2 = StringVar()

    text1 = Label(root, textvariable=var, relief=RAISED)
    var.set("Hello ! Python GUI Learners")
    text1.pack()

    text2 = Label(root, textvariable=var1, relief=RAISED)
    var1.set("Hello ! Developers ")
    text2.pack()

    text3 = Label(root, textvariable=var1, relief=RAISED)
    var2.set("Hello ! Programmers ")
    text3.pack()
    root.title("Label Example")
    root.mainloop()
