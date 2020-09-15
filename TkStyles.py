from Tkinter import *
import Tkinter

top = Tkinter.Tk()

B1 = Tkinter.Button(top, text ="FLAT", relief=FLAT )
B2 = Tkinter.Button(top, text ="RAISED", relief=RAISED )
B3 = Tkinter.Button(top, text ="SUNKEN", relief=SUNKEN )
B4 = Tkinter.Button(top, text ="GROOVE", relief=GROOVE )
B5 = Tkinter.Button(top, text ="RIDGE", relief=RIDGE )

B1.pack()
B2.pack()
B3.pack()
B4.pack()
B5.pack()
top.mainloop()
