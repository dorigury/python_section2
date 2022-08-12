from tkinter import *

def printHello() :
    print('hi')

root = Tk()

w = Label(root, text="Pythone Test")
b = Button(root, text="Hello Python", command=printHello)
c = Button(root, text="Quiz", command=root.quit)

w.pack()
b.pack()
c.pack()

root.mainloop()
