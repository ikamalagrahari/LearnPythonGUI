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

def getGender():
    output = "Your Gender is : " + str(var.get())
    label.config(text=output)


root= Tk()
var = StringVar()

male = Radiobutton(root, text="Male" , variable=var , value="Male", command=getGender )
male.pack(anchor= W)

female = Radiobutton(root, text="Female" , variable=var , value="Female", command=getGender )
female.pack(anchor= W)

other = Radiobutton(root, text="Other" , variable=var , value="Other", command=getGender )
other.pack(anchor= W)

label = Label(root)
label.pack()


root.title("RadioButton Exampl")
root.mainloop()