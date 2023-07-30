# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 16:32:47 2023

@author: Siddhant
"""

from tkinter import*
import tkinter.messagebox 
root=Tk()
root.geometry=("200x100")
root.configure(bg="LightBlue")
def giga():
    tkinter.messagebox.showinfo("Link","https://www.youtube.com/channel/UCYODqRdwq4JfVT4o-RdS2_g")
name=Label(root,text="Name").place(x=30,y=50)
email=Label(root,text="Email").place(x=30,y=90)
password=Label(root,text="Password").place(x=30,y=130)
submit=Button(root,text="Submit",command = giga,activeforeground="Red",activebackground="Pink",).place(x=30,y=170)
e1=Entry(root).place(x=80,y=50)
e2=Entry(root).place(x=80,y=90)
e3=Entry(root,show="*").place(x=90,y=130)
root.mainloop()