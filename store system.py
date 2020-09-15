from tkinter import*
import random
import time;

#To make sure that is gonna appear the canvas
root = Tk ()
root.geometry("1600x800")
root.title("Store system")

Box = Frame(root, width = 1600,height = 50,bg="red", relief=SUNKEN)
Box.pack(side=TOP)

Box1 = Frame(root, width = 160,height = 700,bg="red", relief=SUNKEN)
Box1.pack(side=LEFT)

Box2 = Frame(root, width = 1600,height = 700,bg="red", relief=SUNKEN)
Box2.pack(side=RIGHT)

#Time function
localtime=time.asctime(time.localtime(time.time()))

#labels
lblInfo = Label(Box, font=("arial",50),text="Store",fg="red", bd=10, anchor="w")
lblInfo.grid(row=0,column=0)

lblInfo = Label(Box, font=("arial",50),text=localtime,fg="red", bd=10, anchor="w")
lblInfo.grid(row=1,column=0)

#calculator
text_input = StringVar()
txtDisplay = Entry(Box2,font=("arial", 20), textvariable=text_input, bd=10, insertwidth=1, bg="white", justify="right")
txtDisplay.grid(columnspan=4)

operator= ""
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

btn7=Button(Box2,padx=16,pady=16,bd=5, fg="black", font=('arial',20),text="7",bg="red", command=lambda: btnClick(7)) .grid(row=2,column=0)

root.mainloop()
