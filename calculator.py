from tkinter import*

#To make sure that is gonna appear the canvas
root = Tk ()
root.geometry("1600x800")
root.title("Calculator")

Box = Frame(root, width = 1600,height = 50,bg="red", relief=RAISED)
Box.pack(side=TOP)

Box2 = Frame(root, width = 1000,height = 700,bg="#82E0AA", relief=RAISED)
Box2.pack(side=TOP)

#labels
lblInfo = Label(Box, font=("arial",40),text="Calculator",fg="#82E0AA", bd=10, anchor="w")
lblInfo.grid(row=0,column=0)

#calculator
text_input = StringVar()
txtDisplay = Entry(Box2,font=("arial", 20), textvariable=text_input, bd=0, insertwidth=1, bg="#FFFFFF", justify="right")
txtDisplay.grid(columnspan=4)

#show numbers on the input
operator= ""
def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)

#delete button
def btnDelete():
    global operator
    operator = ""
    text_input.set("")

#equal button
def btnEqual():
    global operator
    sumup =str(eval(operator))
    text_input.set(sumup)
    operator=""

#row 1 calculator
btn7=Button(Box2,padx=20,pady=20,bd=2, fg="black", font=('arial',20),text="7",bg="#82E0AA", command=lambda: btnClick(7)) .grid(row=2,column=0)
btn8=Button(Box2,padx=20,pady=20,bd=2, fg="black", font=('arial',20),text="8",bg="#82E0AA", command=lambda: btnClick(8)) .grid(row=2,column=1)
btn9=Button(Box2,padx=20,pady=20,bd=2, fg="black", font=('arial',20),text="9",bg="#82E0AA", command=lambda: btnClick(9)) .grid(row=2,column=2)
multiplication=Button(Box2,padx=20,pady=20,bd=2, fg="black", font=('arial',20),text="x",bg="#ABEBC6", command=lambda: btnClick("*")) .grid(row=2,column=3)

#row 2 calculator
btn4=Button(Box2,padx=20,pady=20,bd=2, fg="black", font=('arial',20),text="4",bg="#82E0AA", command=lambda: btnClick(4)) .grid(row=3,column=0)
btn5=Button(Box2,padx=20,pady=20,bd=2, fg="black", font=('arial',20),text="5",bg="#82E0AA", command=lambda: btnClick(5)) .grid(row=3,column=1)
btn6=Button(Box2,padx=20,pady=20,bd=2, fg="black", font=('arial',20),text="6",bg="#82E0AA", command=lambda: btnClick(6)) .grid(row=3,column=2)
subtraction=Button(Box2,padx=20,pady=20,bd=2, fg="black", font=('arial',20),text="-",bg="#ABEBC6", command=lambda: btnClick("-")) .grid(row=3,column=3)

#row 3 calculator
btn1=Button(Box2,padx=20,pady=20,bd=2, fg="black", font=('arial',20),text="1",bg="#82E0AA", command=lambda: btnClick(1)) .grid(row=4,column=0)
btn2=Button(Box2,padx=20,pady=20,bd=2, fg="black", font=('arial',20),text="2",bg="#82E0AA", command=lambda: btnClick(2)) .grid(row=4,column=1)
btn3=Button(Box2,padx=20,pady=20,bd=2, fg="black", font=('arial',20),text="3",bg="#82E0AA", command=lambda: btnClick(3)) .grid(row=4,column=2)
addition=Button(Box2,padx=20,pady=20,bd=2, fg="black", font=('arial',20),text="+",bg="#ABEBC6", command=lambda: btnClick("+")) .grid(row=4,column=3)

#row 4 calculator
equal=Button(Box2,padx=20,pady=20,bd=2, fg="black", font=('arial',20),text="=",bg="#ABEBC6", command=btnEqual) .grid(row=5,column=0)
btn0=Button(Box2,padx=20,pady=20,bd=2, fg="black", font=('arial',20),text="0",bg="#82E0AA", command=lambda: btnClick(0)) .grid(row=5,column=1)
delete=Button(Box2,padx=20,pady=20,bd=2, fg="black", font=('arial',20),text="C",bg="#ABEBC6", command=btnDelete) .grid(row=5,column=2)
division=Button(Box2,padx=20,pady=20,bd=2, fg="black", font=('arial',20),text="/",bg="#ABEBC6", command=lambda: btnClick("/")) .grid(row=5,column=3)

root.mainloop()
