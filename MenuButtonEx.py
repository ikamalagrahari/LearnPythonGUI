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

    menubutton = Menubutton(root, text="DropDown")
    menubutton.grid()
    menubutton.menu = Menu(menubutton, tearoff=0)
    menubutton["menu"] = menubutton.menu

    fileVar = IntVar()
    editVar = IntVar()
    helpVar = IntVar()
    saveVar = IntVar()

    menubutton.menu.add_checkbutton(label="File", variable=fileVar)
    menubutton.menu.add_checkbutton(label="Edit", variable=editVar)
    menubutton.menu.add_checkbutton(label="Save", variable=saveVar)
    menubutton.menu.add_checkbutton(label="Help", variable=helpVar)

    menubutton.pack()

    root.title("MenuButton Example")
    root.mainloop()
