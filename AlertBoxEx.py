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

#import messagebox from tkinter for using it
from tkinter import messagebox

root = Tk()

def msg():

    messagebox.showinfo("Important Message","This is  an example of MessageBox or AlertBox In Python")
    #messagebox has different options  like askquestion , ok , retry, undo, redo

button = Button(root, text="Show Message", command=msg)
button.pack()

root.title("MessageBox or AlertBox Example ")
root.mainloop()