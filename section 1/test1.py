from tkinter import *
def printHello():
    print("Hello Sydeny")

root = Tk()
l=Label(root,text="파이썬테스트")
b=Button(root,text="hello sindy",command=printHello)
c=Button(root,text="Quit",command=root.quit)

l.pack()
b.pack()
c.pack()

root.mainloop()
