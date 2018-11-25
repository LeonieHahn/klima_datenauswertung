# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 20:07:42 2018

@author: kgn
"""


class Measurement:

    def __init__(self, m_id, datum, temp_1, water_1, temp_2, water_2):
        self._id = m_id
        self._datum = datum
        self._temp_1 = temp_1
        self._water_1 = water_1
        self._temp_2 = temp_2
        self._water_2 = water_2

    @property
    def id(self):
        return self._id

    @property
    def datum(self):
        return self._datum

    @property
    def temp_1(self):
        return self._temp_1

    @property
    def water_1(self):
        return self._water_1

    @property
    def temp_2(self):
        return self._temp_2

    @property
    def water_2(self):
        return self._water_2

    def getKey(custom):
        return custom.datum


class DateWithoutSeconds:

    def __init__(self, year, month, day, hour, minute):
        self.id = id
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute

    def __eq__(self, other):
        if (self.year == other.year) & (self.month == other.month) & (self.day == other.day) & (
                self.hour == other.hour):
            return abs(self.minute - other.minute) <= 15
