# import pickle


# data = {
#     'Year': '2023',
#     'Month': 'Oct',
#     'Day' : [
#         {
#             'Date': '2',
#             'Day_of_week' : 'Tues',
#             'Time_slot' : [
#                 {
#                     '1' : {
#                         'note' : 'sleep', 
#                         'category' : 'none',
#                         'location' : 'home',
#                         'start' : '10.30AM',
#                         'end' : '11.00AM',
#                         'notify_me' : 'Yes'
#                     }
                    
#                 }
#             ]
#         }
#     ]
# }

# with open('data.pickle', 'wb') as file: 
#     pickle.dump(data, file)
    
# loaded_data = None
# with open('data.pickle', 'rb') as file: 
#     loaded_data = pickle.load(file)

# for i, n in enumerate(loaded_data['Day']):
#     if n['Date'] == '2':
#         n['Time_slot'].append({'2' : {
#                         'note' : 'hangout', 
#                         'category' : 'none',
#                         'location' : 'mall',
#                         'start' : '10.30AM',
#                         'end' : '11.00AM',
#                         'notify_me' : 'Yes'
#                     }})
#     elif i == len(loaded_data['Day']) - 1: 
#         loaded_data['Day'].append({'Date': '2',
#             'Day_of_week' : 'Tues',
#             'Time_slot' : [
#                 {
#                     '1' : {
#                         'note' : 'sleep', 
#                         'category' : 'none',
#                         'location' : 'home',
#                         'start' : '10.30AM',
#                         'end' : '11.00AM',
#                         'notify_me' : 'Yes'
#                     }
                    
#                 }
#             ]})
        
# word = "10.30AM"
# start = float(word[:len(word)-2])
# print(start)

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.messagebox import showinfo
from calendar import month_name

root = tk.Tk()

# config the root window
root.geometry('300x200')
root.resizable(False, False)
root.title('Combobox Widget')

# label
label = ttk.Label(text="Please select a month:")
label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_month = tk.StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_month)

# get first 3 letters of every month name
month_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]

# prevent typing a value
month_cb['state'] = 'readonly'

# place the widget
month_cb.pack(fill=tk.X, padx=5, pady=5)

# class InvalidValueError(Exception): 
#     pass

# try: 
#     if selected_month not in month_cb['values']:
#         raise InvalidValueError()
# except InvalidValueError: 
#     showinfo(
#         tk.messagebox.showerror(title="invalid start end time", message= "Start time cannot be later than End time", icon="warning")
#     )
    

# bind the selected value changes
def month_changed(event):
    """ handle the month changed event """
    showinfo(
        title='Result',
        message=f'You selected {selected_month.get()}!'
    )

month_cb.bind('<<ComboboxSelected>>', month_changed)



root.mainloop()