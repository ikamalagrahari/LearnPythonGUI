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

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)

dataList = Listbox(root, yscrollcommand=scrollbar.set)

for nos in range(100):
    dataList.insert(END , str(nos)+"Welcome Python GUI Developers ! we love programming ")

dataList.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=dataList.yview)


root.title("ScrollBar Example ")
root.mainloop()
