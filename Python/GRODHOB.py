# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 20:49:13 2023

@author: Siddhant
"""

from tkinter import*

root=Tk()
root.geometry("1000x900")
root.configure(background="Yellow")

c = Canvas(root,bg = "Red",height="500",width ="700")
ark=c.create_arc((60,60,210,210),start=60, extent=359.99, fill ="white")
brk=c.create_arc((80,80,210,210),start=60, extent = 359.99, fill = "yellow")
csk=c.create_arc((100,100,210,210),start=60, extent = 359.99, fill="blue")
c.pack()


root.mainloop()