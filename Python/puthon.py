# -*- coding: utf-8 -*-
"""
Created on Tue May  2 15:15:30 2023

@author: Siddhant
"""
""''##
from tkinter import*
root=Tk()
root.geometry ("1000x1200")
root.configure(bg = "#ED5488")
L1=Label(root,text="My list of favorite games")
Vul=Listbox(root,bg="#3A377B",fg="LightBlue")
Vul.pack()
Vul.insert(1,"Bedwars")
Vul.insert(2,"Minecraft")
Vul.insert(3,"War robots")
Vul.insert(4,"Arsenal")
Vul.insert(5,"Doors")
Vul.insert(6,"CSGO")
Vul.insert(7,"Fortnite")
Vul.insert(8,"Roblox")
Vul.insert(9,"PV2")

B1=Button(root,text="Aim trainer",command = lambda Vul=Vul:Vul.delete(ANCHOR) ,activeforeground="#67934C",activebackground="#2C4D3E")
B1.pack()
Vul.pack()
root.mainloop()