import json 
import os
from tkinter import *

class meth:
    def splitrom(romdir, splitString):
        romlist = []
        for item in romdir:
            newitem = item.split(splitString)
            fix = "".join(newitem)
            romlist.append(fix)
        return romlist
    def createDisplay(splitstring,listpath,listbox:Listbox):
        crateList = os.listdir(listpath)
        fixedDsList = meth.splitrom(crateList,splitstring)
        for item in fixedDsList:
            listbox.insert(END,item)
    