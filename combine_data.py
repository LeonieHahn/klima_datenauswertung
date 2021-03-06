# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 19:42:08 2018

@author: kgn
"""

import csv
from Measurement import Measurement, DateWithoutSeconds
from datetime import datetime


class DataParser(object):

    def __init__(self):
        self._csv_file = None
        self._calendar = self.import_calendar()
        self._data_set = []
        self._file_no = 0

    def pass_file(self, csv_file_name):
        self._csv_file = csv_file_name

    def set_full_data_set(self, full_data_set):
        self._data_set = full_data_set

    def fill_missing_dates(self):
        calendar = self._calendar
        data_set = self._data_set
        # get calendar on same date as measurement
        calendar_index = self.get_same_start()

        new_data_set = []
        for index_m in range(len(data_set) - 1):
            # check if next date in measurement is next date in calendar
            # print(index_m)
            # if not insert a empty measurement
            current_date = data_set[index_m].datum
            next_date = data_set[index_m + 1].datum
            new_data_set.append(data_set[index_m])
            if not abs(int(current_date.minute) - int(next_date.minute)) == 30:

                print("next data set detected!")
                print(f'current {current_date} next {next_date}')

                next_measurement = index_m + 1
                while not self.the_same(calendar_index, next_measurement):
                    new_data_set.append(Measurement(None, calendar[calendar_index], None, None, None, None))
                    calendar_index += 1

                print("next data set appended!")

        return new_data_set

    def the_same(self, index_c, index_m):
        calendar = self._calendar
        data_set = self._data_set
        data_date = DateWithoutSeconds(year=data_set[index_m].datum.year,
                                       month=data_set[index_m].datum.month,
                                       day=data_set[index_m].datum.day,
                                       hour=data_set[index_m].datum.hour,
                                       minute=data_set[index_m].datum.minute)
        calendar_date = DateWithoutSeconds(year=calendar[index_c].year,
                                           month=calendar[index_c].month,
                                           day=calendar[index_c].day,
                                           hour=calendar[index_c].hour,
                                           minute=calendar[index_c].minute
                                           )

        return data_date == calendar_date

    def get_same_start(self):
        calendar = self._calendar
        data_set = self._data_set
        for index_m in range(len(data_set) - 1):
            for index_c in range(len(calendar)):
                if self.the_same(index_c, index_m):
                    return index_c

    @staticmethod
    def import_calendar():
        with open("Calendar/kalender.csv") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            calendar = []
            for row in csv_reader:
                datetime_object = datetime.strptime(row[0], '%d.%m.%Y %H:%M')
                calendar.append(datetime_object)
            return calendar

    def import_one_csv(self):
        if self._csv_file:
            self._file_no += 1
            with open(self._csv_file) as csv_file:
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
                            print(
                                f'\tIndex: {row[0]} Date {row[1]} Temp1 {row[2]} Water1 {row[3]} Temp2 {row[4]} Water2 {row[5]} ')

                        # objekt measurement von der Klasse Measurement wird erstellt
                        measurement = Measurement(f'{self._file_no}_{id}', datetime_object, temp_1, water_1, temp_2,
                                                  water_2)
                        data_set.append(measurement)
                        line_count += 1

                print(f'Processed {line_count} lines from {self._csv_file}.')
                return data_set
