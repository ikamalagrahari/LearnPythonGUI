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

    list = Listbox(root)
    list.insert(1, "Python")
    list.insert(2,"Java")
    list.insert(3,"C & C++")
    list.insert(4, "JavaScript")
    list.insert(5, "PHP")
    list.insert(6, "Perl")
    list.insert(4, "Ruby")

    list.pack()

    root.title("ListBox Example")
    root.mainloop()