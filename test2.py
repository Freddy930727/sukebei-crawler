from tkinter import *
def ShowMsg():
    for i in checkvalue:
        if checkvalue[i].get() == True:
            print(item[i])
window = Tk()
item= {0:"a", 1:"b",2:"3"}
checkvalue = {}
for i in range(len(item)):
    checkvalue[i] = BooleanVar()
    Checkbutton(window, variable = checkvalue[i], text=item[i])
Checkbutton.pack()
window.mainloop()
