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

text = Text(root)
text.insert(INSERT,"Hello Python Coders !")
text.insert(END,"Python GUI is Fun ...")
text.pack()

text.tag_add("add","1.0", "1.8")
text.tag_config("add",background="yellow",foreground="red")

text.tag_add("demo","1.22", "1.30")
text.tag_config("demo",background="aqua",foreground="yellow")

root.title("Text Example ")
root.mainloop()
