from tkinter import*
import random
import time;

#To make sure that is gonna appear the canvas
root = Tk ()
root.geometry("1600x800")
root.title("Restaurant system")

Box = Frame(root, width = 1600,height = 50, relief=SUNKEN)
Box.pack(side=TOP)

Box1 = Frame(root, width = 800,height = 700, relief=SUNKEN , padx=100, pady=0)
Box1.pack(side=LEFT)

Box2 = Frame(root, width = 300,height = 700, relief=SUNKEN, padx=200, pady=10)
Box2.pack(side=RIGHT)

#Time function
localtime=time.asctime(time.localtime(time.time()))

#labels
lblInfo = Label(Box, font=("arial",40),text="Sales system",fg="#82E0AA", bd=10, anchor="w")
lblInfo.grid(row=0,column=0)

lblInfo = Label(Box, font=("arial",15),text=localtime,fg="#ABEBC6", bd=10, anchor="w")
lblInfo.grid(row=1,column=0)

def Ref():
    x = random.randint(100, 999)
    randomRef = str(x)
    rand.set(randomRef)

    CoA =float(Coats.get())
    CoB =float(Shirts.get())
    CoC =float(Shorts.get())
    CoD =float(Socks.get())
    CoE =float(Shoes.get())
    CoF =float(Glasses.get())
    CoG =float(Watches.get())
    CoH =float(Bracelets.get())

    CostofCoats = CoA * 20.00
    CostofShirts = CoB * 15.00
    CostofShorts = CoC * 17.50 
    CostofSocks = CoD * 9.50
    CostofShoes = CoE * 36.00
    CostofGlasses = CoF * 13.50
    CostofWatches = CoG * 27.50
    CostosBracelets = CoH * 7.00

    CostofShopping = "$", str("%.2f" % (CostofCoats + CostofShirts + CostofShorts + CostofSocks + CostofShoes + CostofGlasses + CostofWatches + CostosBracelets))

    PayTax = ((CostofCoats + CostofShirts + CostofShorts + CostofSocks + CostofShoes + CostofGlasses + CostofWatches + CostosBracelets) * 0.2)

    TotalCost = (CostofCoats + CostofShirts + CostofShorts + CostofSocks + CostofShoes + CostofGlasses + CostofWatches + CostosBracelets)

    OverAllCost = "$", str("%.2f" % (PayTax + TotalCost))
    PaidTax = "$", str("%.2f" % PayTax)
    Taxes.set(PaidTax)
    Subtotal.set(CostofShopping)
    Total.set(OverAllCost)

#Reset
def Reset():
    rand.set("")
    Coats.set("")
    Shirts.set("")
    Shorts.set("")
    Socks.set("")
    Shoes.set("")
    Glasses.set("")
    Watches.set("")
    Bracelets.set("")
    Subtotal.set("")
    Taxes.set("")
    Total.set("")

#Exit
def qExit():
    root.destroy()

#products & invoice
rand = StringVar()
Coats = StringVar()
Shirts = StringVar()
Shorts = StringVar()
Socks = StringVar()
Shoes = StringVar()

lblInvoice = Label(Box1, font=("arial",15),text="Invoice no.", bd=5, anchor="w")
lblInvoice.grid(row=0,column=0)
txtInvoice=Entry(Box1, font=("arial",15),textvariable=rand, bd=5, insertwidth=4, bg="#82E0AA", justify = "right")
txtInvoice.grid(row=0,column=1, padx=10, pady=10)

lblCoats = Label(Box1, font=("arial",15),text="Coats", bd=5, anchor="w")
lblCoats.grid(row=1,column=0)
txtCoats=Entry(Box1, font=("arial",15),textvariable=Coats, bd=5, insertwidth=4, bg="#82E0AA", justify = "right")
txtCoats.grid(row=1,column=1, padx=10, pady=10)

lblShirts = Label(Box1, font=("arial",15),text="Shirts", bd=5, anchor="w")
lblShirts.grid(row=2,column=0)
txtShirts=Entry(Box1, font=("arial",15),textvariable=Shirts, bd=5, insertwidth=4, bg="#82E0AA", justify = "right")
txtShirts.grid(row=2,column=1, padx=10, pady=10)

lblShorts = Label(Box1, font=("arial",15),text="Shorts", bd=5, anchor="w")
lblShorts.grid(row=3,column=0)
txtShorts=Entry(Box1, font=("arial",15),textvariable=Shorts, bd=5, insertwidth=4, bg="#82E0AA", justify = "right")
txtShorts.grid(row=3,column=1, padx=10, pady=10)

lblSocks = Label(Box1, font=("arial",15),text="Socks", bd=5, anchor="w")
lblSocks.grid(row=4,column=0)
txtSocks=Entry(Box1, font=("arial",15),textvariable=Socks, bd=5, insertwidth=4, bg="#82E0AA", justify = "right")
txtSocks.grid(row=4,column=1, padx=10, pady=10)

lblShoes = Label(Box1, font=("arial",15),text="Shoes", bd=5, anchor="w")
lblShoes.grid(row=5,column=0)
txtShoes=Entry(Box1, font=("arial",15),textvariable=Shoes, bd=5, insertwidth=4, bg="#82E0AA", justify = "right")
txtShoes.grid(row=5,column=1, padx=10, pady=10)

#products & invoice 2nd column
Glasses = StringVar()
Watches = StringVar()
Bracelets = StringVar()
Subtotal = StringVar()
Taxes = StringVar()
Total = StringVar()

lblGlasses = Label(Box1, font=("arial",15),text="Glasses", bd=5, anchor="w")
lblGlasses.grid(row=0,column=2)
txtGlasses=Entry(Box1, font=("arial",15),textvariable=Glasses, bd=5, insertwidth=4, bg="#82E0AA", justify = "right")
txtGlasses.grid(row=0,column=3, padx=10, pady=10)

lblWatches = Label(Box1, font=("arial",15),text="Watches", bd=5, anchor="w")
lblWatches.grid(row=1,column=2)
txtWatches=Entry(Box1, font=("arial",15),textvariable=Watches, bd=5, insertwidth=4, bg="#82E0AA", justify = "right")
txtWatches.grid(row=1,column=3, padx=10, pady=10)

lblBracelets = Label(Box1, font=("arial",15),text="Bracelets", bd=5, anchor="w")
lblBracelets.grid(row=2,column=2)
txtBracelets=Entry(Box1, font=("arial",15),textvariable=Bracelets, bd=5, insertwidth=4, bg="#82E0AA", justify = "right")
txtBracelets.grid(row=2,column=3, padx=10, pady=10)

lblSubtotal = Label(Box1, font=("arial",15),text="Subtotal", bd=5, anchor="w")
lblSubtotal.grid(row=3,column=2)
txtSubtotal=Entry(Box1, font=("arial",15),textvariable=Subtotal, bd=5, insertwidth=4, bg="#82E0AA", justify = "right")
txtSubtotal.grid(row=3,column=3, padx=10, pady=10)

lblTaxes = Label(Box1, font=("arial",15),text="Taxes", bd=5, anchor="w")
lblTaxes.grid(row=4,column=2)
txtTaxes=Entry(Box1, font=("arial",15),textvariable=Taxes, bd=5, insertwidth=4, bg="#82E0AA", justify = "right")
txtTaxes.grid(row=4,column=3, padx=10, pady=10)

lblTotal = Label(Box1, font=("arial",15),text="Total", bd=5, anchor="w")
lblTotal.grid(row=5,column=2)
txtTotal=Entry(Box1, font=("arial",15),textvariable=Total, bd=5, insertwidth=4, bg="#82E0AA", justify = "right")
txtTotal.grid(row=5,column=3, padx=10, pady=10)

#Button Total
btnTotal=Button(Box1,padx=16,pady=16, fg="black",font=('arial',20), width=5, text="Total", bg="#FFFFFF", command= Ref).grid(row=7, column=1)

#Button Reset
btnReset=Button(Box1,padx=16, pady=16, fg="black", font=('arial',20), width=5, text="Reset", bg="#FFFFFF", command=Reset).grid(row=7, column=2)

#Button Exit
btnExit=Button(Box1,padx=16, pady=16, fg="black", font=('arial',20), width=5, text="Exit", bg="#FFFFFF", command=qExit).grid(row=7, column=3)

#calculator
text_input = StringVar()
txtDisplay = Entry(Box2,font=("arial", 20), textvariable=text_input, bd=10, insertwidth=1, bg="#FFFFFF", justify="right")
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
btn7=Button(Box2,padx=16,pady=16,bd=8, fg="black", font=('arial',20),text="7",bg="#82E0AA", command=lambda: btnClick(7)) .grid(row=2,column=0)
btn8=Button(Box2,padx=16,pady=16,bd=8, fg="black", font=('arial',20),text="8",bg="#82E0AA", command=lambda: btnClick(8)) .grid(row=2,column=1)
btn9=Button(Box2,padx=16,pady=16,bd=8, fg="black", font=('arial',20),text="9",bg="#82E0AA", command=lambda: btnClick(9)) .grid(row=2,column=2)
multiplication=Button(Box2,padx=16,pady=16,bd=8, fg="black", font=('arial',20),text="x",bg="#ABEBC6", command=lambda: btnClick("*")) .grid(row=2,column=3)

#row 2 calculator
btn4=Button(Box2,padx=16,pady=16,bd=8, fg="black", font=('arial',20),text="4",bg="#82E0AA", command=lambda: btnClick(4)) .grid(row=3,column=0)
btn5=Button(Box2,padx=16,pady=16,bd=8, fg="black", font=('arial',20),text="5",bg="#82E0AA", command=lambda: btnClick(5)) .grid(row=3,column=1)
btn6=Button(Box2,padx=16,pady=16,bd=8, fg="black", font=('arial',20),text="6",bg="#82E0AA", command=lambda: btnClick(6)) .grid(row=3,column=2)
subtraction=Button(Box2,padx=16,pady=16,bd=8, fg="black", font=('arial',20),text="-",bg="#ABEBC6", command=lambda: btnClick("-")) .grid(row=3,column=3)

#row 3 calculator
btn1=Button(Box2,padx=16,pady=16,bd=8, fg="black", font=('arial',20),text="1",bg="#82E0AA", command=lambda: btnClick(1)) .grid(row=4,column=0)
btn2=Button(Box2,padx=16,pady=16,bd=8, fg="black", font=('arial',20),text="2",bg="#82E0AA", command=lambda: btnClick(2)) .grid(row=4,column=1)
btn3=Button(Box2,padx=16,pady=16,bd=8, fg="black", font=('arial',20),text="3",bg="#82E0AA", command=lambda: btnClick(3)) .grid(row=4,column=2)
addition=Button(Box2,padx=16,pady=16,bd=8, fg="black", font=('arial',20),text="+",bg="#ABEBC6", command=lambda: btnClick("+")) .grid(row=4,column=3)

#row 4 calculator
equal=Button(Box2,padx=16,pady=16,bd=8, fg="black", font=('arial',20),text="=",bg="#ABEBC6", command=btnEqual) .grid(row=5,column=0)
btn0=Button(Box2,padx=16,pady=16,bd=8, fg="black", font=('arial',20),text="0",bg="#82E0AA", command=lambda: btnClick(0)) .grid(row=5,column=1)
delete=Button(Box2,padx=16,pady=16,bd=8, fg="black", font=('arial',20),text="C",bg="#ABEBC6", command=btnDelete) .grid(row=5,column=2)
division=Button(Box2,padx=16,pady=16,bd=8, fg="black", font=('arial',20),text="/",bg="#ABEBC6", command=lambda: btnClick("/")) .grid(row=5,column=3)

root.mainloop()
