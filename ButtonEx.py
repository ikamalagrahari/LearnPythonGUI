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

def show():
    print("Ok Button was Clicked...")

button_ok = Button(root)
button_ok.place(relx=0.18, rely=0.17, relheight=0.20, relwidth=0.50)
button_ok.configure(activebackground="#000000")
button_ok.configure(background="#aeaeae")
button_ok.configure(text="ok")
button_ok.configure(command=show)

root.title("button exp ")

root.mainloop()
