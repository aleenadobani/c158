# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 16:39:43 2023

@author: User
"""

#bad geometry error
from tkinter import *
root=Tk()
root.title("Geometry Error")

try:
    root.geometry("600")
except:
    print("Bad geometry error, only one dimension passed in geometry instead of two")
    
    root.mainloop()