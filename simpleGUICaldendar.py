from tkinter import *
import calendar 

box=calendar.calendar(2020)

root=Tk()
root.geometry("550x600")
root.title("Calendar")
label1=Label(root,text="Calendar",bg='#FFFFFF',fg="#B364BD",font=("times",28,'bold'))
label1.grid(row=1,column=1)
root.config(bg="#FFFFFF")
l1=Label(root,text=box,font="consolas 10 bold")
l1.grid(row=2,column=1,padx=20)
root.mainloop()
