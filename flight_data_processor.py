import enum
from xmlrpc.client import DateTime


def flight_data_processor(list_data):
    flight_data= {
        'flight_number':'',
        'departure_time' :'',
        'arrival_time':'',
        #'duration_minutes':'',
        'status':''
    }
    #list_data = ['AZ001', '2025-02-19 15:30', '2025-02-20 03:45', 'ON_TIME']
    #dict.get(list_data)
    # for i, key in enumerate(dict):
    #     dict.update({key:list_data[i]})
    res = dict (zip (flight_data, list_data))

    print(str(res))
    return res
flight_data_processor(['AZ001', '2025-02-19 15:30', '2025-02-20 03:45', 'ON_TIME'])


 # dict={'flight_number':str,'departure_time' :DateTime, 'arrival_time':DateTime,'duration_minutes':int,'status':enum}
 # print(dict)


