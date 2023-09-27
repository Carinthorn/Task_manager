import tkinter as tk
from tkinter import *
import calendar

root = tk.Tk()
class Planner():
    def __init__(self): 
        menubar = Menu(root)
        day = Menu(menubar, tearoff = 0)
        week = Menu(menubar, tearoff = 0)
        month = Menu(menubar, tearoff = 0)
        root.config(menu = menubar)
        
Planner()
root.mainloop()
        
        
        
# class Day(): 
    

# class Week():
    
    
# class Month():
    