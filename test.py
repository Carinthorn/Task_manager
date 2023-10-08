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

from datetime import datetime

current_year = datetime.now().strftime("%Y")
current_month = datetime.now().strftime("%B")
current_date = datetime.now().strftime("%d")
current_day = datetime.now().strftime("%A")

data = {
    'Year': "2023",
    'Month': "October",
    'Day' : [
        {
            'Date': "07",
            'Day_of_week' : "Sunday",
            'Time_slot' : [
                {
                    '1' : {
                        'note' : "BB", 
                        'category' : "Work",
                        'location' : "G",
                        'start' : "12.30AM",
                        'end' : "13.00AM",
                        'notify_me' : "Yes"
                    }
                }
            ]
        },
        {
            'Date': "08",
            'Day_of_week' : "Sunday",
            'Time_slot' : [
                {
                    '1' : {
                        'note' : "Basketball", 
                        'category' : "None",
                        'location' : "Gym",
                        'start' : "10.30AM",
                        'end' : "11.00AM",
                        'notify_me' : "Yes"
                    }
                }
            ]
        }
    ]
}
year = "2023"
month = "October"
date = "08"
info = []

# for i in data: 
#     if i['Year'] == year and i['Month'] == month:
#         for j in i['Day']:
#             if j['Date'] == date:
#                 for time in j['Time_slot']:
#                     for t in time:
#                         info.append((t['start'] + " to "+ t['end'], t['note'], t['location'], t['notify_me']))
 
 
#year, month, date, start, end, note, location, notify_me
# print(data['Year'])
# print(data['Month'])
# print(data['Day'][0]['Date'])
# print(data['Day'][0]['Time_slot'][0]['1']['start'])
# print(data['Day'][0]['Time_slot'][0]['1']['end'])
# print(data['Day'][0]['Time_slot'][0]['1']['note'])
# print(data['Day'][0]['Time_slot'][0]['1']['location'])
# print(data['Day'][0]['Time_slot'][0]['1']['notify_me'])

if data['Year'] == year and data['Month'] == month:
    for i, j in enumerate(data['Day']):
        if j['Date'] == date:
            id = 0
            for time in j['Time_slot']:
                id += 1
                info.append((time[str(id)]['start'] + " to "+ time[str(id)]['end'], time[str(id)]['note'], time[str(id)]['location'], time[str(id)]['notify_me']))
        elif i == len(data['Day']) - 1: 
            print("Date not found")
else: 
    print("Year/Month not found")
for i in info:
    print(i)

