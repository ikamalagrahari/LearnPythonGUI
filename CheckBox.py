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

    CheckVar1 = IntVar()
    CheckVar2 = IntVar()
    CheckVar3 = IntVar()

    c1 = Checkbutton(root, text="Dancing", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=20)
    c2 = Checkbutton(root, text="Singing", variable=CheckVar2, onvalue=1, offvalue=0, height=5, width=20)
    c3 = Checkbutton(root, text="Reading", variable=CheckVar3, onvalue=1, offvalue=0, height=5, width=20)

    c1.pack()
    c2.pack()
    c3.pack()

    root.title("CheckBox Example")
    root.mainloop()
