import tkinter as tk
from tkinter import *
import os
from allmethods import meth


root = tk.Tk()

root.title("Rom Archive")
root.geometry("1000x500")

"""Ds Stuff"""
dsListbox = Listbox(root)
meth.createDisplay(".nds","E:/Ds Dumps", dsListbox)
dsListbox.config(width=40)
dsLabel = Label(root,text="Ds Games")

#Placing Ds stuff
dsLabel.place(x=50,y=25)
dsListbox.place(x=50,y=50)

"""3Ds Stuff"""
ThreeDsListbox = Listbox(root)
ThreeDsListbox.config(width=40)
threedlist = os.listdir("E:/3Ds Dumps")

#Splitting all of the roms
cxiList = []
threeDList = []
all3dsRoms = []
for rom in threedlist:
    if rom.endswith('.cxi'):
        cxiList.append(rom)
    elif rom.endswith('.3ds'):
        threeDList.append(rom)
cxiSplit = meth.splitrom(cxiList,".cxi")
threeDSplit = meth.splitrom(threeDList,'.3ds')
all3dsRoms = cxiSplit + threeDSplit
for item in all3dsRoms:
    ThreeDsListbox.insert(END,item)
threeDsLabel = Label(root,text="3Ds Games")
#placing 3Ds Stuff
ThreeDsListbox.place(x=350,y=50)
threeDsLabel.place(x=350,y=25)

"""Switch"""
#Display Stuff
switchListbox = Listbox(root)
switchListbox.config(width=40)
switchLabel = Label(root,text="Switch Games")
gameList = os.listdir("E:/Switch Dumps/Unfused Backup")
for item in gameList:
    switchListbox.insert(END,item)

#Placing Switch stuff
switchListbox.place(x=50,y=275)
switchLabel.place(x=50,y=250)


"Wii"
#Stuff for the display
wiiListbox = Listbox(root)
wiiListbox.config(width=40,height=3)
wiiLabel = Label(root,text="Wii Games")
#making the Path a List
wiiGames = os.listdir("E:/Wii Dumps")

#adding the List to the Listbox
for item in wiiGames:
    wiiListbox.insert(END,item)

#Placing everything
wiiListbox.place(x=350,y=275)
wiiLabel.place(x=350, y=250)

"""Wii U"""
#Wii U Game list
wiiUgames = os.listdir("E:/Wii U Dumps/Games")

wiiUListbox = Listbox(root)
wiiUlabel = Label(root,text="Wii U Games")
wiiUListbox.config(width=40,height=4)


for item in wiiUgames:
    wiiUListbox.insert(END,item)
wiiUListbox.place(x=350,y=375)
wiiUlabel.place(x=350,y=350)



root.mainloop()