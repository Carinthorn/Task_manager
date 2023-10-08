import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from datetime import datetime
import pickle
from abc import ABC, abstractmethod

# Global variables
current_year = datetime.now().strftime("%Y")
current_month = datetime.now().strftime("%B")
current_date = datetime.now().strftime("%d")
current_day = datetime.now().strftime("%A")

pages = ["Day", "Week", "Month"]
   
time_slot = []
for i in range(24):
    if i < 10:
        time_slot.append("0" + str(i) + ".00AM")
        time_slot.append("0" + str(i) + ".30AM")
    elif i > 12:
        time_slot.append(str(i) + ".00PM")
        time_slot.append(str(i) + ".30PM")
    else: 
        time_slot.append(str(i) + ".00AM")
        time_slot.append(str(i) + ".30AM")

notify_me = ["Yes", "No"]
category_list = ["None", "Work", "Study", "Exercise", "Leisure", "Others"]

#global var 
today  = datetime.now()
current_year = today.strftime("%Y")
current_month = today.strftime("%B")
current_date = today.strftime("%d")
current_day = today.strftime("%A")
current_page = "Day" 

class PlannerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Planner")
        self.geometry("785x500")
        self.resizable(width=False, height=False)
        self.current_page = "Day"
        self.create_widgets()

    def create_widgets(self):
        self.nav_buttons = {}
        x_position = 270
        for page in pages:
            button = tk.Button(self, text=page, width=3, borderwidth=0, highlightthickness=0,
                               command=lambda p=page: self.show_page(p))
            button.place(x=x_position, y=5)
            self.nav_buttons[page] = button
            x_position += 70
            
        Button(self, text = "<", width = 1, borderwidth = 0, highlightthickness = 0).place(x = 630, y = 20)
        Button(self, text = "Today", width = 3, borderwidth = 0, highlightthickness = 0).place(x = 670, y = 20)
        Button(self, text = ">", width = 1, borderwidth = 0, highlightthickness = 0).place(x = 730, y = 20)
        
        #need to change when user click arrow > or <
        self.today = datetime.now()
        self.date = self.today.strftime("%B %d, %Y")
        Label(self, text = self.date, font = ("Arial", 25, "bold")).place(x = 10, y = 45)
        Label(self, text = self.today.strftime("%A"), font = ("Arial", 20)).place(x = 10, y = 72)

        self.current_frame = None
        self.show_page(self.current_page)

    def show_page(self, page_name):
        if self.current_frame:
            self.current_frame.destroy()

        if page_name == "Day":
            self.current_frame = DayFrame(self)
        # Add similar conditions for "Week" and "Month" pages if needed

class PageFrame(tk.Frame, ABC):
    @abstractmethod 
    def create_widgets(self):
        pass

    @abstractmethod
    def save_data(self):
        pass

    @abstractmethod
    def clear_input(self):
        pass

class DayFrame(PageFrame):
    def __init__(self, master):
        super().__init__(master)
        self.place(x = 0, y = 100, width = 785, height = 490) 
        tableframe = tk.Frame(self, bg="grey")
        # tableframe.place(x = 0, y = 10, width = 445, height = 900)
        self.gen_table_widget(current_date, current_month, current_year)
        self.create_widgets()
        
    def create_widgets(self):
        rightframe = tk.Frame(self, bg="#D9D9D9")
        rightframe.place(x = 444, y = 10, width = 340, height = 900)
        Button(rightframe, text="add", font = ("Arial", 15), width = 5, height = 2, borderwidth=0, highlightthickness=0, pady = 0, background="#ABBBF0").place(x = 20, y = 20)
        inputframe = tk.Frame(rightframe, bg="#ABBBF0")
        inputframe.place(x = 20, y = 50, width = 300, height = 260)
        
        Label(inputframe, text = "Note", font = ("Arial", 15)).place(x = 0, y = 12)
        self.note = tk.Entry(inputframe, borderwidth = 1) 
        self.note.place(x = 90, y = 10)
        
        Label(inputframe, text = "Category", font = ("Arial", 15)).place(x = 0, y = 42)
        self.category = CollapsibleList.create(frame=inputframe, width = 15, datalist=category_list, x = 90, y = 40, canType=True)
        
        Label(inputframe, text = "Time period (From - To)", font = ("Arial", 15)).place(x = 0, y = 70)
        self.start_time = CollapsibleList.create(frame=inputframe, width = 7, datalist=time_slot, x = 90, y = 100)
        self.end_time = CollapsibleList.create(frame=inputframe, width = 7, datalist=time_slot, x = 200, y = 100)
        
        Label(inputframe, text = "Location", font = ("Arial", 15)).place(x = 0, y = 130)
        self.location = tk.Entry(inputframe, width = 15, borderwidth = 1)
        self.location.place(x = 90, y = 130)
        
        Label(inputframe, text = "Notify me", font = ("Arial", 15)).place(x = 0, y = 160)
        self.notify = CollapsibleList.create(frame=inputframe, width = 7, datalist=notify_me, x = 90, y = 160)
        
        Button(inputframe, text="Save", font=("Arial", 15), command = self.save_data,  width = 5, borderwidth=0, highlightthickness=0, pady = 10, background="#ABBBF0").place(x = 190, y = 200)
    
    def gen_table_widget(self, date, month, year):
        file_handler = FileHandling()
        table_frame = tk.Frame(self, bg="grey") 
        table_frame.place(x = 0, y = 10, width = 445, height = 900)
        data = file_handler.load_data('data.pickle')
        
        columns = ['Time', 'Note']
        self.table = ttk.Treeview(table_frame, columns=columns, show='headings')
        self.table.heading('Time', text='Time')
        self.table.heading('Note', text='Note')
        
        self.table.bind('<<TreeviewSelect>>', self.item_selected)
        self.table.place(x = 15, y = 20, width = 400, height = 350)
        
        #help: not sure if it works
        scrollbar = ttk.Scrollbar(table_frame, orient="vertical", command=self.table.yview)
        scrollbar.place(x= 415, y=20, height=350)
        self.table.configure(yscroll=scrollbar.set)
        
        info = []
        if data['Year'] == year and data['Month'] == month:
            for i, j in enumerate(data['Day']):
                if j['Date'] == date:
                    id = 0
                    for time in j['Time_slot']:
                        id += 1
                        info.append((time[str(id)]['start'] + " to "+ time[str(id)]['end'], time[str(id)]['note'] + "@" + time[str(id)]['location']))
                elif i == len(data['Day']) - 1: 
                    print("Date not found")
        else: 
            print("Year/Month not found")
        #help sort time slot
        #info = [('10.30AM to 11.00AM', 'Basketball', 'Gym', 'Yes')]

        for i in info: 
            self.table.insert('', tk.END, values=i)
            
    def clear_table(self):
        for item in self.table.get_children():
            self.table.delete(item)
            
    def item_selected(self, obj, event): #help event = click on the row, find some action 
        for selected_item in obj.selection():
            item = obj.item(selected_item)
            record = item['values']
            tk.showinfo(title='Information', message=','.join(record))
            
    def save_data(self):
        note = self.note.get() 
        category_result = self.category.get()
        start_t = self.start_time.get()
        end_t = self.end_time.get()
        location = self.location.get()
        notify_result = self.notify.get()
        data = [note,category_result, start_t, end_t, location, notify_result]
        file_handler = FileHandling()
        file_handler.save_data(data, 'data.pickle')
        
        self.clear_table()
        self.gen_table_widget(current_date, current_month, current_year)
        self.clear_input()

    def clear_input(self):
        self.note.delete(0, 'end')
        self.category.set('')
        self.location.delete(0, 'end')
        #clear combobox
        self.start_time.set('')
        self.end_time.set('')
        self.notify.set('')

class CollapsibleList:
    @staticmethod
    def create(frame, width, datalist, x, y, canType=False):
        data = tk.StringVar()
        data_combobox = ttk.Combobox(frame, width=width, textvariable=data)
        data_combobox['value'] = datalist
        if not canType:
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
        location = data[4]
        notify_result = data[5]
        
        if note == "" or category == "" or location == "" or start_t == "" or end_t == "" or notify_result == "":
            tk.messagebox.showerror(title="incomplete info", message="Please fill in all the information", icon="warning")
        else:
            start = float(start_t[:len(start_t)-2]) 
            end = float(end_t[:len(end_t)-2]) 
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
                    
                #help : when save = info from db not add to table 
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
                
                print(loaded_data)
                
if __name__ == "__main__":
    planner = PlannerApp()
    planner.mainloop()
