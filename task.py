import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import calendar
from datetime import datetime
import pickle
from abc import ABC, abstractmethod

pages = ["Day", "Week", "Month"]
   
time_slot = []
for i in range(24):
    if i < 10:
        time_slot.append("0" + str(i) + ".00AM")
        time_slot.append("0" + str(i) + ".30AM")
    elif i > 12:
        time_slot.append(str(i) + ":00PM")
        time_slot.append(str(i) + ":30PM")
    else: 
        time_slot.append(str(i) + ":00AM")
        time_slot.append(str(i) + ":30AM")

notify_me = ["Yes", "No"]
category_list = ["None", "Work", "Study", "Exercise", "Leisure", "Others"]

#global var 
today  = datetime.now()
current_year = today.strftime("%Y")
current_month = today.strftime("%B")
current_date = today.strftime("%d")
current_day = today.strftime("%A")
current_page = "Day" 

#template for all pages 
class Planner(ABC): 
    @abstractmethod
    def create_widget(self): 
        pass

    @abstractmethod
    def save(self):
        pass
    
    @abstractmethod
    def clear_input(self): 
        pass
    
class Generic(tk.Tk, Planner):
    def __init__(self):
        self.title("Planner")
        self.geometry("785x500")
        self.resizable(width = False, height = False)
        self.create_widget()
        #default setting
        if current_page == "Day":
            self.dayframe = Day(self)
        
    def call_day(self):
        self.dayframe = Day(self)  # Create Day frame   
        global current_page
        current_page = "Day"
    
    def create_widget(self): 
        Button(self,text = "+", width = 3, borderwidth = 0, highlightthickness = 0).place(x = 270, y = 5)
        Button(self,text = "Day", width = 3, borderwidth = 0, highlightthickness = 0, command=self.call_day).place(x = 340, y = 5)
        Button(self,text = "Week", width = 3, borderwidth = 0, highlightthickness = 0).place(x = 410, y = 5)
        Button(self,text = "Month", width = 3, borderwidth = 0, highlightthickness = 0).place(x = 480, y = 5)
        
        Button(self, text = "<", width = 1, borderwidth = 0, highlightthickness = 0).place(x = 630, y = 20)
        Button(self, text = "Today", width = 3, borderwidth = 0, highlightthickness = 0).place(x = 670, y = 20)
        Button(self, text = ">", width = 1, borderwidth = 0, highlightthickness = 0).place(x = 730, y = 20)
        
        self.today = datetime.now()
        self.date = self.today.strftime("%B %d, %Y")
        Label(self, text = self.date, font = ("Arial", 25, "bold")).place(x = 10, y = 45)
        Label(self, text = self.today.strftime("%A"), font = ("Arial", 20)).place(x = 10, y = 72)

    def save(self):
        pass
    
    def clear_input(self): 
        pass
    
    
class Day(Generic): 
    def __init__(self, master):
        super().__init__()
        self.place(x = 0, y = 100, width = 785, height = 490) #set up frame iwht specific location 
        tableframe = tk.Frame(self, bg="grey")
        tableframe.place(x = 0, y = 10, width = 445, height = 900)
        self.create_widget()
    
    def create_widget(self): 
        super().create_widget()
        rightframe = tk.Frame(self, bg="#D9D9D9")
        rightframe.place(x = 444, y = 10, width = 340, height = 900)
        Button(rightframe, text="add", font = ("Arial", 15), width = 5, height = 2, borderwidth=0, highlightthickness=0, pady = 0, background="#ABBBF0").place(x = 20, y = 20)
        inputframe = tk.Frame(rightframe, bg="#ABBBF0")
        inputframe.place(x = 20, y = 50, width = 300, height = 260)
        
        Label(inputframe, text = "Note", font = ("Arial", 15)).place(x = 0, y = 12)
        self.note = tk.Entry(inputframe, borderwidth = 1) #20 15 15
        self.note.place(x = 90, y = 10)
        
        Label(inputframe, text = "Category", font = ("Arial", 15)).place(x = 0, y = 42)
        self.category = Collapsible_list.create(self, frame=inputframe, width = 15, datalist=category_list, x = 90, y = 40, canType=True)
        
        Label(inputframe, text = "Time period (From - To)", font = ("Arial", 15)).place(x = 0, y = 70)
        self.start_time = Collapsible_list.create(self, frame=inputframe, width = 7, datalist=time_slot, x = 90, y = 100)
        self.end_time = Collapsible_list.create(self, frame=inputframe, width = 7, datalist=time_slot, x = 200, y = 100)
        
        Label(inputframe, text = "Location", font = ("Arial", 15)).place(x = 0, y = 130)
        self.location = tk.Entry(inputframe, width = 15, borderwidth = 1)
        self.location.place(x = 90, y = 130)
        
        Label(inputframe, text = "Notify me", font = ("Arial", 15)).place(x = 0, y = 160)
        self.notify = Collapsible_list.create(self, frame=inputframe, width = 7, datalist=notify_me, x = 90, y = 160)
        
        Button(inputframe, text="Save", font=("Arial", 15), command = self.save,  width = 5, borderwidth=0, highlightthickness=0, pady = 10, background="#ABBBF0").place(x = 190, y = 200)
    
    def save(self):
        note = self.note.get() 
        category_result = self.category.get()
        start_t = self.start_time.get()
        end_t = self.end_time.get()
        location = self.location.get()
        notify_result = self.notify.get()
        data = [note,category_result, start_t, end_t, location, notify_result]
        FileHandling.save_data(self, data, 'data.pickle')
        
    def clear_input(self): 
        self.note.delete(0, 'end')
        self.category.set('')
        self.location.delete(0, 'end')
        #clear combobox
        self.start_time.set('')
        self.end_time.set('')
        self.notify.set('')

class Collapsible_list: 
    def create(self, frame, width, datalist, row=None, column=None, x=None, y=None, canType = False):
        data = tk.StringVar()
        data_combobox = ttk.Combobox(frame, width=width, textvariable=data)
        data_combobox['value'] = datalist
        if canType == False: 
            data_combobox['state'] = 'readonly'
        data_combobox.place(x=x, y=y)
        return data
    
    
class FileHandling:
    def load_data(self, filename):
        loaded_data = None
        with open(filename, 'rb') as file: 
            loaded_data = pickle.load(file)
        return loaded_data
    
    def save_data(self, data, filename):
        note = data[0]
        category = data[1]
        start_t = data[2]
        end_t = data[3]
        start = float(start_t[:len(start_t)-2])
        end = float(end_t[:len(end_t)-2])
        location = data[4]
        notify_result = data[5]
        
        if note == "" or category == "" or location == "" :
            tk.messagebox.showerror(title="incomplete info", message="Please fill in all the information", icon="warning")
        else:
            if start == end: 
                tk.messagebox.showerror(title="the same start end time",message="Error: Start time and End time cannot be the same", icon="warning")
            elif start > end:  
                tk.messagebox.showerror(title="invalid start end time", message= "Start time cannot be later than End time", icon="warning")
            else: 
                category_list.append(category)
                data = {
                    'Year': current_year,
                    'Month': current_month,
                    'Day' : [
                        {
                            'Date': current_date,
                            'Day_of_week' : current_day,
                            'Time_slot' : [
                                {
                                    '1' : {
                                        'note' : note, 
                                        'category' : category,
                                        'location' : location,
                                        'start' : start_t,
                                        'end' : end_t,
                                        'notify_me' : notify_result
                                    }
                                }
                            ]
                        }
                    ]
                }
                
                with open(filename, 'wb') as file: 
                    pickle.dump(data, file)
                    
                loaded_data = self.load_data('data.pickle')
                if loaded_data['Year'] == current_year and loaded_data['Month'] == current_month:
                    for i, n in enumerate(loaded_data['Day']):
                        if n['Date'] == str(current_date):
                            id = len(n['Time_slot']) + 1
                            n['Time_slot'].append({str(id) : {
                                            'note' : note, 
                                            'category' : category,
                                            'location' : location,
                                            'start' : start_t,
                                            'end' : end_t,
                                            'notify_me' : notify_result
                                        }})
                            print("Success1")
                        elif i == len(loaded_data['Day']) - 1: 
                            id = 1
                            loaded_data['Day'].append({'Date': current_date,
                                'Day_of_week' : current_day,
                                'Time_slot' : [
                                    {
                                        str(id) : {
                                            'note' : note, 
                                            'category' : category,
                                            'location' : location,
                                            'start' : start_t,
                                            'end' : end_t,
                                            'notify_me' : notify_result
                                        }
                                    }
                                ]})
                            print("Success2")
                else: 
                    print(data)
                    loaded_data.append(data)
                    print("Success3")
                
                print(loaded_data)
                print(category_list)

if __name__ == "__main__":
    planner = Generic()  
    planner.mainloop()  