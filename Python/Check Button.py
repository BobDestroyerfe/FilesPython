# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 16:20:49 2023

@author: Siddhant
"""

from tkinter import*
root=Tk()
root.geometry=("200x100")
root.configure(bg="LightBlue")
checkvar1=IntVar()
checkvar2=IntVar()
checkvar3=IntVar()
label1=Label(root,text="Which language?")
label1.pack()
chkbtn1=Checkbutton(root,text="English",variable=checkvar1,onvalue=1,offvalue=0,height=5,width=10)
chkbtn1.pack()
chkbtn2=Checkbutton(root,text="Hindi",variable=checkvar2,onvalue=1,offvalue=0,height=5,width=10)
chkbtn2.pack()
chkbtn3=Checkbutton(root,text="French",variable=checkvar3,onvalue=1,offvalue=0,height=5,width=10)
chkbtn3.pack()
root.mainloop()