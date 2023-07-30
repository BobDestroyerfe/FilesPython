# -*- coding: utf-8 -*-
"""
Created on Mon May  1 20:10:45 2023

@author: Siddhant
"""

from tkinter import*
from tkinter import messagebox    
from playsound import playsound
root=Tk()
root.geometry("500x700")
root.configure(bg="Black")
def joke1():
    messagebox.showinfo("Joke","Because they have many fans")
    playsound('1.mp3')
def joke2():
    messagebox.showinfo("Joke1","I dont know but the flag i s a big plus")
def joke3():
    messagebox.showinfo("Joke2","He said OUCH!")
def joke4():
    messagebox.showinfo("Joke3","Watermelon")
f=Frame(root)
f.pack()
leftframe=Frame(root)
leftframe.pack(side=LEFT)
rightframe=Frame(root)
rightframe.pack(side=RIGHT)
B1=Button(f,command = joke1,text="How do celebrities stay cool",activeforeground="Pink",activebackground="Red")
B1.pack(side= BOTTOM)
B2=Button(f,command = joke2, text="What's the best thing about Switzerland?",activeforeground="#3D0EA4",activebackground="#04F524")
B2.pack(side = TOP)
B3=Button(rightframe,command =joke3 ,text="What did the man do after he fell?",activeforeground="#438301",activebackground="#3F96E9")
B3.pack()
B4=Button(leftframe,command = joke4,text="When do you go at red and stop at green",activeforeground="#4D8ACE",activebackground="#68D352")
#00EC6D")
B4.pack()
root.mainloop()