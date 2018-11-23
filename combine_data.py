# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 19:42:08 2018

@author: kgn
"""

import csv
from Measurement import Measurement
from datetime import datetime
from datetime import timedelta


def main():
    my_csvs = ['LC3_2017.06.04.csv',
               'LC3_2018.02.02.csv']
    data_set_complete =[]
    
    for csv_file in my_csvs:
        # data_set_complete = data_set_complete + import_one_csv(csv_file)
        
        data_set_complete += import_one_csv(csv_file)
    
    #sort by date
    
    fill_missing_dates(data_set_complete)
    
def fill_missing_dates(data_set):
    calendar = import_calendar()
    # get calendar on same date as measurement
    for index_m in range(len(data_set) - 1):
        for index_c in range(len(calendar)):
            print(calendar[index_c])
            print(data_set[index_m].datum)
            date_calendar = datetime.date(calendar[index_c].year,
                                 calendar[index_c].day, 
                                 calendar[index_c].month,
                                 calendar[index_c].hour,
                                 calendar[index_c].minute)
            date_data_set = datetime.date(data_set[index_c].year,
                                 data_set[index_c].day, 
                                 data_set[index_c].month,
                                 data_set[index_c].hour,
                                 data_set[index_c].minute)
            
            if calendar[index_c] == data_set[index_m].datum:
                print (index_c)
    #check if next date in measurement is next date in calendar 
    
    # if not insert a empty measurement
    
    
    
        
        current_date = data_set[index_m].datum
    
        next_date = data_set[index_m + 1].datum
        
        
        if not pow(int(current_date.minute) - int(next_date.minute),2) == pow(30, 2):
            if not current_date.hour == next_date.hour or current_date.hour == next_date.hour +1:
                if not current_date.day == next_date.day or current_date.day == next_date.day + 1 :
                    print ("Halt")
                    print (f'current {current_date} next {next_date}')
        c = current_date.day + 2
        d = current_date.day +1        
        
def import_calendar():
    with open("kalender.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        calendar = []
        for row in csv_reader:
            datetime_object = datetime.strptime(row[0], '%d.%m.%Y %H:%M')
            calendar.append(datetime_object)
        return calendar
        
def import_one_csv(csv_file_name):
    with open(csv_file_name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        
        data_set = []
        measurement = None
        for row in csv_reader:
            # Titel-Name
            if line_count == 0:
                # print(f'Title {row[0]}')
                line_count += 1
            # Spalten-Name
            elif line_count == 1:
                # print(f'Column names  {", ".join(row)}')
                line_count += 1
            else:
                id = int(row[0])
                # datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')  
                datetime_object = datetime.strptime(row[1], '%m/%d/%y %H:%M:%S %p') 
                temp_1 = float(row[2])
                water_1 = float(row[3])
                temp_2 = float(row[4])
                water_2 = float(row[5])
                
                if line_count < 1:
                    print(f'\tIndex: {row[0]} Date {row[1]} Temp1 {row[2]} Water1 {row[3]} Temp2 {row[4]} Water2 {row[5]} ')
                
                #objekt measurement vond der Klasse Measurement wird erstellt
                measurement = Measurement(id , datetime_object, temp_1, water_1, temp_2, water_2) 
                data_set.append(measurement)
                line_count += 1
        
        print(f'Processed {line_count} lines from {csv_file_name}.')
        return data_set
        
    
    
main()
    
    
    
    