import sys
from tkinter import *

print("hello")


def timeTable():
    print("\n")
    for x in range(1,13):
      m  = int(EnterTable.get())
      print('\t\t',(x),' x ',(m),'=',(x*m))



Multiply = Tk()
Multiply.geometry('500x760')
Multiply.title("Multiplication table")


EnterTable = StringVar()

Label1 = Label(Multiply,text="Multiplication time table",font =30,fg='Black').grid(row=1,column=6)
Label1 = Label(Multiply,text='                                       ').grid(row=2,column=6)
entry5 = Entry(Multiply,textvariable=EnterTable,justify='center').grid(row=3,column=6)
Label1 = Label(Multiply,text='                                     ').grid(row=4,column=6)


Button1 = Button(Multiply,text="Times tables",command=timeTable).grid(row=5,column=6)
Label1 = Label(Multiply,text='                                       ').grid(row=6,column=6)
QUIT = Button(Multiply,text='Quit',fg="Red",command=Multiply.destroy).grid(row=7,column=6)


Multiply.mainloop()
