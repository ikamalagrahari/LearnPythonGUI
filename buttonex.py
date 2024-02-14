try :
    from Tkinter import *
except ImportError :
    from tkinter import *

try :
     import ttk
     py3 = False

except ImportError :
     import tkinter.ttk as ttk
     py3 = True

     root= Tk()
     def show():
           print("Ok Button was Clicked...")
     buttonok = Button(root)
     buttonok.place(relx= 0.18 , rely=0.17 , relheight=0.20 , relwidth=0.50)
     buttonok.configure(activebackground="#000000")
     buttonok.configure(background="#aeaeae")
     buttonok.configure(text="ok")
     buttonok.configure(command=show)

     root.title("button exp ")

     root.mainloop()