
try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

root = Tk()

text = StringVar()
label = Message(root, textvariable=text, relief=RAISED )
text.set("Hello Python Coders! We love Python programming")


text = StringVar()
label2 = Message(root, textvariable=text, relief=RAISED )
text.set("This notes are created while learning the concepts of Tkinter GUI for my Python Mini Project, You can access the codes from my GitHub account @kamalagrahari03  ")

label.pack()
label2.pack()

root.title("Message Example")
root.mainloop()
