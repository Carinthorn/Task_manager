import tkinter as tk
from tkinter import *
import calendar 

#refactor frame and create a class for month Month(tk.Frame) + def(__inti__): tk.Frame parent somthing 
window = tk.Tk()
window.title("Task Manager")
window.geometry("785x500")
class Planner(tk.Tk):
    def __init__(self, *arg, **kwargs):    
        #problem
        # menubar = Menu(root)
        # day = Menu(menubar, tearoff = 0)
        # week = Menu(menubar, tearoff = 0)
        # month = Menu(menubar, tearoff = 0)
        # menubar.add_cascade(label = "Day", menu = day)
        # menubar.add_cascade(label = "Week", menu = week)
        # menubar.add_cascade(label = "Month", menu = month)
        # root.config(menu = menubar)
        
        #temporary menubar
        # container = tk.Frame(self)
        # container.pack(side="top", fill="both", expand=True)
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)
        menu =  Frame(window)
        menu.grid(row = 0, column = 3, rowspan = 1, columnspan = 7, sticky= tk.W+tk.E)
        Button(menu,text = "+", width = 3, borderwidth = 0, highlightthickness = 0).grid(row = 1, column = 0)
        Button(menu,text = "Day", width = 3, borderwidth = 0, highlightthickness = 0).grid(row = 1, column = 1)
        Button(menu,text = "Week", width = 3, borderwidth = 0, highlightthickness = 0).grid(row = 1, column = 2)
        Button(menu,text = "Month", width = 3, borderwidth = 0, highlightthickness = 0).grid(row = 1, column = 3)
        
        change_bar = Frame(window)
        change_bar.grid(row = 1, column = 6, rowspan = 1, columnspan = 1, sticky = tk.E)
        Button(change_bar, text = "<", width = 1, borderwidth = 0, highlightthickness = 0).grid(row = 1, column = 5, sticky = "e")
        Button(change_bar, text = "Today", width = 3, borderwidth = 0, highlightthickness = 0).grid(row = 1, column = 6, sticky = "e")
        Button(change_bar, text = ">", width = 1, borderwidth = 0, highlightthickness = 0).grid(row = 1, column = 7, sticky = "e")
        
        #calendar
        current_date = "August" + " 2023 " + "BCE"
        Label(window, text = current_date, font=("Arial", 25, "bold")).grid(row = 2, column = 0, rowspan = 2, columnspan = 7, padx = 3, sticky = tk.W)
        calendar_frame = Frame(window)
        calendar_frame.grid(row = 4, column = 0, rowspan = 6, columnspan = 7, sticky= tk.W+tk.E )

        #calendar day labels
        day_labels = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for i, day in enumerate(day_labels):
            Label(calendar_frame, text = day, width = 7, height = 2, relief = "flat", borderwidth = 0, highlightthickness=0).grid(row = 3, column = i, sticky = tk.E)

        row = 5
        column = 0
        days = calendar.monthcalendar(2023, 8)
        for i in range(42): 
            #fucking text problem
            text=i+1
            if text > 31:
                text = (i - 31) + 1
            if i == 11:
                Button(calendar_frame,text=str(text) + "\n-Trip with homies\n-Mountain bike", width = 9, height = 3, relief = "flat", borderwidth = 0, highlightthickness=0, anchor="ne", bg= "#D9D9D9", command = self.display_info).grid(row = row, column = column)
            else:
                self.button = Button(calendar_frame, text=text, width = 9, height = 3, relief = "flat", borderwidth = 0, highlightthickness=0, anchor="ne", bg= "#A4DE9B", command = self.display_info).grid(row = row, column = column)
            #button display info and add info
            column += 1
            if column == 7:
                row += 1
                column = 0
        canvas = tk.Canvas(calendar_frame, width = 200, height = 100)
        canvas.create_rectangle(50, 50, 200, 150, outline="black", fill="red")

        
    def display_info(self, event):
        #check database if the user added sth in a cell if not = add, if so = edit/delete
        pass
# class Month(): 
if __name__ == "__main__": 
    Planner()
    window.mainloop()
    

# class Day(): 
    

# class Week():
    
    
# class Month():
    
