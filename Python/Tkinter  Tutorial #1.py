# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 20:14:18 2023

@author: Siddhant
"""

from tkinter import *   
import tkinter.messagebox  
root = Tk()  
  
root.geometry("200x100")  
root.configure(background="Blue")
def fun():  
    tkinter.messagebox.showerror("Hello", "The aliens have ARRIVED! THE END OF THE WORLD IS HERE!!.")  
def yeet():
    tkinter.messagebox.askyesno("LMFAO","Is green your favourite colour?")
def water():
    tkinter.messagebox.askquestion("Lmao","Do you eat noodles or not?")
def drinks():
    tkinter.messagebox.askretrycancel("HAGU","Are you subscribed to SM GaMing?")
  
b1 = Button(root,text = "Red",command = fun,activeforeground = "red",activebackground = "pink",pady=10)    
b2 = Button(root, text = "Blue",command = yeet,activeforeground = "blue",activebackground = "pink",pady=10)  
b3 = Button(root, text = "Green",command = water,activeforeground = "green",activebackground = "pink",pady = 10)
b4 = Button(root, text = "Yellow",command = drinks,activeforeground = "yellow",activebackground = "pink",pady = 10)  
  
b1.pack(side = LEFT)  
  
b2.pack(side = RIGHT)  
  
b3.pack(side = TOP)  
  
b4.pack(side = BOTTOM)  
  
root.mainloop()