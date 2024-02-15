try :
    from tkinter import *
except ImportError :
    from tkinter import *

try :
     import ttk
     py3 = False

except ImportError :
     import tkinter.ttk as ttk
     py3 = True

     root= Tk()

     root.title("basic frame ")

     root,mainloop()