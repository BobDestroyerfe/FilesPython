# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 20:15:04 2023

@auhtor: Siddhant
"""

from tkinter import*

from functools import partial
root=Tk()
root.geometry("500x700")
root.configure(bg="LightBlue")
def add(L2,Num1,Num2):
    N1=(int)(Num1.get())
    N2=(int)(Num2.get())
    result=N1+N2
    L2.config(text=result)
    return
def sub(L2,Num1,Num2):
        N1=(int)(Num1.get())
        N2=(int)(Num2.get())
        result=N1-N2
        L2.config(text=result)
        return
def mult(L2,Num1,Num2):
    N1=(int)(Num1.get())
    N2=(int)(Num2.get())
    result=N1*N2
    L2.config(text=result)
    return
def div(L2,Num1,Num2):
    N1=(float)(Num1.get())
    N2=(float)(Num2.get())
    result=N1/N2
    L2.config(text=result)
    return
Num1=StringVar()
Num2=StringVar()
L1=Label(root,text="Enter the numbers").place(x=30,y=50)
E1=Entry(root,textvariable=Num1)
E1.place(relx = 0.5 , rely = 0.4, anchor = CENTER)
E2=Entry(root,textvariable=Num2)
E2.place(relx = 0.5 ,rely = 0.6, anchor = CENTER)
L2=Label(root,text="0",width=30)
L2.place(relx = 0.3 ,rely = 0.8, anchor = CENTER  )
add=partial(add,L2,Num1,Num2)
sub=partial(sub,L2,Num1,Num2)
mult=partial(mult,L2,Num1,Num2)
div=partial(div,L2,Num1,Num2)
Add1=Button(root,text="+",command = add, activeforeground="Yellow",activebackground="Black").place(x = 30 , y = 150 )
Sub2=Button(root,text="-",command = sub,activeforeground="LightBlue",activebackground="Blue",width = 3).place(x = 30, y = 180 )
Mult1=Button(root,text="*",command = mult,activeforeground="Red",activebackground="Pink").place(x = 30, y = 210)
Div1=Button(root,text="÷",command = div,activeforeground="Yellow",activebackground="Red").place(x = 30, y = 240)
root.mainloop()